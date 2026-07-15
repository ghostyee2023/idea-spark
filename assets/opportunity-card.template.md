---
title: "Opportunity: {{NAME}}"
type: product-opportunity
status: candidate
schema_version: idea-opportunity/v1
opportunity_id: "{{OPPORTUNITY_ID}}"
source_id: "{{SOURCE_ID}}"
source: "{{SOURCE_REFERENCE}}"
confidence: 0.35
confidence_level: unverified
relationships: []
---

# Opportunity: {{NAME}}

## One-Sentence Definition

For {{USER}}, when {{SCENE}}, turn {{INPUT}} into {{OUTPUT}} so they can {{JOB_TO_BE_DONE}}.

## Source Support

- {{SOURCE_FACT_1}}
- {{SOURCE_FACT_2}}

## Agent Inference

- {{INFERENCE_1}}

## User And Workflow

- User: {{USER}}
- Buyer hypothesis: {{BUYER_OR_UNKNOWN}}
- Scene: {{SCENE}}
- Pain: {{PAIN}}
- Current workaround: {{CURRENT_WORKAROUND}}
- Product shape: {{PRODUCT_SHAPE}}
- Input: {{INPUT}}
- Output: {{OUTPUT}}

## Uncertainties

- {{UNCERTAINTY_1}}

## Verification

- Source support: {{PASS_OR_FAIL}}
- Transferability: {{PASS_OR_FAIL}}
- Product sharpness: {{PASS_OR_FAIL}}
- Confidence: {{HIGH_MEDIUM_LOW}}

## Pressure Test

- Strongest trigger: {{TRIGGER}}
- Strongest rejection reason: {{REJECTION_RISK}}
- Edge case: {{EDGE_CASE}}
- Decision: {{KEEP_RESHAPE_REJECT}}

## Business Lens Handoff

- Status: pending_business_lens
- Why now: {{WHY_NOW}}
- Buyer unknowns: {{BUYER_UNKNOWNS}}
- First commercial question: {{COMMERCIAL_QUESTION}}

## Next Boundary

Do not start development or sales action until `business-lens` returns `proceed` or a directed `reshape`, unless the user explicitly accepts skipping commercial judgment for a prototype-only experiment.
