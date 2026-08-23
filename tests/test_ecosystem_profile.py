from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_profile_manifest_is_projection_only() -> None:
    component = json.loads((ROOT / "component.yaml").read_text(encoding="utf-8"))

    assert component["schema_version"] == "AgenticSecurityEcosystemComponent.v1"
    assert component["component_id"] == "krivonosoff161"
    assert component["kind"] == "profile_projection"
    assert component["integration_status"] == "standalone"
    assert component["authority"] == "none"
    assert component["package"] == {
        "name": None,
        "version": None,
        "install": None,
        "entry_points": [],
    }


def test_current_security_docs_use_harness_public_authority() -> None:
    current = (
        (ROOT / "README.md").read_text(encoding="utf-8")
        + (ROOT / "docs" / "component-roadmap.md").read_text(encoding="utf-8")
        + (ROOT / "docs" / "security-portfolio.md").read_text(encoding="utf-8")
    )

    assert "agentic-security-harness/blob/main/ecosystem/roadmap.yaml" in current
    assert "private canonical source remains in Runtime" not in current
    assert "Runtime Guard owns the Security product roadmap" not in current
    assert "Authority: `none`" in current


def test_legacy_security_projection_is_preserved_as_history() -> None:
    roadmap = (ROOT / "docs" / "component-roadmap.md").read_text(encoding="utf-8")
    normalized = " ".join(roadmap.split())
    legacy_yaml = ROOT / "docs" / "security-portfolio-roadmap-public.yaml"
    legacy_markdown = ROOT / "docs" / "security-portfolio-roadmap-public.md"

    assert legacy_yaml.is_file() and legacy_markdown.is_file()
    assert "retained as a digest-bound historical R4 projection" in normalized
    assert "no longer the current Security roadmap" in normalized
