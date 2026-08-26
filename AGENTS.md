# AI Portfolio Agent Contract

Read and follow the local operator's global agent and Git contracts when they are
available. This repository may narrow those contracts; it never weakens secret,
money, destructive-action, evidence, or owner-gate requirements.

## Repository role

- Repository: `krivonosoff161/krivonosoff161`.
- Role: public Portfolio Integrator and navigation surface.
- It does not own Security or Trading product claims.
- Public Security ecosystem roadmap and evidence truth belongs to
  `agentic-security-harness`; private Runtime Guard owns only its component and
  research evidence; Trading truth
  belongs to `trading-bot-v2`; skeptical Trading validation belongs to
  `honest-backtest`.

## Change rules

- Treat `main` as protected. Work in a registered `codex/*` task worktree.
- Update the machine-readable governance/projection first, then human views.
- Use only merged, sanitized upstream projections and separately pinned merge SHAs.
- Never infer a current claim from `SESSION.md`, `TASK.md`, a handoff, history, or
  an archived roadmap.
- Lower-level repository instructions may narrow this contract but cannot promote
  authority or redefine another repository's owned facts.
- Merge, release, deployment, enforcement, provider/device use, private-data use,
  visibility changes, and destructive Git remain separate owner gates.

## Public boundary

Do not commit secrets, credentials, `.env`, private evidence, raw prompts or model
outputs, runtime databases/logs, machine-local paths, or private Trading state.
The profile contains navigation and sanitized projections only. It grants no
operational authority.

## Required verification

Run both commands before proposing a change:

```text
python tools/validate_security_portfolio_projection.py
python tools/validate_portfolio_governance.py
```
