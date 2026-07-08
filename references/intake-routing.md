# Intake Routing

Use this before ideating.

## Route Table

| Input | Route | Action |
| --- | --- | --- |
| Clear product idea | Maker Forge | Do not generate more ideas unless asked. Hand off for evaluation. |
| Raw source material | Idea Spark | Extract productizable signals and generate candidates. |
| Vague desire to make something | Diagnosis | Ask at most 2 questions, then choose a default lane. |
| Existing opportunity list | Review | Verify, reject weak items, then hand off the strongest to Maker Forge. |
| Request to save or reuse a source | Source Pack | Compile a reusable opportunity pack. |

## Vague Need Diagnosis

Ask only what changes the route:

- Source lane: "Do you want ideas from a specific book/material, or from your own experience/problem?"
- User lane: "Who should the product serve first?"

If the user does not answer, default to:

```text
source = current material or user problem
target user = the user group implied by the material
output = 10 ideas + Top 3 + Maker Forge handoff
```

## Early Handoff

If the user already gives a clear candidate such as "I want to build X for Y", route to Maker Forge. Idea Spark should not dilute a concrete opportunity with unnecessary brainstorming.
