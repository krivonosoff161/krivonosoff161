from __future__ import annotations

import copy
import unittest

from tools.validate_portfolio_governance import (
    GOVERNANCE,
    TRADING,
    GovernanceError,
    load_json,
    validate_all,
    validate_governance,
    validate_trading_projection,
)


class PortfolioGovernanceTests(unittest.TestCase):
    def test_repository_state_is_valid(self) -> None:
        validate_all()

    def test_duplicate_owner_is_rejected(self) -> None:
        value = copy.deepcopy(load_json(GOVERNANCE))
        value["repository_owners"][1]["role"] = value["repository_owners"][0]["role"]
        with self.assertRaisesRegex(GovernanceError, "unique"):
            validate_governance(value)

    def test_owner_promotion_is_rejected(self) -> None:
        value = copy.deepcopy(load_json(GOVERNANCE))
        value["repository_owners"][0]["id"] = "profile-shadow"
        with self.assertRaisesRegex(GovernanceError, "owner drift"):
            validate_governance(value)

    def test_semantic_digest_change_is_rejected(self) -> None:
        value = copy.deepcopy(load_json(GOVERNANCE))
        value["source_pins"]["trading"]["canonical_manifest_sha256"] = "0" * 64
        with self.assertRaisesRegex(GovernanceError, "digest pin drift"):
            validate_governance(value)

    def test_trading_main_drift_is_rejected(self) -> None:
        governance = load_json(GOVERNANCE)
        value = copy.deepcopy(load_json(TRADING))
        value["merged_main"]["trading-bot-v2"] = "0" * 40
        with self.assertRaisesRegex(GovernanceError, "merged-main pins mismatch"):
            validate_trading_projection(value, governance)

    def test_trading_authority_promotion_is_rejected(self) -> None:
        governance = load_json(GOVERNANCE)
        value = copy.deepcopy(load_json(TRADING))
        value["authority"] = "live_execution"
        with self.assertRaisesRegex(GovernanceError, "authority drift"):
            validate_trading_projection(value, governance)


if __name__ == "__main__":
    unittest.main()
