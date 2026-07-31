# Documentation Contract

Status: active portfolio contract
Last updated: 2026-07-05

This document defines how the repositories in this GitHub profile should be
read, updated, and connected. It exists to prevent the portfolio from becoming a
set of unrelated README files, old handoff notes, private calculations, and
duplicated safety disclaimers.

## Core Rule

Each repository may have many documents, but only a small number of documents
are allowed to be treated as source of truth.

```text
profile README
  -> portfolio execution map
  -> documentation contract
  -> repository README
  -> repository project map / current state / runbook / storage boundary
  -> research, examples, history, and archives
```

When documents disagree, use this order unless a repository-specific maintainer
document explicitly narrows it.

## Portfolio-Level Documents

| Document | Authority |
|---|---|
| [`README.md`](../README.md) | Public front door. Explains who I am, what the portfolio is, and where to start. |
| [`docs/execution-map.md`](execution-map.md) | Portfolio ownership map. Explains which repo owns which layer and what order work should follow. |
| `docs/documentation-contract.md` | Documentation governance. Explains which documents are canonical, which are local, and which are archive/history. |

The profile repository is the only place that should define the whole GitHub
portfolio. Individual repos may explain their role, but they should not redefine
the whole system differently.

## Repository Document Roles

Every active repository should fit this shape.

| Role | Typical file | Purpose |
|---|---|---|
| Front door | `README.md` | What this repo is, who it is for, how to try it, and what it does not claim. |
| Maintainer map | `docs/project-map.md` or equivalent | What exists inside the repo and where reviewers should look. |
| Current state | `docs/current-state.md`, `CURRENT_STATE.md`, or equivalent | What is shipped or active now. This should not become a long historical diary. |
| Architecture | `docs/architecture.md`, `ARCHITECTURE.md`, or equivalent | Stable system structure and boundaries. |
| Operator path | `docs/runbook.md`, `docs/farm_runbook.md`, or equivalent | Commands, preflight checks, stop/restart rules, and expected outputs. |
| Storage boundary | `docs/storage-boundaries.md`, `docs/private-public-evidence-boundary.md`, or equivalent | What may be committed, what stays private, and how sanitized evidence is published. |
| Research model | `docs/*model*.md`, `docs/*campaign*.md`, examples | Evidence, methodology, synthetic examples, and claim limits. |
| History/archive | `docs/history/`, `docs/archive/`, dated reports | Old decisions and audit trail. Useful, but not current truth unless promoted. |
| Handoff/session | `TASK.md`, `SESSION.md`, `docs/session_handoff_*.md` | Agent working memory. It must not override current-state or architecture docs. |

## Active Repository Roles

| Repository | Portfolio role | Documentation source of truth |
|---|---|---|
| `agentic-security-harness` | Security flagship and benchmark/evidence layer | README, current state, project map, research problem map, evidence boundary |
| `agentic-runtime-guard` (private) | Product-composition and shadow/advisory runtime research | Russian README, architecture, threat model, evidence contract, product roadmap, portfolio map |
| `agentic-transfer-verifier` | Trust/provenance transfer research | README, formal/risk/leakage model docs |
| `ai-agent-handoff` | Practical handoff protocol and local guard | README, protocol, trust-boundaries, project map |
| `llm-safety-playbooks` | Lightweight practical safety playbooks | README, coverage map, playbooks |
| `trading-bot-v2` | Public trading research workbench and paper/research system | README, current state, architecture, farm runbook, storage boundaries |
| `honest-backtest` | Trading validation layer | README, project map, overfitting/statistics docs |
| `llm-router` | Small LLM call/router support layer | README, operating model, project map |
| `llm-cheap-filter` | Cheap-to-chief triage support layer | README, calibration/replay, project map |
| `trading-bot-research` | Private research/evidence repository | README and private boundary docs only; not a public portfolio entry point |
| `1` / `simple trading bot okx` | Private old/archive trading codebase | Historical reference only; not a current architecture source |

`new-boot` and `desktop-tutorial` are not part of the current public research
architecture unless they are explicitly reactivated later.

## Public vs Private Boundary

Public repositories may contain:

- source code;
- documentation;
- synthetic examples;
- schemas;
- small deterministic fixtures;
- deterministic synthetic traces and redacted artifacts that are intentionally
  committed as public evidence;
- sanitized screenshots or reports;
- public-safe aggregate evidence;
- commands that reproduce public examples without private systems.

Public repositories must not contain:

- real trading strategy calculations or private edge;
- candidate rankings, live parameters, or calibration results;
- private paper/live trade rows with routing details;
- raw market research state;
- `.env` files, API keys, provider credentials, Telegram tokens, or exchange
  secrets;
- raw model prompts, responses, transcripts, canaries, or private attack notes;
- private/local/provider traces and owned-system evidence before sanitization;
- local dashboards, SQLite state, logs, caches, or generated farm output;
- private provider bills or operational account details.

Approved exceptions must be synthetic or explicitly sanitized. A public example
may demonstrate the shape of a calculation, but not the private trading result
or strategy edge behind it.

## Trading Research Rule

Trading research has three layers:

```text
public method and architecture
  -> private research/evidence records
  -> local runtime state and raw calculations
```

Only the first layer belongs in public repositories.

`trading-bot-v2` may explain the workbench, paper/research boundaries, and
validated process. `honest-backtest` may explain validation methods on synthetic
data. `trading-bot-research` may hold private research code and findings when
they are safe for that private repository. Raw runtime state and large generated
artifacts stay outside Git.

## Security Research Rule

Security research must stay defensive, synthetic, owned, or explicitly
authorized.

Public security artifacts may show:

- boundary invariants;
- synthetic target behavior;
- aggregate counts;
- hashes and schema-validated summaries;
- sanitized evidence packs;
- non-claims and residual risk.

Raw prompts, raw model responses, private traces, canary values, and local
calculation notes stay private unless a later review explicitly promotes a
sanitized derivative.

## Update Rules

When changing documentation:

1. Decide which document role is being changed.
2. Update the highest authority document that owns that fact.
3. Link lower-level documents to it instead of duplicating the same rule.
4. Move dated or historical material to history/archive instead of deleting it
   when it still explains a decision.
5. Keep public claims conservative: no profitability, no complete protection,
   no certification, no provider endorsement, no live-trading implication.
6. Re-run a link/private-boundary audit after broad documentation changes.

## Review Checklist

Before accepting a broad documentation change, check:

- Does each repo still have one clear front door?
- Is the current source of truth obvious?
- Are archive/history docs marked as archive/history?
- Are support repos described as support layers, not new flagships?
- Are private trading calculations still outside public Git?
- Are raw model responses, canaries, traces, and private security calculations
  still outside public Git?
- Do cross-repo links point to the profile contract instead of re-explaining the
  entire portfolio differently?
- Do all non-claims remain intact?

## Intended Outcome

A reader should be able to answer:

1. What is the portfolio?
2. Which repositories are the main systems?
3. Which repositories are supporting libraries?
4. Where is the current architecture?
5. Where are operator commands?
6. What is public and what is private?
7. Which docs are current, and which are history?

If the answer requires reading every Markdown file in every repository, the
documentation contract has failed.
