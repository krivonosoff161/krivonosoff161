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
            "5e82e80c9cb96233d23e84e0318b374a6b8f6b01",
        )
        self.assertEqual(
            security["canonical_roadmap_sha256"],
            "1c5c72e88ec18dade8b0828610d29cafd629a8595a64073de825a75cdff1a8a7",
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
