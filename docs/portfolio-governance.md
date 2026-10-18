# Portfolio Governance

Status: **CURRENT**
Governance version: `2026.10.18-v8`
Verified: 2026-10-18
Authority: `none`

The machine source is [`portfolio-governance.yaml`](portfolio-governance.yaml).
This profile integrates navigation and sanitized projections; it does not own or
promote Security or Trading product claims.

## Owners

| Truth | Owner | Profile role |
|---|---|---|
| Public Security ecosystem roadmap | `agentic-security-harness` | Link to the public machine contract and generated views |
| Exact-action approval product | `agentic-action-authority` | Link to its separately owned release and bounded integration contract |
| Private Security research upstream | `agentic-runtime-guard` | Consume only sanitized component and research projections |
| Trading Portfolio | `trading-bot-v2` | Consume sanitized machine projection only |
| Skeptical Trading validation | `honest-backtest` | Preserve its bounded non-claim |
| Public navigation | `krivonosoff161` | Integrate without redefining upstream facts |

Support repositories own only their declared modules. No support library, profile
page, model review, or documentation merge can promote a portfolio status or grant
operational authority.

The [product release entries](portfolio-governance.yaml) pin the separately
verified Harness 1.14.2 and [Action Authority 0.1.1](https://pypi.org/project/agentic-action-authority/0.1.1/)
publications. Action Authority addresses approval for an exact
action and owns an optional Harness adapter that reuses the Harness 1.14.2
guarded writer. Harness is the defensive falsification and evidence lab.
Neither product claims generic containment
or the truth of external content.

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
- The preserved historical Security projection pin is Harness
  `59bbdd42a34450f372e4b54c02de21b155e008c8`; the separate current
  product release pin is in the machine governance. Open review branches cannot
  promote the historical projection.
- Digest comparison normalizes only line endings to UTF-8 LF; semantic changes must
  change the digest.

## Authority and data boundary

The portfolio documentation grants no runtime, provider, device, enforcement,
deployment, release, trading, or sealed-holdout authority. Secrets, credentials,
private evidence, raw prompts/model outputs, runtime databases/logs, and private
Trading state remain outside this repository.
