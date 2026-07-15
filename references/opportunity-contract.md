# Opportunity Contract

Use this contract for every shortlisted, saved, or machine-readable opportunity. Keep chat-only Top 10 lists lightweight, but normalize Top 3 records before handing them to `business-lens`.

## Contract

```json
{
  "schema_version": "idea-opportunity/v1",
  "id": "opportunity-short-id",
  "name": "Opportunity name",
  "user": "Narrow user group",
  "buyer": "Buyer hypothesis or unknown",
  "scene": "Repeated scene",
  "pain": "Observed problem and cost",
  "current_workaround": "What happens today",
  "product_shape": "Smallest plausible product shape",
  "input": "Concrete input",
  "output": "Concrete output",
  "source_support": ["Fact or signal supported by the source"],
  "inferences": ["Agent inference, kept separate from source facts"],
  "uncertainties": ["Unknown that requires validation"],
  "why_now": "Timing or trigger hypothesis",
  "confidence": "high",
  "validation": {
    "source_support": true,
    "transferability": true,
    "product_sharpness": true
  },
  "status": "verified",
  "rejection_reason": ""
}
```

## Field Rules

- Use `schema_version: idea-opportunity/v1`.
- Keep `id` stable within one opportunity list or source pack.
- Use `buyer: unknown` when the payer is not known. Do not invent one.
- Put only source-supported statements in `source_support`.
- Put interpretation and product logic in `inferences`.
- Keep at least one falsifiable unknown in `uncertainties`.
- Use `confidence: high | medium | low` for source support, not market demand.
- Use `status: candidate | verified | rejected`.
- Require all three validation checks for `verified`.
- Require `rejection_reason` for `rejected`.

## Business Lens Handoff

Hand `verified` records to `business-lens`. Business Lens owns:

- buyer and budget confirmation
- value creation and value capture
- acquisition path
- business model
- fatal assumption
- proceed / reshape / park / reject decision

Idea Spark must not fill those fields with false certainty.

## Validation

For saved JSON or reusable handoffs, run:

```bash
python scripts/validate_opportunity.py opportunity.json
```

The validator checks structure and handoff readiness. It does not prove demand or commercial viability.
