# Portfolio Execution Map

Status: active working map  
Last updated: 2026-06-12  
Scope: public repositories, private research boundary, and next execution order.

This map turns the repository set into one portfolio instead of several
unrelated tools.

## Core Thesis

The portfolio is about engineering discipline for agentic systems:

```text
route cheaply -> filter deterministically -> coordinate agents safely
-> validate without self-deception -> measure failure modes
```

The public repositories show reusable methods. Private repositories hold live
trading results, candidate parameters, data snapshots, and operational state.

## Portfolio Layers

| Layer | Repository | Role | Public claim |
|---|---|---|---|
| Agentic security | `agentic-security-harness` | Flagship defensive benchmark | Deterministic replay and measurement of agentic AI failure modes |
| Trading validation | `honest-backtest` | Backtest skepticism layer | Kill weak strategies before they become decisions |
| Trading system | `trading-bot-v2` plus private research state | Applied research pipeline | Pattern-level architecture, not private alpha or parameters |
| Cost control | `llm-cheap-filter` | Cheap-to-chief triage | Spend expensive model calls only where they matter |
| Model access | `llm-router` | Thin role-tiered LLM router | Small auditable LLM call layer with cost logging |
| Agent workflow | `ai-agent-handoff` | Cross-agent handoff and guard | Durable agent coordination without replaying full chat history |

## Public vs Private Boundary

Public:

- architecture and process;
- sanitized examples;
- deterministic tests;
- safe benchmark patterns;
- documentation;
- validation reports with no private edge.

Private:

- real trading outcomes and candidate rankings;
- strategy parameters and calibration results;
- raw private logs;
- API keys, credentials, and provider bills;
- operational dashboards and live research state.

## Execution Order

### P0 - Portfolio Hygiene

Goal: make the GitHub profile and pinned repositories coherent.

Tasks:

- keep the profile README as the portfolio entry point;
- keep each repository description aligned with its real scope;
- add topics and releases only after each repo has a stable first-screen story;
- avoid profitability, complete-security, or uniqueness claims;
- keep private results out of public repositories.

Exit criteria:

- each pinned repository answers "what is this, why now, what is not claimed"
  in the first screen;
- profile links form a clear path through the portfolio.

### P1 - Agentic Security Harness

Goal: make the flagship repository read as a serious defensive benchmark.

Positioning:

- not a live exploit tool;
- not a general red-team scanner;
- deterministic local benchmark for data-boundary, label-propagation, memory,
  tool, provider, and handoff failures.

Next tasks:

- verify external references before changing public docs;
- update prior-art docs with a careful distinction between scanners, runtime
  defenses, benchmarks, and conformance-style tests;
- add machine-readable mapping fields for standards only after verification;
- expand corpus around data-envelope survival and label propagation;
- keep all tests local, synthetic, and safe.

Exit criteria:

- README, corpus docs, competitors docs, and roadmap agree on the same
  positioning;
- benchmark claims are measurable through local `ash` commands;
- no public doc implies complete protection or live offensive use.

### P2 - Honest Backtest

Goal: turn the project from a useful validation checklist into a credible
anti-overfit library.

Next tasks:

- add named statistical tests where appropriate;
- document assumptions plainly;
- keep examples synthetic and deterministic;
- connect forward-ledger discipline to the private Strategy Lab workflow.

Exit criteria:

- a reviewer can see how the project differs from a normal backtest engine;
- validation results reject weak ideas instead of blessing profitable-looking
  runs.

### P3 - Trading Research System

Goal: keep the public architecture useful while preserving private edge.

Public work:

- document the pattern-level scanner pipeline;
- document the strategy-lab process without publishing private candidate
  results;
- cross-link to `honest-backtest` as the validation layer;
- keep source onboarding and LLM cost-control decisions auditable.

Private work:

- store research outputs under the private research root;
- keep candidate registries, Obsidian graphs, SQLite state, and reports private;
- publish only sanitized examples and process descriptions.

Exit criteria:

- public readers understand the machine;
- private results remain private;
- scanner, Strategy Lab, and validation layers have a clear operating boundary.

### P4 - LLM Cheap Filter

Goal: make cost triage measurable, not just plausible.

Next tasks:

- add calibration and replay tooling;
- add a savings report artifact;
- document false-accept and false-escalate rates as first-class concepts;
- compare honestly with adjacent cascade and routing projects.

Exit criteria:

- users can tune thresholds against their own data;
- the library reports what it saved and what risk it introduced.

### P5 - LLM Router

Goal: keep the router small, auditable, and useful as infrastructure.

Next tasks:

- add budget caps and warnings;
- add role-level spending summaries;
- document when to use this instead of a full gateway;
- defer streaming/tools until the small core remains stable.

Exit criteria:

- the router remains easy to audit;
- cost behavior is observable;
- role tiers are the main conceptual primitive.

### P6 - AI Agent Handoff

Goal: align with emerging agent-file conventions without losing the
cross-agent workflow.

Next tasks:

- make templates compatible with common agent instruction files;
- explain that the guard is not a sandbox;
- add rule packs only if they remain simple and testable;
- document full agent handoff round trips.

Exit criteria:

- the repository reads as a protocol plus guard, not just another hook list;
- the safety boundary is honest.

## Verification Queue

Claims from market research must be verified before public documentation uses
them as facts.

Required verification:

- current status of major agentic-security benchmarks and runtime defenses;
- current OWASP, MITRE ATLAS, and NIST mappings;
- acquisition or ownership changes;
- active status, stars, releases, and licenses of named adjacent projects;
- pricing or usage claims, if mentioned at all.

Rule:

If a fact can change, verify it from primary sources or mark it as unverified.

## Operating Rule

Work one repository at a time.

For each repository:

1. Read current README, docs, code, tests, and GitHub-facing metadata.
2. Check the execution-map task for that repository.
3. Make a small coherent change.
4. Run tests and lint appropriate to that repo.
5. Commit only that repository's work.
6. Push only after the commit is clean.

This prevents portfolio work from turning into cross-repository drift.
