"""Fail-closed validation for the public AI Portfolio integration surface."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE = ROOT / "docs" / "portfolio-governance.yaml"
SECURITY = ROOT / "docs" / "security-portfolio-roadmap-public.yaml"
TRADING = ROOT / "docs" / "trading-portfolio-public.yaml"
README = ROOT / "README.md"
COMPONENT = ROOT / "component.yaml"

EXPECTED_LEGACY_SECURITY_PROJECTION_SHA256 = (
    "d960d5a710c152c28ad9837ebd665a476d0fc99562076ff6f1c5f24e73dd0bd6"
)
EXPECTED_ECOSYSTEM_ROADMAP_SHA256 = (
    "1c5c72e88ec18dade8b0828610d29cafd629a8595a64073de825a75cdff1a8a7"
)
EXPECTED_TRADING_MANIFEST_SHA256 = (
    "de9567921c2df7326f365aa16ad8add50c809c05323c171914a9b3f24d90b52e"
)
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SECRET_VALUE = re.compile(
    r"(?i)(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|authorization)"
    r"\s*[:=]\s*\S+|cred://|-----BEGIN [A-Z ]*PRIVATE KEY-----|"
    r"\bsk-[A-Za-z0-9_-]{12,}"
)
PRIVATE_MARKER = re.compile(
    r"(?i)(?:[a-z]:\\(?:users|tmp|ai\\research-artifacts)\\|file://|/home/[^/]+/)"
)


class GovernanceError(ValueError):
    """Raised when a portfolio documentation invariant fails."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GovernanceError(f"cannot load {path.name}: {exc}") from exc
    if not isinstance(value, dict):
        raise GovernanceError(f"{path.name} root must be an object")
    return value


def utf8_lf_digest(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def validate_governance(value: dict[str, Any]) -> None:
    required = {
        "schema_version",
        "governance_version",
        "verified_date",
        "authority",
        "portfolio_integrator",
        "instruction_precedence",
        "lower_level_rule",
        "document_roles",
        "repository_owners",
        "source_pins",
        "status_values",
        "authority_values",
        "projection_rules",
        "owner_gates",
    }
    if set(value) != required:
        raise GovernanceError("governance root shape drift")
    if value["schema_version"] != "AIPortfolioGovernance.v1":
        raise GovernanceError("unsupported governance schema")
    if value["governance_version"] != "2026.08.26-v3":
        raise GovernanceError("unexpected governance version")
    if value["verified_date"] != "2026-08-26" or value["authority"] != "none":
        raise GovernanceError("governance date or authority drift")
    if value["lower_level_rule"] != "narrow_only":
        raise GovernanceError("lower-level rules may only narrow governance")

    owners = value["repository_owners"]
    ids = [item["id"] for item in owners]
    roles = [item["role"] for item in owners]
    if len(ids) != len(set(ids)) or len(roles) != len(set(roles)):
        raise GovernanceError("repository ids and owner roles must be unique")
    expected_roles = {
        "private_security_research_upstream": "agentic-runtime-guard",
        "security_public_ecosystem_roadmap": "agentic-security-harness",
        "trading_portfolio": "trading-bot-v2",
        "skeptical_trading_validation": "honest-backtest",
        "portfolio_navigation_integration": "krivonosoff161",
    }
    by_role = {item["role"]: item["id"] for item in owners}
    if any(by_role.get(role) != owner for role, owner in expected_roles.items()):
        raise GovernanceError("canonical repository owner drift")

    pins = value["source_pins"]
    security = pins["security"]
    trading = pins["trading"]
    for item in (
        security["harness_baseline"],
        trading["trading_main"],
        trading["honest_backtest_main"],
    ):
        if not SHA_RE.fullmatch(item):
            raise GovernanceError("invalid merged-main pin")
    for item in (
        security["canonical_roadmap_sha256"],
        security["legacy_projection_sha256"],
        trading["canonical_manifest_sha256"],
    ):
        if not SHA256_RE.fullmatch(item):
            raise GovernanceError("invalid manifest digest pin")
    if security["canonical_repository"] != (
        "https://github.com/krivonosoff161/agentic-security-harness"
    ) or security["canonical_roadmap_path"] != "ecosystem/roadmap.yaml":
        raise GovernanceError("Security public roadmap owner drift")
    if security["canonical_roadmap_sha256"] != EXPECTED_ECOSYSTEM_ROADMAP_SHA256:
        raise GovernanceError("Security ecosystem roadmap digest pin drift")
    if security["legacy_projection_sha256"] != EXPECTED_LEGACY_SECURITY_PROJECTION_SHA256:
        raise GovernanceError("legacy Security projection digest pin drift")
    if trading["canonical_manifest_sha256"] != EXPECTED_TRADING_MANIFEST_SHA256:
        raise GovernanceError("Trading manifest digest pin drift")
    if trading["hash_canonicalization"] != "utf8_lf":
        raise GovernanceError("Trading digest must be UTF-8 LF canonicalized")
    mandatory = {"merge", "release_or_tag", "deployment", "enforcement_activation"}
    if not mandatory <= set(value["owner_gates"]):
        raise GovernanceError("mandatory owner gate is missing")


def validate_trading_projection(value: dict[str, Any], governance: dict[str, Any]) -> None:
    expected = {
        "schema_version",
        "projection_version",
        "verified_date",
        "source_owner",
        "skeptical_validator",
        "portfolio_integrator",
        "source_manifest_sha256",
        "hash_canonicalization",
        "merged_main",
        "status",
        "authority",
        "capability_summary",
        "next_gate",
        "non_claims",
    }
    if set(value) != expected:
        raise GovernanceError("Trading projection root shape drift")
    pins = governance["source_pins"]["trading"]
    if value["source_owner"] != "trading-bot-v2":
        raise GovernanceError("Trading owner drift")
    if value["skeptical_validator"] != "honest-backtest":
        raise GovernanceError("Trading validator owner drift")
    if value["source_manifest_sha256"] != pins["canonical_manifest_sha256"]:
        raise GovernanceError("Trading manifest digest mismatch")
    if value["hash_canonicalization"] != "utf8_lf":
        raise GovernanceError("Trading projection canonicalization drift")
    if value["merged_main"] != {
        "trading-bot-v2": pins["trading_main"],
        "honest-backtest": pins["honest_backtest_main"],
    }:
        raise GovernanceError("Trading merged-main pins mismatch")
    if value["authority"] != "none" or value["status"] != "current":
        raise GovernanceError("Trading projection status or authority drift")
    required_non_claims = {"profitability", "live_readiness", "order_authority"}
    if not required_non_claims <= set(value["non_claims"]):
        raise GovernanceError("Trading non-claim drift")
    ids = [item["id"] for item in value["capability_summary"]]
    if len(ids) != len(set(ids)):
        raise GovernanceError("duplicate Trading capability")


def validate_readme_navigation() -> None:
    text = README.read_text(encoding="utf-8")
    match = re.search(r"(?ms)^## Start Here\s*$\n(.*?)(?=^## )", text)
    if match is None:
        raise GovernanceError("README lacks Start Here")
    links = re.findall(r"(?m)^- \[[^]]+\]\(([^)]+)\)\s*$", match.group(1))
    expected = [
        "docs/current-portfolio-state.md",
        "docs/security-portfolio.md",
        "docs/trading-portfolio.md",
        "docs/portfolio.md",
    ]
    if links != expected:
        raise GovernanceError("Start Here must contain exactly four ordered entry points")
    if "## Repositories" not in text:
        raise GovernanceError("README lacks separate repository catalog section")
    if "agentic-security-harness/blob/main/ecosystem/roadmap.yaml" not in text:
        raise GovernanceError("README does not point to the public Harness roadmap")


def validate_component_manifest() -> None:
    component = load_json(COMPONENT)
    required = {
        "schema_version", "component_id", "display_name", "repository", "visibility",
        "kind", "summary", "package", "owns", "consumes", "contracts", "docs",
        "compatibility", "integration_status", "evidence_refs", "claims", "non_claims",
        "authority",
    }
    if set(component) != required:
        raise GovernanceError("component manifest shape drift")
    if component["schema_version"] != "AgenticSecurityEcosystemComponent.v1":
        raise GovernanceError("unsupported component manifest schema")
    if component["component_id"] != "krivonosoff161" or component["kind"] != "profile_projection":
        raise GovernanceError("profile component identity drift")
    if component["visibility"] != "public" or component["authority"] != "none":
        raise GovernanceError("profile component visibility or authority drift")
    if component["integration_status"] != "standalone":
        raise GovernanceError("profile projection cannot claim suite integration")


def validate_local_links() -> None:
    markdown_files = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]
    link_pattern = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            target = target.split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if ROOT.resolve() != resolved and ROOT.resolve() not in resolved.parents:
                raise GovernanceError(f"link escapes repository: {path.relative_to(ROOT)}")
            if not resolved.exists():
                raise GovernanceError(
                    f"broken local link: {path.relative_to(ROOT)} -> {target}"
                )


def validate_public_hygiene() -> None:
    forbidden_names = {".env", ".env.local", ".env.production"}
    tracked_names = {path.name.lower() for path in ROOT.rglob("*") if path.is_file()}
    if forbidden_names & tracked_names:
        raise GovernanceError("environment file is present in the public tree")
    if any(name.endswith((".sqlite", ".sqlite3", ".db", ".log")) for name in tracked_names):
        raise GovernanceError("runtime database or log is present in the public tree")
    for path in [
        ROOT / "AGENTS.md",
        ROOT / "README.md",
        ROOT / "component.yaml",
        *sorted((ROOT / "docs").rglob("*")),
    ]:
        if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".json"}:
            continue
        text = path.read_text(encoding="utf-8")
        if SECRET_VALUE.search(text):
            raise GovernanceError(f"secret-shaped value in {path.relative_to(ROOT)}")
        if PRIVATE_MARKER.search(text):
            raise GovernanceError(f"private/runtime marker in {path.relative_to(ROOT)}")


def validate_all() -> None:
    governance = load_json(GOVERNANCE)
    validate_governance(governance)
    security = load_json(SECURITY)
    if hashlib.sha256(SECURITY.read_bytes()).hexdigest() != EXPECTED_LEGACY_SECURITY_PROJECTION_SHA256:
        raise GovernanceError("preserved legacy Security projection bytes drift")
    if security.get("authority") != "none":
        raise GovernanceError("legacy Security projection grants authority")
    validate_component_manifest()
    validate_trading_projection(load_json(TRADING), governance)
    validate_readme_navigation()
    validate_local_links()
    validate_public_hygiene()


def main() -> int:
    validate_all()
    print(f"portfolio governance valid: {utf8_lf_digest(GOVERNANCE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
