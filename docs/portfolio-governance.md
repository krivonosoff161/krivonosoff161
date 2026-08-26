# Portfolio Governance

Status: **CURRENT**
Governance version: `2026.08.23-v2`
Verified: 2026-08-23
Authority: `none`

The machine source is [`portfolio-governance.yaml`](portfolio-governance.yaml).
This profile integrates navigation and sanitized projections; it does not own or
promote Security or Trading product claims.

## Owners

| Truth | Owner | Profile role |
|---|---|---|
| Public Security ecosystem roadmap | `agentic-security-harness` | Link to the public machine contract and generated views |
| Private Security research upstream | `agentic-runtime-guard` | Consume only sanitized component and research projections |
| Trading Portfolio | `trading-bot-v2` | Consume sanitized machine projection only |
| Skeptical Trading validation | `honest-backtest` | Preserve its bounded non-claim |
| Public navigation | `krivonosoff161` | Integrate without redefining upstream facts |

Support repositories own only their declared modules. No support library, profile
page, model review, or documentation merge can promote a portfolio status or grant
operational authority.

## Instruction and document precedence

An action-specific owner instruction is evaluated together with global agent/Git
contracts and the nearest repository contract. Lower-level rules can only narrow
these boundaries. Machine manifests own cross-repository facts; repository current
documents own local facts; history and continuity files are evidence only.

## Git and publication

- Stable `main` is not an agent editing branch.
- Work uses a registered `codex/*` task worktree and explicit-path staging.
- Push and PR authority is task-scoped; merge remains a separate exact-head gate.
- Public projections pin a merged source SHA and a content digest separately.
- Digest comparison normalizes only line endings to UTF-8 LF; semantic changes must
  change the digest.

## Authority and data boundary

The portfolio documentation grants no runtime, provider, device, enforcement,
deployment, release, trading, or sealed-holdout authority. Secrets, credentials,
private evidence, raw prompts/model outputs, runtime databases/logs, and private
Trading state remain outside this repository.
