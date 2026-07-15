# Source Pack Workflow

Use this when a book, course, folder, document set, or recurring source should become a reusable opportunity asset.

The goal is not to summarize the source. The goal is to compile it into a product-opportunity pack that can be reused without re-reading the whole material.

## Pack Shape

```text
source-pack/
  overview.md
  signal-map.md
  opportunity-candidates.md
  verified-opportunities.md
  rejected-opportunities.md
  opportunity-records.json
  decision-cheatsheet.md
```

For OPC, do not create this directory unless the user explicitly asks to save or land the artifact.

## Files

- `overview.md`: source topic, audience, sections, and what the source is useful for.
- `signal-map.md`: repeated pains, workflows, information gaps, decisions, artifacts, and handoffs.
- `opportunity-candidates.md`: generated opportunities with candidate records.
- `verified-opportunities.md`: candidates that passed verification and why.
- `rejected-opportunities.md`: rejected ideas and failed checks.
- `opportunity-records.json`: optional machine-readable Top 3 and rejected records that follow `references/opportunity-contract.md`.
- `decision-cheatsheet.md`: compact decision rules for future ideation from this source.

## Compile Rules

- Extract structure, not summaries.
- Preserve exact terms only when they affect product shape.
- Convert frameworks into "when to use / input / output / failure mode".
- Keep the master overview lean; put detail in supporting files.
- Make every opportunity traceable to source support and inference.
- Validate `opportunity-records.json` with `python scripts/validate_opportunity.py <file>` before treating the pack as reusable.

## Update Mode

When adding new material to an existing pack:

1. Read existing `overview.md`, `signal-map.md`, `verified-opportunities.md`, and `rejected-opportunities.md`.
2. Decide whether new material revises existing signals or adds new ones.
3. Append or revise candidate records.
4. Do not erase old rejected ideas unless the user asks.
