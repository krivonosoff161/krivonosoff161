# Portfolio Execution Map

Status: **CURRENT**

Last updated: 2026-08-01

Implementation baseline: Security `3ce7093` / `f967b90`; Trading `4649647` /
`a23588c`.

This page describes current cross-repository ownership and the next evidence
order. The machine rules are in
[`portfolio-governance.yaml`](portfolio-governance.yaml); repository-local
roadmaps retain their own facts.

## Security path

```text
agentic-security-harness fixtures/evidence
  -> canonical authority-free envelope
  -> agentic-runtime-guard trust graph and deterministic policy
  -> semantic/swarm advisories with abstention
  -> no-effect shadow decision gateway
  -> separately owner-gated receipts and bounded executor
```

Current phase: contract convergence. The immediate gate is a versioned canonical
envelope with field-loss accounting, no-authority-promotion tests, and
cross-repository shadow conformance. Semantic validation, real devices,
enforcement, deployment, and release are later independent gates.

Support ownership:

- `agentic-transfer-verifier`: provenance/authority transfer checks;
- `ai-agent-handoff`: file handoff protocol and edge pattern guard;
- `llm-safety-playbooks`: human operating guidance;
- `llm-router` and `llm-cheap-filter`: optional cost/provider support outside
  the trusted decision core.

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
