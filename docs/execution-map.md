# Portfolio Execution Map

Status: **CURRENT**

Last updated: 2026-08-29

Security public roadmap contract baseline: Harness `714f6b0`. Trading remains on its existing
`4649647` / `a23588c` baseline pending a separate documentation cycle.

This page describes current cross-repository ownership and the next evidence
order. The machine rules are in
[`portfolio-governance.yaml`](portfolio-governance.yaml); repository-local
roadmaps retain their own facts.

## Security path

The ordered Security phases, components and compatibility states are owned by the public
[Harness ecosystem roadmap](https://github.com/krivonosoff161/agentic-security-harness/blob/main/ecosystem/roadmap.yaml).
This profile does not duplicate that execution sequence. Its role is to link the generated
human view and source-owned component documentation without promoting status.

## Trading path

```text
bounded public research inputs
  -> Strategy Lab and experiment registry
  -> deterministic simulation
  -> honest-backtest falsification
  -> fenced candidate lifecycle
  -> paper-only observation and evidence
```

Current gate: complete the separately authorized 48-hour paper-only canary.
LLM output remains advisory. Live execution is outside the supported portfolio
and requires a separate architecture and owner decision.

## Shared sequencing rule

1. Update the repository that owns the fact.
2. Merge and verify its exact main SHA.
3. Produce a sanitized machine projection.
4. Pin source merge SHA and content digest separately in the profile.
5. Run local, link, schema, claim, private-boundary, and cross-platform digest
   validators.
6. Keep merge, runtime, provider, device, deployment, release, and enforcement
   as explicit owner gates.

## Public/private boundary

Public Git may contain code, schemas, documentation, deterministic synthetic
fixtures, and reviewed sanitized projections. Secrets, raw prompts/model output,
private evidence, real Trading results, strategy parameters, runtime databases,
logs, and operational state remain outside public Git.
