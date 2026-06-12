# Portfolio Map

This portfolio is organized around one idea: AI-assisted engineering should
produce systems, evidence, and reviewable artifacts, not just chat output.

For the active cross-repository work queue, see
[Portfolio Execution Map](execution-map.md).

## Project Groups

### 1. Agentic AI Security

Repository:

- [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness)

Role:

- flagship public project;
- defensive security benchmark;
- synthetic local targets only;
- portable traces and scorecards;
- data-boundary and recipient-control focus.

Why it matters:

Agentic systems increasingly move data between tools, memory, providers,
applications, and users. A system prompt is not a security boundary. The project
turns those risks into safe, reproducible defensive tests.

### 2. Trading Research Infrastructure

Repository state:

- private applied system;
- selected methods extracted into public repositories.

Role:

- news scanner;
- cheap-to-chief LLM review;
- outcome audit;
- strategy research lab;
- private candidate registry.

Why it matters:

Trading research fails when noisy signals, overfit backtests, and narrative
confidence are treated as evidence. The system is designed to log, reject, and
validate ideas before they become decisions.

### 3. Backtest Validation

Repository:

- [honest-backtest](https://github.com/krivonosoff161/honest-backtest)

Role:

- synthetic examples;
- validation layers;
- anti-overfitting framing;
- forward-log discipline.

Why it matters:

Most bad strategies can be killed cheaply before real money or live systems are
involved.

### 4. LLM Infrastructure

Repositories:

- [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter)
- [llm-router](https://github.com/krivonosoff161/llm-router)

Role:

- cost-aware model routing;
- cheap-to-chief escalation;
- provider-neutral calls;
- usage and cost logging.

Why it matters:

In agentic systems, using the best model for every step is usually wasteful.
Most work should be filtered, summarized, or classified cheaply before an
expensive model is asked to decide.

### 5. Agent Workflow Safety

Repository:

- [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff)

Role:

- file-based agent handoff protocol;
- reduced context replay;
- PreToolUse safety guard;
- simple agent coordination pattern.

Why it matters:

Agentic coding workflows need memory, accountability, and guardrails. Chat
history alone is not a reliable operating surface.

## Public vs Private Boundary

Public:

- methods;
- harnesses;
- examples;
- tests;
- documentation;
- sanitized reports.

Private:

- trading results;
- live parameters;
- credentials;
- raw private logs;
- candidate strategies;
- operational dashboards.

This split is intentional. The public work shows process quality; the private
work holds sensitive research state.
