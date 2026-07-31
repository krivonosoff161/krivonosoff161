"""Validate the public Security Portfolio Roadmap without private-repo access."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROJECTION = ROOT / "docs" / "security-portfolio-roadmap-public.yaml"
MARKDOWN = ROOT / "docs" / "security-portfolio-roadmap-public.md"
FORBIDDEN_KEYS = {"commit", "credential", "secret", "seed", "label", "holdout"}
ROOT_KEYS = {
    "schema_version",
    "roadmap_version",
    "baseline_date",
    "source_sha256",
    "rendered_markdown_sha256",
    "authority",
    "thesis",
    "global_invariants",
    "repositories",
    "status_profiles",
    "modules",
    "relations",
    "phases",
    "claims",
    "residual_risks",
    "owner_gates",
}
SECRET_VALUE = re.compile(
    r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|authorization)"
    r"\s*[:=]\s*\S+|cred://|-----BEGIN [A-Z ]*PRIVATE KEY-----|"
    r"\bsk-[A-Za-z0-9_-]{12,}"
)


def fail(message: str) -> None:
    raise SystemExit(message)


def assert_acyclic(items: list[dict[str, Any]], label: str) -> None:
    graph = {item["id"]: list(item.get("depends_on", [])) for item in items}
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            fail(f"{label} dependency cycle at {node}")
        if node in visited:
            return
        if node not in graph:
            fail(f"unknown {label} dependency: {node}")
        visiting.add(node)
        for dependency in graph[node]:
            visit(dependency)
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)


def main() -> int:
    try:
        projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot load public projection: {exc}")
    if projection.get("schema_version") != "SecurityPortfolioRoadmapPublic.v1":
        fail("unsupported public projection schema")
    if projection.get("authority") != "none":
        fail("public projection grants authority")
    if set(projection) != ROOT_KEYS:
        fail("public projection root shape drift")
    digest = projection.get("source_sha256", "")
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        fail("invalid private-source digest")
    serialized = json.dumps(projection, ensure_ascii=False).lower()
    if len(PROJECTION.read_bytes()) > 512_000 or SECRET_VALUE.search(serialized):
        fail("public projection is oversized or contains a secret-shaped value")
    for key in FORBIDDEN_KEYS:
        if f'"{key}"' in serialized:
            fail(f"forbidden public key: {key}")
    if re.search(r"[a-z]:\\\\|/users/|/tmp/|worktree", serialized, re.IGNORECASE):
        fail("local filesystem marker in public projection")
    shapes = {
        "repository": (
            {"id", "repository", "visibility", "role", "roadmap_authority"},
            projection["repositories"],
        ),
        "module": (
            {
                "id",
                "owner",
                "status",
                "evidence_class",
                "depends_on",
                "delivers",
                "next_gates",
                "forbidden_claims",
            },
            projection["modules"],
        ),
        "relation": ({"source", "target", "type", "authority_effect"}, projection["relations"]),
        "phase": (
            {"id", "status", "depends_on", "modules", "exit_criteria", "criterion_status"},
            projection["phases"],
        ),
        "claim": (
            {
                "id",
                "module",
                "supported_claim",
                "evidence_class",
                "causal_scope",
                "forbidden_promotions",
                "next_gate",
            },
            projection["claims"],
        ),
        "risk": ({"id", "severity", "status", "mitigated_by"}, projection["residual_risks"]),
    }
    for label, (expected, items) in shapes.items():
        if any(not isinstance(item, dict) or set(item) != expected for item in items):
            fail(f"unexpected {label} properties")
    assert_acyclic(projection["modules"], "module")
    assert_acyclic(projection["phases"], "phase")
    module_ids = {item["id"] for item in projection["modules"]}
    for relation in projection["relations"]:
        if relation["source"] not in module_ids or relation["target"] not in module_ids:
            fail("relation refers to an unknown module")
        if relation["type"] in {"advises", "informs", "validates", "records_to"}:
            if relation["authority_effect"] != "none":
                fail("advisory relation expands authority")
    markdown = MARKDOWN.read_bytes()
    markdown_digest = hashlib.sha256(markdown).hexdigest()
    if markdown_digest != projection.get("rendered_markdown_sha256"):
        fail("public Markdown bytes do not match the renderer-bound digest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
