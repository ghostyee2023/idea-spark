---
name: idea-spark
description: "Turn raw materials, books, notes, articles, documents, trends, conversations, customer complaints, personal experiences, or vague product curiosity into source-grounded, auditable small product opportunities. Use when the user asks to find, generate, brainstorm, discover, compare, or extract product ideas from source material or an unclear problem. Output verified candidate records for business-lens; do not use for commercial judgment or MVP design."
---

# 灵感火花 Idea Spark

Version: v0.3.0

## Core Rule

Generate product opportunities from source signals, not random ideas.

Always separate:

- what the source material actually says
- what the agent infers
- what product opportunity emerges
- what remains unverified
- what should be handed to `business-lens`

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

If the user already has a clear product idea, use `business-lens`. Route directly to `maker-forge` only when the user explicitly wants a prototype plan and accepts that commercial judgment remains incomplete.

## Operating Modes

Use lite mode by default:

1. Route the input: clear idea, raw source, vague need, or update to an existing opportunity list.
2. Clarify the source and target user only when the missing answer changes the output.
3. Extract pain signals, repeated workflows, information gaps, decision bottlenecks, and toolable moments.
4. Generate 10 small product opportunities.
5. Verify and reject weak candidates.
6. Select Top 3.
7. Hand off the strongest 1-3 candidates to `business-lens`.
8. Stop at the commercial-judgment boundary unless the user separately invokes the downstream MVP workflow.

Use source-pack mode when the user asks to turn a book, course, document set, or recurring source into a reusable opportunity asset. Read `references/source-pack-workflow.md`.

Use full mode only when the user asks for a formal report, saved artifact, workshop, product strategy, or reusable source pack.

## Workflow

1. Identify the input type.
   Classify it as book, article, notes, course material, trend, conversation, customer complaint, personal experience, or vague problem. If unclear, infer and mark assumptions.

2. Route the input.
   Use the routing table in `references/intake-routing.md`. If the input is a clear product idea, stop ideation and route to `business-lens`.

3. Extract source signals.
   Use `references/source-to-opportunity-workflow.md`.

4. Check host context only when useful.
   Read `references/host-integration.md` when the host has registered search, structured extraction, confidence, relationship, or execution capabilities. Keep the check read-only unless the user asks to save.

5. Generate candidates.
   Use multiple lenses from `references/ideation-patterns.md`: workflow tool, decision aid, template system, diagnostic agent, transformation engine, micro database, browser plugin, operating checklist, training product, or service-assisted MVP.

6. Verify candidates.
   Use `references/opportunity-verification.md`. Keep a short rejected list so weak ideas do not silently disappear.

7. Build an audit trail.
   Use `references/candidate-audit.md` when the source is long, ambiguous, or the output may later become a product asset. Normalize shortlisted records with `references/opportunity-contract.md`.

8. Select Top 3.
   Prefer opportunities with repeated pain, clear input/output, reachable users, and a small first version.

9. Pressure-test the shortlist.
   Use `references/pressure-test.md` when the user asks which idea to build, asks for a serious recommendation, or plans to save the result.

10. Validate reusable handoffs.
    For saved or machine-readable opportunity JSON, run `python scripts/validate_opportunity.py <file>`. Do not treat structural validation as market validation.

11. Hand off to Business Lens.
    Pass only `verified` records that follow `references/opportunity-contract.md`. Leave unknown buyers and budgets explicit. Do not replace the complete handoff records with a prose summary.

12. Output or save the result.
    Use `references/output-template.md` for normal responses. When the user asks to save an opportunity, start from `assets/opportunity-card.template.md` and follow the host write boundary.

## Boundaries

- Do not expose private paths, internal project names, unpublished customer details, or source collection metadata.
- Do not expose external inspiration sources in normal outputs. Say "method pattern" or "sanitized case pattern" when needed.
- Do not write files unless the user asks to save, create, land, or sync.
- Do not turn every observation into a product. Preserve rejected ideas and reasons.
- Do not skip `business-lens` when the user asks whether an idea is a business opportunity.
- Do not place idea-stage candidates into an execution queue or start development without a downstream commercial decision, unless the user explicitly accepts a prototype-only experiment.
- Do not present creative confidence as market validation.

## References

- `references/source-to-opportunity-workflow.md`: use for extracting productizable signals from raw material.
- `references/intake-routing.md`: use to decide whether to ideate, compile a source pack, or hand off to business-lens.
- `references/ideation-patterns.md`: use for multi-lens product opportunity generation.
- `references/opportunity-verification.md`: use for verification, rejection, and Top 3 selection.
- `references/candidate-audit.md`: use to preserve candidates, rejected ideas, source support, and uncertainty.
- `references/opportunity-contract.md`: use to normalize Top 3, saved, and machine-readable opportunity records.
- `references/host-integration.md`: use only when the host has registered search, extraction, confidence, relationship, or execution capabilities.
- `references/source-pack-workflow.md`: use when creating a reusable opportunity pack from a book, course, or document set.
- `references/pressure-test.md`: use to test whether the Top 3 are distinct, triggerable, and buildable.
- `references/output-template.md`: use for normal user-facing outputs.
- `assets/opportunity-card.template.md`: use when the user asks to save a standalone opportunity card.
- `scripts/validate_opportunity.py`: use to validate saved JSON handoffs.
