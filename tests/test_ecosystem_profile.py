from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class EcosystemProfileTests(unittest.TestCase):
    def test_profile_manifest_is_projection_only(self) -> None:
        component = json.loads((ROOT / "component.yaml").read_text(encoding="utf-8"))

        self.assertEqual(
            component["schema_version"], "AgenticSecurityEcosystemComponent.v1"
        )
        self.assertEqual(component["component_id"], "krivonosoff161")
        self.assertEqual(component["kind"], "profile_projection")
        self.assertEqual(component["integration_status"], "standalone")
        self.assertEqual(component["authority"], "none")
        self.assertEqual(
            component["package"],
            {
                "name": None,
                "version": None,
                "install": None,
                "entry_points": [],
            },
        )

    def test_current_security_docs_use_harness_public_authority(self) -> None:
        current = (
            (ROOT / "README.md").read_text(encoding="utf-8")
            + (ROOT / "docs" / "component-roadmap.md").read_text(encoding="utf-8")
            + (ROOT / "docs" / "security-portfolio.md").read_text(encoding="utf-8")
        )

        self.assertIn(
            "agentic-security-harness/blob/main/ecosystem/roadmap.yaml", current
        )
        self.assertNotIn("private canonical source remains in Runtime", current)
        self.assertNotIn("Runtime Guard owns the Security product roadmap", current)
        self.assertIn("Authority: `none`", current)

    def test_security_projection_is_pinned_to_merged_harness_main(self) -> None:
        governance = json.loads(
            (ROOT / "docs" / "portfolio-governance.yaml").read_text(encoding="utf-8")
        )
        security = governance["source_pins"]["security"]

        self.assertEqual(
            security["harness_baseline"],
            "59bbdd42a34450f372e4b54c02de21b155e008c8",
        )
        self.assertEqual(
            security["canonical_roadmap_sha256"],
            "263f0b985172579661d60de73da935a311b513213c438d210155c7310938af03",
        )

        for relative_path in (
            "docs/current-portfolio-state.md",
            "docs/execution-map.md",
        ):
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("Harness `59bbdd4`", text)

    def test_installation_projection_preserves_release_and_activation_boundaries(self) -> None:
        current = (ROOT / "docs" / "current-portfolio-state.md").read_text(
            encoding="utf-8"
        )
        roadmap = (ROOT / "docs" / "component-roadmap.md").read_text(
            encoding="utf-8"
        )
        catalog = (ROOT / "docs" / "portfolio.md").read_text(encoding="utf-8")
        normalized_current = " ".join(current.split())

        self.assertIn("`agentic-llm-router`", roadmap)
        self.assertIn("agentic-security-harness[router]==1.4.0", normalized_current)
        self.assertIn("agentic-security-harness[all]==1.4.0", normalized_current)
        self.assertIn("resolves exact companion versions from public PyPI", roadmap)
        self.assertIn("Installation does not activate an extension", roadmap)
        for coordinate in (
            "agentic-transfer-verifier==0.2.1",
            "agentic-transfer-verifier-harness-extension==1.0.1",
            "ai-agent-handoff==0.3.0",
            "ai-agent-handoff-harness-extension==1.0.0",
            "llm-safety-playbooks==0.1.0",
            "agentic-llm-router==0.2.0",
            "llm-cheap-filter==0.2.0",
        ):
            self.assertIn(coordinate, roadmap)
        self.assertIn(
            "[llm-router](https://github.com/krivonosoff161/llm-router) | `contract_only`",
            catalog,
        )

    def test_legacy_security_projection_is_preserved_as_history(self) -> None:
        roadmap = (ROOT / "docs" / "component-roadmap.md").read_text(encoding="utf-8")
        normalized = " ".join(roadmap.split())
        legacy_yaml = ROOT / "docs" / "security-portfolio-roadmap-public.yaml"
        legacy_markdown = ROOT / "docs" / "security-portfolio-roadmap-public.md"

        self.assertTrue(legacy_yaml.is_file() and legacy_markdown.is_file())
        self.assertIn(
            "retained as a digest-bound historical R4 projection", normalized
        )
        self.assertIn("no longer the current Security roadmap", normalized)
