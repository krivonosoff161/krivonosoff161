# AI-Assisted Workflow

This workflow treats LLM agents as engineering participants under constraints.

## Operating Model

1. A human defines the problem, scope, risks, and success criteria.
2. One or more agents inspect the code or documents.
3. The task is converted into small verifiable changes.
4. Tests, reports, and review passes decide whether the work is acceptable.
5. The result is committed only after verification.

## Why This Matters

Agentic coding is powerful, but uncontrolled autonomy creates risk:

- private files can leak into commits;
- public docs can overclaim;
- tests can drift away from real behavior;
- agents can solve the wrong problem;
- context can fragment across sessions.

The workflow uses explicit boundaries:

- read-only review when needed;
- separate public and private repositories;
- no secret files in commits;
- deterministic tests before push;
- docs updated with code;
- conservative claims.

## Common Pattern

```text
idea
  -> safe framing
  -> task brief
  -> implementation
  -> local tests
  -> adversarial review
  -> fixes
  -> commit
  -> push
  -> post-run audit
```

## Human Role

The human role is not replaced. It changes:

- choose the problem;
- decide what matters;
- reject weak outputs;
- compare agents;
- keep private boundaries;
- force measurable artifacts;
- decide what is public.

## Agent Role

Agents are useful for:

- codebase search;
- implementation;
- test generation;
- documentation alignment;
- audit passes;
- alternative designs;
- regression checks.

They are not trusted blindly.

## Rule

If a project cannot explain its evidence, it is not finished.
