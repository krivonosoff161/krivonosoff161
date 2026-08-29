# Repository Catalog and Roles

Status: **CURRENT**

Verified: 2026-08-29

This is a catalog, not a second product roadmap. Current state is in
[`current-portfolio-state.md`](current-portfolio-state.md), and ownership rules
are in [`portfolio-governance.md`](portfolio-governance.md).

## Security Portfolio

| Repository | Integration status | Owned role | Authority ceiling |
|---|---|---|---|
| `agentic-runtime-guard` (private) | `contract_only` | Private defensive research upstream and bounded shadow/runtime research | No public roadmap, production or operational authority |
| [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness) | `suite_verified` | Public ecosystem core, roadmap, defensive benchmark and synthetic integration laboratory | No certification or production enforcement |
| [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier) | `extension_candidate` | Transfer provenance, freshness, capability, and authority checks | Advisory module only |
| [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff) | `extension_candidate` | Practical file handoff protocol and pattern guard | Guard, not sandbox or verifier |
| [llm-safety-playbooks](https://github.com/krivonosoff161/llm-safety-playbooks) | `standalone` | Human operating guidance | Guidance, not enforcement |

## Trading Portfolio

| Repository | Owned role | Authority ceiling |
|---|---|---|
| [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2) | Canonical public-safe Trading roadmap, research orchestration, deterministic simulation, and paper observation | Paper-only contours require separate owner authority; no live execution |
| [honest-backtest](https://github.com/krivonosoff161/honest-backtest) | Skeptical deterministic validation | A pass means only "not rejected" |

## Shared support

| Repository | Integration status | Owned role | Authority ceiling |
|---|---|---|---|
| [llm-router](https://github.com/krivonosoff161/llm-router) | `contract_only` | Provider-neutral routing and usage/cost arithmetic | Not a policy gateway or secret manager |
| [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter) | `standalone` | Deterministic and cheap-to-chief triage | Cannot lower a guard decision or establish correctness |
| [krivonosoff161](https://github.com/krivonosoff161/krivonosoff161) | `standalone` | Public navigation and sanitized integration | Projection only; owns no upstream product claim |

Integration status is projected from the merged Harness compatibility contract. It is not
an installation, release or authority claim.

## Reading order

- [Current portfolio state](current-portfolio-state.md)
- [Security Portfolio](security-portfolio.md)
- [Trading Portfolio](trading-portfolio.md)
- [Execution map](execution-map.md)
- [Portfolio Governance](portfolio-governance.md)
- [Documentation Contract](documentation-contract.md)
