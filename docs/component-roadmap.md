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

1. Harness main declares the source extras `transfer`, `handoff`, `playbooks`, `router`,
   `filter`, and `all`; the router distribution coordinate is `agentic-llm-router`.
2. These extras are available only from the exact merged source or a controlled wheelhouse
   until a separate release publishes matching artifacts to public PyPI.
3. Installation does not activate an extension. Metadata inspection, owner approval, and
   explicit binding remain mandatory and Runtime Guard remains private `contract_only`.
4. Profile CI rejects source-pin drift, broken links and unknown component identifiers.
5. Trading governance remains separate and this profile remains authority-free.
