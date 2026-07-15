#!/usr/bin/env python3
"""Validate idea-spark opportunity records without external dependencies."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "idea-opportunity/v1"
REQUIRED_STRINGS = (
    "schema_version",
    "id",
    "name",
    "user",
    "scene",
    "pain",
    "current_workaround",
    "product_shape",
    "input",
    "output",
    "why_now",
    "confidence",
    "status",
)
LIST_FIELDS = ("source_support", "inferences", "uncertainties")
VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_STATUS = {"candidate", "verified", "rejected"}
VALIDATION_KEYS = ("source_support", "transferability", "product_sharpness")


def read_payload(source: str) -> Any:
    if source == "-":
        return json.load(sys.stdin)
    return json.loads(Path(source).read_text(encoding="utf-8"))


def normalize_records(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict) and "opportunities" in payload:
        payload = payload["opportunities"]
    if isinstance(payload, dict):
        return [payload]
    if isinstance(payload, list) and all(isinstance(item, dict) for item in payload):
        return payload
    raise ValueError("Expected an opportunity object, a list of objects, or an object with 'opportunities'.")


def validate_record(record: dict[str, Any], index: int) -> list[str]:
    prefix = f"record[{index}]"
    errors: list[str] = []

    for field in REQUIRED_STRINGS:
        value = record.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{prefix}.{field}: required non-empty string")

    status = record.get("status")

    for field in LIST_FIELDS:
        value = record.get(field)
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            errors.append(f"{prefix}.{field}: required list of non-empty strings")
        elif not value and (field != "source_support" or status != "rejected"):
            errors.append(f"{prefix}.{field}: must not be empty")

    if record.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{prefix}.schema_version: expected '{SCHEMA_VERSION}'")

    if record.get("confidence") not in VALID_CONFIDENCE:
        errors.append(f"{prefix}.confidence: expected one of {sorted(VALID_CONFIDENCE)}")

    if status not in VALID_STATUS:
        errors.append(f"{prefix}.status: expected one of {sorted(VALID_STATUS)}")

    buyer = record.get("buyer", "unknown")
    if not isinstance(buyer, str) or not buyer.strip():
        errors.append(f"{prefix}.buyer: expected a non-empty string, 'unknown', or omit the field")

    validation = record.get("validation")
    if not isinstance(validation, dict):
        errors.append(f"{prefix}.validation: required object")
    else:
        for key in VALIDATION_KEYS:
            if not isinstance(validation.get(key), bool):
                errors.append(f"{prefix}.validation.{key}: required boolean")
        if status == "verified" and not all(validation.get(key) is True for key in VALIDATION_KEYS):
            errors.append(f"{prefix}.validation: verified records must pass all checks")

    if status == "rejected":
        reason = record.get("rejection_reason")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"{prefix}.rejection_reason: required for rejected records")

    return errors


def validate_payload(payload: Any) -> tuple[list[dict[str, Any]], list[str]]:
    records = normalize_records(payload)
    if not records:
        return records, ["payload: expected at least one opportunity record"]
    errors: list[str] = []
    for index, record in enumerate(records):
        errors.extend(validate_record(record, index))
    ids = [record.get("id") for record in records if isinstance(record.get("id"), str)]
    duplicates = sorted({record_id for record_id in ids if ids.count(record_id) > 1})
    for record_id in duplicates:
        errors.append(f"payload.id: duplicate opportunity id '{record_id}'")
    return records, errors


def self_test() -> int:
    valid = {
        "schema_version": SCHEMA_VERSION,
        "id": "opportunity-demo-001",
        "name": "Demo opportunity",
        "user": "Independent consultants",
        "buyer": "unknown",
        "scene": "After a customer interview",
        "pain": "Notes do not become reusable decisions",
        "current_workaround": "Manual copy and summary",
        "product_shape": "diagnostic assistant",
        "input": "Interview notes",
        "output": "Decision-ready opportunity card",
        "source_support": ["The source shows repeated manual synthesis"],
        "inferences": ["A structured assistant may reduce rework"],
        "uncertainties": ["Whether consultants will change their workflow"],
        "why_now": "More customer discovery is being recorded with AI",
        "confidence": "medium",
        "validation": {
            "source_support": True,
            "transferability": True,
            "product_sharpness": True,
        },
        "status": "verified",
        "rejection_reason": "",
    }
    _, valid_errors = validate_payload(valid)
    if valid_errors:
        print("Self-test failed on valid record:", valid_errors, file=sys.stderr)
        return 1

    invalid = dict(valid)
    invalid["status"] = "rejected"
    invalid["rejection_reason"] = ""
    _, invalid_errors = validate_payload(invalid)
    if not invalid_errors:
        print("Self-test failed to reject invalid record", file=sys.stderr)
        return 1

    print("Self-test passed.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate idea-spark opportunity JSON.")
    parser.add_argument("source", nargs="?", help="JSON file path, or '-' for stdin")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.source:
        parser.error("source is required unless --self-test is used")

    try:
        records, errors = validate_payload(read_payload(args.source))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Validation input error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps({"valid": not errors, "records": len(records), "errors": errors}, ensure_ascii=False, indent=2))
    elif errors:
        print("Opportunity validation failed:")
        for error in errors:
            print(f"- {error}")
    else:
        print(f"Opportunity validation passed for {len(records)} record(s).")

    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
