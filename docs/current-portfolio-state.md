# Current AI Portfolio State

Status: **CURRENT**
Verified: 2026-08-29
Security public roadmap contract baseline: Harness `1c4f0f0`; Trading baseline remains
`4649647` / `a23588c` pending its own documentation cycle.

## Security

The federated Security ecosystem has one public machine-readable roadmap in
`agentic-security-harness`. Harness v1.3.0 is the published public core. Its merged source
now declares the `transfer`, `handoff`, `playbooks`, `router`, `filter`, and `all` optional
extras for exact-source or controlled-wheelhouse installation. Transfer Verifier and AI
Agent Handoff are `extension_candidate` components; Playbooks and Cheap Filter remain
`standalone`; Router and private Runtime Guard remain `contract_only`. Runtime Guard is not
part of the public optional extras.

The exact-source companion stack is merged and CI-verified, but it has not been published as
a new Harness or companion release. Therefore the supported public PyPI installation remains
the v1.3.0 core; commands such as `pip install agentic-security-harness[router]` require a
separate release/publication gate. Installing an extra never activates or binds it: metadata
inspection, owner approval, and explicit binding remain separate steps.

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
