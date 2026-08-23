# Current AI Portfolio State

Status: **CURRENT**
Verified: 2026-08-23
Security public roadmap contract baseline: Harness `28865fc`; Trading baseline remains
`4649647` / `a23588c` pending its own documentation cycle.

## Security

The federated Security ecosystem has one public machine-readable roadmap in
`agentic-security-harness`. Released Harness is the public core; the other public
repositories are currently standalone or contract-only components, not yet installable
Harness extensions. Private Runtime Guard is a research upstream and is not required by the
public installation.

Current gate: complete documentation convergence, then implement the Extension SDK and
cross-repository compatibility contracts before claiming installable extensions.

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
