# Public profile component roadmap

Status: generated-source navigation contract  
Authority: `none`

The canonical public roadmap for the Agentic Security ecosystem is the machine-readable
[`ecosystem/roadmap.yaml`](https://github.com/krivonosoff161/agentic-security-harness/blob/main/ecosystem/roadmap.yaml)
in Agentic Security Harness. Its generated human view is
[`docs/ecosystem-roadmap.md`](https://github.com/krivonosoff161/agentic-security-harness/blob/main/docs/ecosystem-roadmap.md).

This profile is a projection and navigation surface. It does not own component status,
compatibility, claims, release state or authority. Security information shown here must be
generated from or directly linked to the public Harness contract; repository-local facts
remain owned by their source repositories.

## Projection flow

```text
Harness ecosystem/roadmap.yaml
  + source-owned component.yaml manifests
  + Harness compatibility contract
        -> generated public profile summary
        -> links to component-owned documentation and evidence
```

## Preserved history

The files `security-portfolio-roadmap-public.yaml` and
`security-portfolio-roadmap-public.md` are retained as a digest-bound historical R4
projection. They are no longer the current Security roadmap and must not override the Harness
ecosystem contract.

## Current installation projection

1. Harness `v1.4.0` publishes the extras `transfer`, `handoff`, `playbooks`, `router`,
   `filter`, and `all`; the router distribution coordinate is `agentic-llm-router`.
2. Every extra and `all` resolves exact companion versions from public PyPI in a clean
   environment without editable installs, local paths, Git URLs, or a pre-existing wheelhouse.
3. Installation does not activate an extension. Metadata inspection, owner approval, and
   explicit binding remain mandatory and Runtime Guard remains private `contract_only`.
4. Profile CI rejects source-pin drift, broken links and unknown component identifiers.
5. Trading governance remains separate and this profile remains authority-free.

Exact public coordinates consumed by Harness `1.4.0`:

- `transfer`: `agentic-transfer-verifier==0.2.1` and
  `agentic-transfer-verifier-harness-extension==1.0.1`;
- `handoff`: `ai-agent-handoff==0.3.0` and
  `ai-agent-handoff-harness-extension==1.0.0`;
- `playbooks`: `llm-safety-playbooks==0.1.0`;
- `router`: `agentic-llm-router==0.2.0`;
- `filter`: `llm-cheap-filter==0.2.0`.
