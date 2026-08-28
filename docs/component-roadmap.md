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

## Next documentation gates

1. Preserve the merged v1.3.0 status projection while the optional-extras stack is in review.
2. After exact-head merges, repin the Harness merge SHA and regenerate install commands from
   the merged package metadata rather than from review branches.
3. Reject profile drift, broken links and unknown component identifiers in CI.
4. Keep Trading governance separate from the Security ecosystem migration.
5. Keep profile updates projection-only and authority-free.
