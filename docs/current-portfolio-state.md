# Current AI Portfolio State

Status: **CURRENT**
Verified: 2026-08-30
Security public roadmap contract baseline: Harness `59bbdd4`; Trading baseline remains
`4649647` / `a23588c` pending its own documentation cycle.

## Security

The federated Security ecosystem has one public machine-readable roadmap in
`agentic-security-harness`. Harness v1.4.0 and the exact companion distributions are
published on public PyPI. The `transfer`, `handoff`, `playbooks`, `router`, `filter`, and
`all` extras resolve from a clean PyPI-only environment without editable installs, local
paths, Git URLs, or a pre-existing wheelhouse. Transfer Verifier and AI
Agent Handoff are `extension_candidate` components; Playbooks and Cheap Filter remain
`standalone`; Router and private Runtime Guard remain `contract_only`. Runtime Guard is not
part of the public optional extras.

The supported public install surface now includes commands such as
`pip install "agentic-security-harness[router]==1.4.0"` and
`pip install "agentic-security-harness[all]==1.4.0"`. Installing an extra never activates
or binds it: metadata inspection, owner approval, configuration, invocation, and explicit
binding remain separate steps. Publication is installation evidence, not effectiveness,
independent review, production enforcement, or operational authority.

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
