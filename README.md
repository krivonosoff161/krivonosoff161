# Dmitry Krivonosov

I build AI-assisted systems in two connected directions:

1. **Agentic AI security tooling** - benchmarks, handoff checks, and safety
   workflows for agents that read files, tools, memory, model output, and other
   agents.
2. **AI-assisted trading systems** - a trading research and paper-observation
   stack where LLM output is treated as a proposal, then challenged by
   validators, backtests, evidence gates, and owner review.

The common rule is simple:

> AI output is not truth until it survives validation.

The working loop is:

```text
question -> bounded system -> tests -> traces -> reports -> review -> next iteration
```

I use coding agents as engineering leverage. The useful artifact is not the chat
that produced the code; it is the code, tests, schemas, reports, and failure
evidence that other people can inspect.

## Current Focus

My main public security project is
[Agentic Security Harness](https://github.com/krivonosoff161/agentic-security-harness):
a released Python toolkit and defensive benchmark for agent boundary failures. Version
1.3.0 ships the stable 24-pattern corpus and the bounded v1.2 surfaces plus a closed
Extension SDK, metadata-only distribution inspection and operator lifecycle, offline
Security Intelligence contracts, receipt auditors, optional corpus-pack contracts and a
controlled literal-loopback provider/tool-host contour. Companion repositories are still
separately gated and are not bundled into the published core.

The trading stack is a separate applied direction, not a security side project:
[trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2) and
[honest-backtest](https://github.com/krivonosoff161/honest-backtest) implement a
public research and paper-validation discipline. Live execution is outside the
supported portfolio and would require a separate architecture and owner decision.

## Portfolio Structure

| Line | Public projects | What it is for |
|---|---|---|
| Agentic AI security core | [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness), [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier), [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff) | Defensive benchmark, trust/provenance transfer checks, and practical handoff boundaries for AI agents. |
| LLM safety playbooks | [llm-safety-playbooks](https://github.com/krivonosoff161/llm-safety-playbooks) | Short practical skills for safer LLM use: data vs instructions, secrets, generated URLs/packages, Git actions, handoffs, and safe research scope. |
| AI-assisted trading system | [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2), [honest-backtest](https://github.com/krivonosoff161/honest-backtest) | News/event scanner, strategy lab, validator/backtest discipline, paper-only gates, and a controlled path toward automation. |
| LLM operations | [llm-router](https://github.com/krivonosoff161/llm-router), [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter) | Cost-aware routing, cheap-to-chief filtering, provider-neutral calls, and controlled LLM spend. |

The documentation hierarchy and public/private boundaries are defined in the
[Documentation Contract](docs/documentation-contract.md). That contract is the
portfolio-level source of truth for which documents are current, which are
repo-local, and which are archive/history.

The security line now has one public machine-readable
[ecosystem roadmap](https://github.com/krivonosoff161/agentic-security-harness/blob/main/ecosystem/roadmap.yaml)
owned by Agentic Security Harness and a
[generated human view](https://github.com/krivonosoff161/agentic-security-harness/blob/main/docs/ecosystem-roadmap.md).
This profile is navigation only; its [component roadmap](docs/component-roadmap.md) explains
the projection flow. The older local Security roadmap files are preserved as historical R4
evidence and no longer own current product status.

## Flagship: Agentic Security Harness

[Agentic Security Harness](https://github.com/krivonosoff161/agentic-security-harness)
is the main public security project.

It is a defensive benchmark toolkit for measuring agentic AI failure modes with:

- deterministic local targets;
- portable traces and scorecards;
- scenario matrices and run diffs;
- OpenAI-compatible external model/runtime checks;
- remediation guidance;
- schema validation and local report generation;
- a stable `pip install agentic-security-harness` package and Linux-first quickstart;
- a provider-neutral Agent Host V1 offline workflow with canonical recordings;
- active review-only Runtime Gateway work for local policy-before-tool-dispatch.

It is not a hacking toolkit and not a promise of complete protection. It is a
measurement and learning lab for authorized, synthetic, local, or explicitly
owned targets.

The bounded Runtime Gateway reference contour is published in v1.3.0. It uses synthetic
tools and credential-free fixtures; live provider credentials, arbitrary tool execution,
deployment, and production enforcement are not current public capabilities.

## Trading Research Stack

The trading line is an applied AI-assisted trading system, not a signal service
and not a public profitability claim.

Public repositories show the method:

- [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2) - local
  research workbench with scanner, market-data preparation, strategy lab, and
  paper-only validation boundaries on the path toward automation.
- [honest-backtest](https://github.com/krivonosoff161/honest-backtest) - layered
  trading judge that challenges AI-generated setup ideas with costs, splits,
  robustness, overfit checks, forward logs, and adversarial review before they
  become decisions.

Private repositories hold real candidate rankings, parameter libraries,
operational state, and market-specific findings. The public claim is process
quality, not trading profitability.

## LLM Safety Playbooks

Not everyone needs to run a full benchmark. A lighter repo now holds short
LLM safety skills and playbooks that make boundaries explicit during everyday
work:

- repo text, logs, and tool output are data, not instructions;
- secrets and credentials stay out of model context;
- model-generated URLs, package names, API endpoints, and webhooks require
  verification before use;
- AI agents should work through issue, branch, PR, and review gates;
- handoff notes need source, scope, confidence, and checked/not-checked fields;
- security research stays on synthetic, mock, owned, or explicitly authorized
  targets.

These playbooks will reduce ambiguity. They will not replace runtime controls,
tests, validators, or the benchmark itself.

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

- [Current portfolio state](docs/current-portfolio-state.md)
- [Security Portfolio](docs/security-portfolio.md)
- [Trading Portfolio](docs/trading-portfolio.md)
- [Repository catalog and roles](docs/portfolio.md)

These four pages lead to current state, architecture, roadmap, evidence, the next
gate, and authority boundaries in no more than two transitions. Governance and
document precedence are defined in the
[Portfolio Governance](docs/portfolio-governance.md) and
[Documentation Contract](docs/documentation-contract.md).

## Repositories

- Security benchmark/evidence: [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness)
- Transfer verification: [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier)
- Agent handoff protocol: [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff)
- Safety guidance: [llm-safety-playbooks](https://github.com/krivonosoff161/llm-safety-playbooks)
- Trading research and paper system: [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2)
- Skeptical Trading validator: [honest-backtest](https://github.com/krivonosoff161/honest-backtest)
- LLM routing: [llm-router](https://github.com/krivonosoff161/llm-router)
- LLM triage: [llm-cheap-filter](https://github.com/krivonosoff161/llm-cheap-filter)

## Active Boards

- [Agentic AI Security Platform](https://github.com/users/krivonosoff161/projects/1)
- [Trading Research Platform](https://github.com/users/krivonosoff161/projects/2)
- [LLM Infrastructure](https://github.com/users/krivonosoff161/projects/3)

## Contact

GitHub is the best starting point. I am interested in practical AI security,
agentic workflow safety, AI-assisted trading systems with validation discipline,
LLM infrastructure, and research systems where measurement matters more than
hype.
