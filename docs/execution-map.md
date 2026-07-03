# Portfolio Execution Map

Status: active working map
Last updated: 2026-07-03
Scope: public repositories, private research boundary, and next execution order.

This map keeps the repository set coherent. The goal is not a collection of
unrelated Python repositories. It is a public profile with two connected but
different directions:

1. Agentic AI security tooling.
2. AI-assisted trading systems with validation discipline and a
   paper-to-automation path.

## Portfolio Layers

| Layer | Repository | Role | Public claim |
|---|---|---|---|
| Agentic security core | `agentic-security-harness` | Flagship defensive benchmark | Deterministic evaluation of agentic AI boundary failures |
| Transfer verification | `agentic-transfer-verifier` | Trust/provenance research line | Validate data, context, provenance, and authority across agent runtimes |
| Agent workflow | `ai-agent-handoff` | Practical protocol + guard | Durable handoff files and simple guardrails for AI coding agents |
| LLM safety playbooks | `llm-safety-playbooks` | Lightweight practical skills | Help users make LLM boundaries explicit without running the full benchmark |
| AI-assisted trading system | `trading-bot-v2` | Applied trading workbench | Scanner, Strategy Lab, paper boundaries, and automation path |
| Trading validator | `honest-backtest` | Backtest and setup judge | Challenge AI-generated trading ideas before they become decisions |
| Cost control | `llm-cheap-filter` | Cheap-to-chief triage | Spend expensive model calls only where they matter |
| Model access | `llm-router` | Thin role-tiered LLM router | Small auditable LLM call layer with cost logging |

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

### P0 - GitHub Portfolio Hygiene

Goal: make the GitHub profile and main repositories read as a coherent research
portfolio.

Tasks:

- keep the profile README as the entry point;
- keep each repository description aligned with its real scope;
- add topics and releases only after each repo has a stable first-screen story;
- avoid profitability, complete-security, or uniqueness claims;
- keep private results out of public repositories.

Exit criteria:

- each pinned repository answers "what is this, why now, what is not claimed";
- profile links form a clear path through the portfolio;
- supporting libraries do not distract from the two main research lines.

### P1 - Agentic Security Harness

Goal: make the flagship repository read as a serious independent benchmark
toolkit.

Current position:

- local deterministic targets;
- external OpenAI-compatible checks;
- schema validation;
- run diffs;
- HTML reports;
- local run DB;
- Docker/PyPI readiness docs.

Next tasks:

- preserve the v1.0-readiness path;
- keep schema compatibility explicit;
- add showcase-level examples and docs only after validation;
- avoid implying complete security or real-world exploit capability.

Exit criteria:

- new users can install, run, validate, report, and diff without private context;
- benchmark claims are measurable through local `ash` commands.

### P2 - LLM Safety Playbooks

Goal: grow a lightweight practical repo that turns recurring agentic safety
lessons into short skills and playbooks.

Scope:

- data vs instruction boundaries;
- secret and credential handling;
- model-generated URL/package/API endpoint verification;
- issue/branch/PR safety for coding agents;
- handoff verification fields;
- safe research scope for synthetic, mock, owned, or explicitly authorized
  targets.

Non-scope:

- no claim that prompts alone provide security;
- no replacement for runtime controls, validators, tests, or the benchmark;
- no live exploit instructions;
- no provider abuse.

Exit criteria for first slice:

- repository exists;
- README explains the limitation clearly;
- 5-6 short skills exist as Markdown files;
- each skill has purpose, when to use, boundaries, and example wording;
- profile links it as a practical entry point, not a completed security system.

### P3 - Agentic Transfer Verifier

Goal: create a new research toolkit for validating data handoffs between
heterogeneous AI agent ecosystems.

Scope:

- data envelopes;
- provenance;
- trust levels;
- authority boundaries;
- approval binding;
- stale/replayed context;
- audit trail integrity;
- cross-runtime handoff semantics.

Non-scope:

- no live exploitation;
- no third-party abuse;
- no vendor-specific credential handling;
- no claim of universal standardization.

Exit criteria for first slice:

- problem statement;
- boundary model;
- simple envelope schema;
- synthetic local examples;
- tests for provenance and integrity checks;
- clear link to `agentic-security-harness` and `ai-agent-handoff`.

### P4 - AI-Assisted Trading System

Goal: keep the public architecture useful while preserving private edge and
make the validator/backtest role explicit.

Current public work:

- news/event scanner;
- Strategy Lab;
- data preparation;
- candidate registry boundary;
- no-live-trading docs.

Next tasks:

- integrate Strategy Lab with `honest-backtest`;
- turn lite candidates into hard-validation requests;
- build private setup library cards;
- keep LLM output classified as proposal, not decision;
- keep real results private.

Exit criteria:

- public readers understand the machine;
- private results remain private;
- scanner, Strategy Lab, and validation layers have a clear operating boundary.

### P5 - Honest Backtest

Goal: make the project the validation layer for Strategy Lab candidates and a
standalone anti-overfit toolkit.

Next tasks:

- expose stable callable validation APIs;
- document how Strategy Lab hands candidates to it;
- keep examples synthetic and deterministic;
- keep the language "kill bad ideas cheaply", not "certify strategies".

Exit criteria:

- a reviewer can see how it differs from a normal backtest engine;
- Strategy Lab can call it without shell scraping.

### P6 - Agent Handoff

Goal: align the project with the transfer-verification research line without
turning it into a large framework.

Next tasks:

- make the protocol relationship to `agentic-transfer-verifier` explicit;
- keep the guard honest: guard, not sandbox;
- add examples only where they prove a handoff property.

Exit criteria:

- the repository reads as a practical protocol plus guard;
- deeper verification work lives in the new transfer project.

### P7 - LLM Infrastructure

Goal: keep `llm-router` and `llm-cheap-filter` small, useful supporting
libraries.

Next tasks:

- document when to use each;
- keep cost behavior observable;
- avoid over-positioning them as main portfolio projects.

Exit criteria:

- they support the main systems without pulling attention from them.

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
