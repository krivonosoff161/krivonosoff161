# Case Study: Agentic Security Harness

## Problem

LLM agents are no longer only chatbots. They read tool output, write memory,
route data, call APIs, and hand work to other agents. That creates failure modes
that classic prompt filtering does not fully cover:

- data-boundary confusion;
- recipient and authority drift;
- memory governance failures;
- tool and provider boundary mistakes;
- approval context gaps;
- audit trail weakness;
- perception and ambient-context confusion.

## What I Built

Agentic Security Harness is a trace-first defensive benchmark toolkit for these
failure modes.

The current public version includes:

- deterministic local targets;
- a 24-pattern deterministic seed corpus;
- vulnerable vs protected replay;
- scenario matrices;
- external OpenAI-compatible model/runtime checks;
- portable traces;
- scorecards;
- remediation guidance;
- schema validation;
- run diffs;
- self-contained HTML reports;
- local run indexing.

## Why It Is Useful

The project does not claim complete protection. It gives teams a way to ask
better questions:

- Did the label survive the agent handoff?
- Did memory preserve scope?
- Did approval apply to the exact action being taken?
- Did the target keep tool and authority boundaries separate?
- Did the protected version reduce findings compared with the baseline?
- Can the run be replayed, validated, diffed, and reviewed?

## Safety Frame

The repository is defensive by design:

- mock/demo/local targets;
- synthetic data;
- no real secrets;
- no live exploitation;
- no third-party abuse;
- explicit residual-risk language.

The goal is measurement infrastructure, not an offensive toolkit.

## Evidence

Useful artifacts in the repository:

- `examples/demo-report/`
- `examples/protected-demo-agent-report/`
- `examples/comparison-report/`
- `docs/benchmark-semantics.md`
- `docs/corpus.md`
- `docs/problem-solution-catalog.md`
- `docs/connect-models.md`
- `docs/run-diff.md`
- `docs/artifact-schemas.md`
