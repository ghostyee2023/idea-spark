# Host Integration

Use host capabilities only when the host project has registered and enabled them. Keep Idea Spark portable and fall back to the source material when no host integration exists.

## Read-Only Context Search

Use a safe local search capability before a serious or saveable run when prior context could change the result.

Search for:

- similar opportunity cards
- previously rejected candidates
- existing products, services, courses, or customer workflows
- prior validation evidence

Use a narrow query built from target user, repeated workflow, pain, and product shape. Read only the most relevant results. Treat old opportunities as context, not proof of demand.

Use the search result to:

- avoid repeating a rejected idea
- mark a candidate as an update or duplicate
- identify reusable assets or reachable users
- preserve a contradiction that needs review

Do not scan an entire workspace by default and do not expose private paths in user-facing output.

## Structured Source Extraction

For long or mixed source sets, optionally use a registered semantic extraction capability before ideation. Extract only product-relevant units:

- actors and roles
- repeated scenes and workflows
- pains and costs
- decisions and handoffs
- inputs and outputs
- current workarounds
- contradictions and missing evidence

Do not require semantic extraction for short inputs.

## Saved Asset Metadata

When the user explicitly asks to save an opportunity card and the host supports confidence or typed relationships:

- score confidence for the source-supported claims, not the commercial outcome
- link the opportunity to its source with a source or derived-from relation
- record a contradiction only when two claims cannot both be true
- keep speculative candidates below the host's reliable-knowledge threshold

Use `assets/opportunity-card.template.md` as the starting point.

## Execution Boundary

Idea Spark may create candidates and saved opportunity cards. It must not place a candidate into an execution queue, start development, or claim validation success merely because the idea is interesting.

Require a `business-lens` decision of `proceed` or a clearly directed `reshape` before the host creates a development, sales, or delivery action.

If a host capability is unavailable or disabled, continue with the core workflow and state the missing context briefly.
