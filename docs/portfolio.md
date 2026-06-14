# Portfolio Map

This portfolio is organized around practical research systems. The public
repositories show reusable methods, contracts, and tools; private repositories
hold sensitive research state and real results.

## Core Thesis

AI-assisted engineering should produce reviewable systems:

```text
bounded problem -> reproducible run -> machine-readable artifact -> review -> next test
```

The same discipline appears in both active directions:

- agentic AI systems need measurable safety and handoff boundaries;
- trading research needs validation before any setup becomes a decision.

## Project Groups

### 1. Agentic AI Security

Repository:

- [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness)

Role:

- flagship public project;
- defensive benchmark toolkit;
- deterministic local targets;
- trace, scorecard, matrix, diff, report, and remediation artifacts;
- external model/runtime checks through explicit OpenAI-compatible endpoints.

Why it matters:

Agentic systems move data between tools, memory, providers, files, users, and
other agents. A system prompt is not a security boundary. This project turns
those risks into safe, reproducible defensive checks.

### 2. Agent Handoff and Transfer Verification

Repositories:

- [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff)
- [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier)

Role:

- file-based handoff protocol for AI coding agents;
- guard hook for sensitive paths and commands;
- verifier for data envelopes, provenance, trust levels, approvals,
  audit trails, and cross-runtime handoff semantics.

Why it matters:

Agent ecosystems increasingly pass context and authority through plain files,
tool results, chat summaries, memory entries, and model-generated plans. The
research question is whether those handoffs can be validated instead of merely
trusted.

### 3. Trading Research Infrastructure

Repositories:

- [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2)
- private [trading-bot-research](https://github.com/krivonosoff161/trading-bot-research)

Role:

- news scanner and market-context pipeline;
- strategy research lab;
- private candidate registry;
- data preparation and outcome tracking;
- future execution integration behind explicit gates.

Why it matters:

Trading research fails when noisy events, overfit parameters, and narrative
confidence are treated as evidence. The public repository shows the machinery;
the private repository stores real candidate results and parameters.

### 4. Backtest Validation

Repository:

- [honest-backtest](https://github.com/krivonosoff161/honest-backtest)

Role:

- layered validation toolkit;
- synthetic examples;
- costs, splits, robustness, overfit statistics, forward logs, and adversarial
  review;
- intended validation layer for Strategy Lab candidates.

Why it matters:

Most weak trading ideas can be killed before they reach paper-forward tracking
or any execution system.

### 5. LLM Infrastructure

Repositories:

- [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter)
- [llm-router](https://github.com/krivonosoff161/llm-router)

Role:

- cost-aware model routing;
- cheap-to-chief escalation;
- provider-neutral calls;
- usage and cost logging.

Why it matters:

In agentic systems, expensive models should be used for the decisions that
actually need them. Cheap deterministic filters and role-tiered routing keep
costs visible.

## Public vs Private Boundary

Public:

- methods;
- harnesses;
- examples;
- tests;
- schemas;
- documentation;
- sanitized reports.

Private:

- trading results;
- live parameters;
- credentials;
- raw private logs;
- candidate strategy rankings;
- operational dashboards.

This split is intentional. The public work shows process quality; the private
work holds sensitive research state.
