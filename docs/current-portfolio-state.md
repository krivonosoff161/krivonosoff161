# Current AI Portfolio State

Status: **CURRENT**
Verified: 2026-08-29
Security public roadmap contract baseline: Harness `c1dd698`; Trading baseline remains
`4649647` / `a23588c` pending its own documentation cycle.

## Security

The federated Security ecosystem has one public machine-readable roadmap in
`agentic-security-harness`. Harness v1.3.0 is the published public core. Transfer Verifier
and AI Agent Handoff are exact-source `extension_candidate` components; Playbooks, Router
and Cheap Filter remain `standalone`; private Runtime Guard remains `contract_only` and is
not required by the public installation. None of those companion states means that a
Harness optional extra is already merged or published.

Current gate: review the exact-source installable companion stack, keep every distribution
explicit and non-auto-activating, and only then merge and separately release any optional
extras. Until those gates complete, the supported public installation is the v1.3.0 core.

- [Security Portfolio entry](security-portfolio.md)
- [Public ecosystem roadmap](https://github.com/krivonosoff161/agentic-security-harness/blob/main/docs/ecosystem-roadmap.md)

## Trading

The Trading Portfolio is a public research and paper-observation system. Its
canonical public-safe manifest belongs to `trading-bot-v2`; `honest-backtest`
independently tries to falsify candidates. A validator pass means only "not
rejected by these checks".

Current gate: the separately authorized 48-hour paper-only canary remains
unfinished. Live execution is outside the supported portfolio and requires a
separate architecture and owner decision.

- [Trading Portfolio entry](trading-portfolio.md)
- [Machine projection](trading-portfolio-public.yaml)

## Shared boundary

Both lines use AI output as advisory input. Deterministic validators, evidence
contracts, and explicit owner gates retain decision authority. No document on this
profile grants operational authority.
