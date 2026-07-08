---
name: idea-spark
description: "Turn raw materials, books, notes, articles, documents, trends, conversations, customer complaints, personal experiences, or vague product curiosity into useful and interesting small product opportunities. Use when the user asks to find, generate, brainstorm, discover, or extract product ideas from source material or an unclear problem. Output candidate opportunities; hand off commercial judgment to business-lens and MVP shaping to maker-forge."
---

# 灵感火花 Idea Spark

Version: v0.2.0

## Core Rule

Generate product opportunities from source signals, not random ideas.

Always separate:

- what the source material actually says
- what the agent infers
- what product opportunity emerges
- what remains unverified
- what should be handed to `maker-forge`

Do not claim that a source signal proves market demand. A book, note, trend, or conversation can reveal pain, workflow, language, and hidden demand, but real users still need validation.

Keep external inspirations sanitized. Use method patterns, not source names, links, author names, repository names, or collection metadata in user-facing outputs unless the user explicitly asks for bibliography.

## Positioning

Idea Spark is the upstream ideation skill:

```text
raw material / vague problem
-> pain and workflow extraction
-> candidate small product opportunities
-> verification and rejection
-> Top 3 opportunities
-> handoff to business-lens
-> optional handoff to maker-forge
```

Business Lens is the commercial judgment skill:

```text
candidate opportunity
-> buyer
-> business logic
-> monetization
-> acquisition path
-> proceed / reshape / park / reject
```

Maker Forge is the downstream MVP skill:

```text
commercially plausible opportunity
-> demand sentence
-> case analogy
-> risk and score
-> 3-hour MVP
```

If the user already has a clear product idea, use `maker-forge` directly.

## Operating Modes

Use lite mode by default:

1. Route the input: clear idea, raw source, vague need, or update to an existing opportunity list.
2. Clarify the source and target user only when the missing answer changes the output.
3. Extract pain signals, repeated workflows, information gaps, decision bottlenecks, and toolable moments.
4. Generate 10 small product opportunities.
5. Verify and reject weak candidates.
6. Select Top 3.
7. Hand off the strongest 1-3 candidates to `business-lens`.
8. Hand off to `maker-forge` only when the user wants an MVP or a candidate passes commercial judgment.

Use source-pack mode when the user asks to turn a book, course, document set, or recurring source into a reusable opportunity asset. Read `references/source-pack-workflow.md`.

Use full mode only when the user asks for a formal report, saved artifact, workshop, product strategy, or reusable source pack.

## Workflow

1. Identify the input type.
   Classify it as book, article, notes, course material, trend, conversation, customer complaint, personal experience, or vague problem. If unclear, infer and mark assumptions.

2. Route the input.
   Use the routing table in `references/intake-routing.md`. If the input is a clear product idea, stop ideation and route to `maker-forge`.

3. Extract source signals.
   Use `references/source-to-opportunity-workflow.md`.

4. Generate candidates.
   Use multiple lenses from `references/ideation-patterns.md`: workflow tool, decision aid, template system, diagnostic agent, transformation engine, micro database, browser plugin, operating checklist, training product, or service-assisted MVP.

5. Verify candidates.
   Use `references/opportunity-verification.md`. Keep a short rejected list so weak ideas do not silently disappear.

6. Build an audit trail.
   Use `references/candidate-audit.md` when the source is long, ambiguous, or the output may later become a product asset.

7. Select Top 3.
   Prefer opportunities with repeated pain, clear input/output, reachable users, and a small first version.

8. Pressure-test the shortlist.
   Use `references/pressure-test.md` when the user asks which idea to build, asks for a serious recommendation, or plans to save the result.

9. Hand off to Business Lens.
   Format each selected candidate with:

   ```text
   name:
   user:
   buyer:
   scene:
   pain:
   current workaround:
   product shape:
   input:
   output:
   source signal:
   uncertainty:
   why now:
   ```

10. Hand off to Maker Forge only if needed.
   If the user asks "how do I build first version", pass the Business Lens result to `maker-forge`.

11. Output the result.
   Use `references/output-template.md` unless the user asks for a different format.

## Boundaries

- Do not expose private paths, internal project names, unpublished customer details, or source collection metadata.
- Do not expose external inspiration sources in normal outputs. Say "method pattern" or "sanitized case pattern" when needed.
- Do not write files unless the user asks to save, create, land, or sync.
- Do not turn every observation into a product. Preserve rejected ideas and reasons.
- Do not skip `business-lens` when the user asks whether an idea is a business opportunity.
- Do not skip `maker-forge` when the user asks how to build the first MVP.
- Do not present creative confidence as market validation.

## References

- `references/source-to-opportunity-workflow.md`: use for extracting productizable signals from raw material.
- `references/intake-routing.md`: use to decide whether to ideate, compile a source pack, or hand off to maker-forge.
- `references/ideation-patterns.md`: use for multi-lens product opportunity generation.
- `references/opportunity-verification.md`: use for verification, rejection, and Top 3 selection.
- `references/candidate-audit.md`: use to preserve candidates, rejected ideas, source support, and uncertainty.
- `references/source-pack-workflow.md`: use when creating a reusable opportunity pack from a book, course, or document set.
- `references/pressure-test.md`: use to test whether the Top 3 are distinct, triggerable, and buildable.
- `references/output-template.md`: use for normal user-facing outputs.
