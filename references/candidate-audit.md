# Candidate Audit

Use this when the ideation output may become a saved product asset, workshop artifact, or follow-up build task.

## Audit Structure

Keep four lists:

```text
source_signals:
  - what the material actually supports

candidates:
  - all generated product opportunities

verified:
  - candidates that passed verification and why

rejected:
  - candidates that failed and which check they failed
```

## Candidate Record

Use the full contract in `references/opportunity-contract.md` for Top 3, saved, or machine-readable records. For working candidates, preserve at least:

```yaml
schema_version: idea-opportunity/v1
id:
name:
user:
buyer: unknown
scene:
pain:
current_workaround:
input:
output:
product_shape:
source_support: []
inferences: []
uncertainties: []
why_now:
confidence: high | medium | low
verification:
  source_support:
  transferability:
  product_sharpness:
status: candidate | verified | rejected
rejection_reason:
```

## Why Keep Rejected Ideas

Rejected ideas prevent the agent from re-suggesting weak concepts later. They also show whether the filter is too strict or too loose.

For serious work, a good run should reject a meaningful number of ideas. If all 10 pass, the verification is probably too soft.
