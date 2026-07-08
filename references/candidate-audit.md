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

```yaml
id:
name:
user:
scene:
pain:
current_workaround:
input:
output:
product_shape:
source_support:
inference:
uncertainty:
verification:
  repeated_signal:
  transferability:
  product_sharpness:
status: candidate | verified | rejected
rejection_reason:
```

## Why Keep Rejected Ideas

Rejected ideas prevent the agent from re-suggesting weak concepts later. They also show whether the filter is too strict or too loose.

For serious work, a good run should reject a meaningful number of ideas. If all 10 pass, the verification is probably too soft.
