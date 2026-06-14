# Dmitry Krivonosov

I build AI-assisted research systems for agentic AI security, LLM workflow
infrastructure, and trading-research validation.

The common thread is not a single model or framework. It is a working loop:

```text
question -> bounded system -> tests -> traces -> reports -> review -> next iteration
```

I use coding agents as engineering leverage. The useful artifact is not the chat
that produced the code; it is the code, tests, schemas, reports, and failure
evidence that other people can inspect.

## Active Research Lines

| Line | Public projects | What it is for |
|---|---|---|
| Agentic AI security | [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness) | Defensive benchmark toolkit for agentic AI boundary failures, traces, scorecards, remediation, and model/runtime checks. |
| Agent handoff and data transfer | [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff), [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier) | Durable handoff files, provenance, authority boundaries, and verification of data moving between agent runtimes. |
| Trading research validation | [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2), [honest-backtest](https://github.com/krivonosoff161/honest-backtest) | News/event scanner, strategy research lab, backtest skepticism, setup validation, and private research state. |
| LLM infrastructure | [llm-router](https://github.com/krivonosoff161/llm-router), [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter) | Cost-aware routing, cheap-to-chief filtering, provider-neutral calls, and controlled LLM spend. |

## Flagship: Agentic Security Harness

[Agentic Security Harness](https://github.com/krivonosoff161/agentic-security-harness)
is the main public security project.

It is a defensive benchmark toolkit for measuring agentic AI failure modes with:

- deterministic local targets;
- portable traces and scorecards;
- scenario matrices and run diffs;
- OpenAI-compatible external model/runtime checks;
- remediation guidance;
- schema validation and local report generation.

It is not a hacking toolkit and not a promise of complete protection. It is a
measurement and learning lab for authorized, synthetic, local, or explicitly
owned targets.

## Trading Research Stack

The trading line is an applied research system, not a signal service.

Public repositories show the method:

- [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2) - local
  research workbench with scanner, market-data preparation, strategy lab, and
  paper-only validation boundaries.
- [honest-backtest](https://github.com/krivonosoff161/honest-backtest) - layered
  validation toolkit that tries to kill weak backtests before they become
  decisions.

Private repositories hold real candidate rankings, parameter libraries,
operational state, and market-specific findings. The public claim is process
quality, not trading profitability.

## Agent Handoff / Transfer Research

AI agents increasingly pass files, memory, tool output, approvals, and context
between runtimes. That handoff is often treated as plain text, but it carries
trust, provenance, and authority.

Current and planned work:

- [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff) - a
  file-based handoff protocol for AI coding agents plus a small guard hook.
- [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier) - research toolkit for verifying data
  envelopes, provenance, authority boundaries, and audit trails across
  heterogeneous agent ecosystems.

## How I Work

1. Find a real operational weakness.
2. Turn it into a bounded research question.
3. Build a deterministic harness or workflow around it.
4. Use agents for implementation and review under explicit constraints.
5. Verify with tests, schemas, reports, and adversarial review.
6. Publish reusable methods while keeping private data and credentials private.

## Public vs Private Boundary

Public:

- methods;
- test harnesses;
- synthetic examples;
- docs;
- schemas;
- sanitized reports;
- reproducible CLI flows.

Private:

- trading results and candidate rankings;
- live parameters;
- provider credentials;
- private logs;
- operational dashboards;
- raw market research state.

## Start Here

- Security benchmark: [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness)
- Trading validation: [honest-backtest](https://github.com/krivonosoff161/honest-backtest)
- Trading research workbench: [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2)
- Agent handoff protocol: [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff)
- Transfer verification: [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier)
- LLM routing: [llm-router](https://github.com/krivonosoff161/llm-router)
- LLM triage: [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter)
- Portfolio map: [docs/portfolio.md](docs/portfolio.md)
- Execution map: [docs/execution-map.md](docs/execution-map.md)

## Contact

GitHub is the best starting point. I am interested in practical AI security,
agentic workflow safety, LLM infrastructure, and research systems where
measurement matters more than hype.
