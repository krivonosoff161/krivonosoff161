# Dmitry Krivonosov

I build AI-assisted research systems for agentic security, LLM workflow
automation, and trading research validation.

My work is not centered on one model, one provider, or one framework. The
pattern is broader:

```text
problem framing -> agent-assisted implementation -> tests -> audits -> traces -> reports
```

I use coding agents as engineering leverage, not as a substitute for judgment:
I define the problem, constraints, architecture, review criteria, and research
direction; agents help implement, test, compare, and audit the work.

## Current Focus

- Agentic AI security: data boundaries, recipient control, tool permissions,
  memory poisoning, replayable traces, and defensive benchmarks.
- LLM workflow systems: cheap-to-chief routing, provider abstraction, model cost
  control, and handoff protocols for multi-agent coding.
- Trading research infrastructure: news scanning, market-context pipelines,
  strategy discovery, validation discipline, and private result registries.
- Research process design: turn vague ideas into reproducible experiments,
  measurable artifacts, and reviewable code.

## Flagship Project

### [Agentic Security Harness](https://github.com/krivonosoff161/agentic-security-harness)

A trace-first defensive benchmark for agentic AI failure modes.

It reproduces how LLM agents, tool chains, memory, and data boundaries fail in
local synthetic targets, then captures each run as a portable trace and
scorecard.

What it demonstrates:

- agentic data-boundary and recipient-control tests;
- vulnerable vs protected replay;
- deterministic local targets;
- validation of benchmark artifacts;
- safe research framing: no live exploitation, no real secrets, no third-party
  abuse.

This is the public security-research core of the portfolio.

## Applied Research System

### Trading research and scanner infrastructure

The main trading system is a private applied research project. Public
repositories show selected methods and tools, while real data, candidate
results, parameters, and strategy conclusions stay private.

The system explores:

- news ingestion and machine-readable event extraction;
- cheap-model filtering before expensive model review;
- outcome logging and no-go audits;
- strategy research queues;
- validation before any forward/paper/live use;
- private candidate registries and review packs.

The public claim is process quality, not trading profitability.

## Supporting Projects

| Project | What it shows |
|---|---|
| [honest-backtest](https://github.com/krivonosoff161/honest-backtest) | A layered validation architecture for killing weak trading ideas before they cost money. |
| [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter) | A zero-dependency cheap-to-chief triage pipeline for reducing LLM cost and noise. |
| [llm-router](https://github.com/krivonosoff161/llm-router) | A small async router for role-tiered LLM calls across OpenAI-compatible providers and Yandex AI Studio. |
| [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff) | A file-based handoff protocol for AI coding agents, plus a safety guard for sensitive paths and commands. |

## How I Work

I work as an AI-assisted systems builder:

1. Find a real operational weakness.
2. Convert it into a testable research question.
3. Build a small deterministic harness around it.
4. Let agents implement and review under explicit constraints.
5. Verify with tests, reports, and adversarial review.
6. Keep private results private and publish reusable methods.

The important part is not that an agent wrote code. The important part is that
the process produces artifacts other people can inspect:

- tests;
- traces;
- scorecards;
- examples;
- documentation;
- failure reports;
- conservative claims.

## What I Do Not Claim

- I do not claim that a benchmark proves complete security.
- I do not claim that a backtest proves a profitable strategy.
- I do not publish private trading results or production credentials.
- I do not present offensive security work as a product.

The public repositories are method-first. The private systems hold the live
research state and results.

## Useful Starting Points

- Security benchmark: [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness)
- Backtest validation: [honest-backtest](https://github.com/krivonosoff161/honest-backtest)
- LLM triage: [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter)
- LLM routing: [llm-router](https://github.com/krivonosoff161/llm-router)
- Agent workflow safety: [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff)

## Contact

GitHub is the best place to start. I am interested in practical AI security,
agentic workflow safety, LLM infrastructure, and research systems where
measurement matters more than hype.
