# Portfolio Map

This portfolio is organized around two connected but different directions:

1. Agentic AI security tooling.
2. AI-assisted trading systems with validator/backtest discipline.

The public repositories show reusable methods, contracts, and tools; private
repositories hold sensitive research state and real results.

Documentation authority and public/private storage rules are defined in
[`documentation-contract.md`](documentation-contract.md). This page is the
portfolio map; it should not redefine repository-local source-of-truth rules.

## Core Thesis

AI-assisted engineering should produce reviewable systems:

```text
bounded problem -> reproducible run -> machine-readable artifact -> review -> next test
```

The same discipline appears in both active directions:

- agentic AI systems need measurable safety, provenance, and handoff
  boundaries;
- AI-assisted trading needs validators, backtests, paper runs, and review gates
  before a model-generated setup becomes a decision.

## Project Groups

### 1. Agentic AI Security

Repositories:

- [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness)
- [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier)
- [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff)

Role:

- flagship public project;
- defensive benchmark toolkit;
- deterministic local targets;
- trace, scorecard, matrix, diff, report, and remediation artifacts;
- external model/runtime checks through explicit OpenAI-compatible endpoints.
- practical handoff files and provenance/authority transfer checks.

Why it matters:

Agentic systems move data between tools, memory, providers, files, users, and
other agents. A system prompt is not a security boundary. This project turns
those risks into safe, reproducible defensive checks.

### 2. LLM Safety Playbooks

Repository:

- [llm-safety-playbooks](https://github.com/krivonosoff161/llm-safety-playbooks)

Role:

- short practical skills for everyday LLM use;
- prompt/workflow guidance that makes boundaries explicit;
- data-vs-instruction, secret handling, generated-resource verification,
  Git/PR safety, handoff verification, and safe research scope.

Why it matters:

Not every user needs to run a benchmark. Some need a small set of repeatable
skills that reduce ambiguity before a model or coding agent acts.

### 3. AI-Assisted Trading System

Repositories:

- [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2)
- [honest-backtest](https://github.com/krivonosoff161/honest-backtest)
- private trading research workspace

Role:

- news scanner and market-context pipeline;
- strategy research lab;
- validator/backtest discipline for AI-generated setup ideas;
- private candidate registry;
- data preparation and outcome tracking;
- paper-only validation boundaries;
- future automation behind explicit gates.

Why it matters:

Trading research fails when noisy events, overfit parameters, and narrative
confidence are treated as evidence. In this line, LLM output is a proposal. The
validator/backtest layer tries to kill weak setups before they reach paper
tracking or automation.

### 4. LLM Operations

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

For the exact rule on what belongs in public Git, private repositories, local
runtime state, and archive/history docs, use
[`documentation-contract.md`](documentation-contract.md).
