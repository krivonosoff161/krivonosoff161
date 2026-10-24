# Dmitry Krivonosov

I build AI-assisted systems with a current focus on agentic AI security:

1. **Agentic AI security tooling** - benchmarks, handoff checks, and safety
   workflows for agents that read files, tools, memory, model output, and other
   agents.
2. **Other projects** - an AI-assisted trading research and paper-observation
   stack, with development paused pending hardware.

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

[Agentic Action Authority](https://github.com/krivonosoff161/agentic-action-authority)
lets an application require an operator's signed approval for one exact document
action. Its [0.3.0 package is on PyPI](https://pypi.org/project/agentic-action-authority/0.3.0/),
with [verified production release checks](https://github.com/krivonosoff161/agentic-action-authority/actions/runs/40075923312).
The approval core installs independently; the optional Harness adapter creates
the approved file through Harness's existing guarded writer.

[Agentic Security Harness](https://github.com/krivonosoff161/agentic-security-harness)
is the defensive testing and evidence lab: reproduce agent boundary failures,
compare controls, and inspect the result. Its current published version is 1.14.2.

These tools address bounded action and workflow controls, not arbitrary-agent
containment or content truth. [Current release evidence and boundaries](docs/current-portfolio-state.md)
link the exact sources and checks for each product.

Under Other projects, the trading stack remains a separate applied direction:
[trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2) and
[honest-backtest](https://github.com/krivonosoff161/honest-backtest) implement a
public research and paper-validation discipline. Development is paused pending
hardware. Live execution is outside the
supported portfolio and would require a separate architecture and owner decision.

## Portfolio Structure

| Line | Public projects | What it is for |
|---|---|---|
| Agentic AI security core | [agentic-action-authority](https://github.com/krivonosoff161/agentic-action-authority), [agentic-security-harness](https://github.com/krivonosoff161/agentic-security-harness), [agentic-transfer-verifier](https://github.com/krivonosoff161/agentic-transfer-verifier), [ai-agent-handoff](https://github.com/krivonosoff161/ai-agent-handoff) | Exact-action approval product, defensive falsification and evidence lab, transfer checks, and handoff boundaries. |
| LLM safety playbooks | [llm-safety-playbooks](https://github.com/krivonosoff161/llm-safety-playbooks) | Short practical skills for safer LLM use: data vs instructions, secrets, generated URLs/packages, Git actions, handoffs, and safe research scope. |
| Other projects: AI-assisted trading | [trading-bot-v2](https://github.com/krivonosoff161/trading-bot-v2), [honest-backtest](https://github.com/krivonosoff161/honest-backtest) | Research and paper-validation discipline; development paused pending hardware. |
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
- a published 1.14.2 release with a guarded writer reused by Action Authority's optional adapter;
- a provider-neutral Agent Host V1 offline workflow with canonical recordings;
- bounded synthetic Runtime Gateway reference work for policy-before-tool-dispatch.

It is not a hacking toolkit and not a promise of complete protection. It is a
measurement and learning lab for authorized, synthetic, local, or explicitly
owned targets.

The Runtime Gateway reference contour published in v1.3.0 uses synthetic tools
and credential-free fixtures. That historical reference does not establish
deployment or production enforcement.

## Other Projects: Trading Research Stack

Trading development is paused pending hardware. The trading line is an applied
AI-assisted research system, not a signal service or public profitability claim.

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
- Exact-action approval: [agentic-action-authority](https://github.com/krivonosoff161/agentic-action-authority)
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
