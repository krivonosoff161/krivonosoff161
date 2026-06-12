# Case Study: Agentic Security Harness

## Problem

LLM agents are no longer only chatbots. They read tool output, write memory,
route data, call APIs, and hand work to other agents. That creates failure modes
that classic prompt filtering does not fully cover:

- recipient confusion;
- sensitivity-label stripping;
- memory poisoning;
- tool-permission abuse;
- provider-boundary leakage;
- cross-agent contamination;
- audit gaps.

## What I Built

Agentic Security Harness is a trace-first defensive benchmark for these failure
modes.

The current public version includes:

- deterministic local targets;
- a seven-pattern seed corpus;
- vulnerable vs protected replay;
- portable traces;
- scorecards;
- artifact validation;
- safe research documentation.

## Why It Is Useful

The project does not claim complete protection. It gives teams a way to ask
better questions:

- Did the label survive the agent handoff?
- Did the memory write preserve storage rules?
- Did the tool call respect the recipient boundary?
- Did the protected target reduce findings compared with the baseline?
- Can the run be replayed and reviewed?

## Safety Frame

The repository is defensive by design:

- mock/demo/local targets;
- synthetic data;
- no real secrets;
- no live exploitation;
- no instructions for abusing third-party systems.

The goal is to build measurement infrastructure, not an offensive toolkit.

## Evidence

Useful artifacts in the repository:

- `examples/demo-report/`
- `examples/protected-demo-agent-report/`
- `examples/comparison-report/`
- `docs/harness.md`
- `docs/corpus.md`
- `docs/problem-solution-catalog.md`
