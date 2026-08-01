# Agentic AI Security Portfolio: публичная дорожная карта

> Санитизированная проекция приватной канонической карты. Не содержит секретов, закрытых сценариев, holdout-данных или operational authority.

## Что строится

Prevent untrusted observations from becoming trusted context, authority, capability, consent, or effects without provenance, explicit policy, bounded execution, and privacy-minimized evidence.

Репозитории остаются федеративными: Runtime Guard — приватный composition root, Harness — публичная лаборатория фальсификации, остальные репозитории владеют ограниченными библиотечными, edge- или support-модулями.

## Модули

| Модуль | Владелец | Текущий честный статус | Следующий доказательный gate |
|---|---|---|---|
| M01-boundary-adapters | agentic-runtime-guard | partial | loss_accounting_for_each_source; authenticated_producer_design |
| M02-canonical-envelope | agentic-security-harness | partial | stable_cross_repository_schema; lossless_required_field_adapters; version_migration_tests |
| M03-trust-graph | agentic-runtime-guard | partial | producer_attestation; telemetry_loss_budget; cross_repository_conformance |
| M04-transfer-verifier | agentic-transfer-verifier | partial | json_loader; cli_and_report_artifacts; runtime_advisory_adapter; representative_transfer_labels |
| M05-deterministic-policy | agentic-runtime-guard | implemented_bounded | advisory_input_contract; policy_version_migration; hostile_bypass_review |
| M06-semantic-sentinel | agentic-runtime-guard | preregistered_not_implemented | artifact_license_code_template_policy_commitment; leakage_audit; independent_family_partition; selective_risk_evaluation |
| M07-swarm-analyzer | agentic-runtime-guard | research_only | new_frozen_hypothesis; new_unseen_family_evaluation; independent_custody |
| M08-decision-gateway | agentic-runtime-guard | planned | formal_combination_algebra; conflict_tests; no_authority_promotion_proof |
| M09-receipt-authority | agentic-runtime-guard | implemented_bounded | receipt_lifecycle_security_review; key_isolation; concurrency_and_crash_tests |
| M10-bounded-executor | agentic-runtime-guard | implemented_synthetic | os_sandbox_design; junction_hardlink_handle_race_tests; disposable_pilot |
| M11-evidence-ledger | agentic-runtime-guard | partial | pseudonymization_review; retention_policy; tamper_evidence; restore_and_loss_tests |
| M12-harness-regression | agentic-security-harness | implemented_development | scenario_alias_registry; causal_ablations; unseen_family_protocol; product_contract_replay |
| M13-handoff-edge | ai-agent-handoff | implemented_pattern_guard | verified_metadata_adapter; sequence_safety_tests |
| M14-provider-router | llm-router | optional_support | concurrent_budget_reservations; provider_contract_tests; secret_broker_boundary |
| M15-cost-triage | llm-cheap-filter | optional_support | labelled_routing_errors; independent_chief_validation; cannot_lower_guard_decision_test |
| M16-operator-playbooks | llm-safety-playbooks | implemented_guidance | map_playbooks_to_machine_controls; operator_usability_review |

## Связи и границы полномочий

| Источник | Связь | Назначение | Authority |
|---|---|---|---|
| M01-boundary-adapters | projects_to | M02-canonical-envelope | downgrade_only |
| M02-canonical-envelope | projects_to | M03-trust-graph | none |
| M03-trust-graph | informs | M04-transfer-verifier | none |
| M04-transfer-verifier | advises | M05-deterministic-policy | none |
| M02-canonical-envelope | projects_to | M06-semantic-sentinel | downgrade_only |
| M02-canonical-envelope | projects_to | M07-swarm-analyzer | downgrade_only |
| M06-semantic-sentinel | advises | M08-decision-gateway | none |
| M07-swarm-analyzer | advises | M08-decision-gateway | none |
| M05-deterministic-policy | constrains | M08-decision-gateway | none |
| M08-decision-gateway | authorizes_bounded | M09-receipt-authority | bounded_explicit_only |
| M09-receipt-authority | authorizes_bounded | M10-bounded-executor | bounded_explicit_only |
| M08-decision-gateway | records_to | M11-evidence-ledger | none |
| M10-bounded-executor | records_to | M11-evidence-ledger | none |
| M12-harness-regression | validates | M02-canonical-envelope | none |
| M12-harness-regression | validates | M06-semantic-sentinel | none |
| M12-harness-regression | validates | M07-swarm-analyzer | none |
| M13-handoff-edge | projects_to | M02-canonical-envelope | downgrade_only |
| M05-deterministic-policy | constrains | M14-provider-router | none |
| M05-deterministic-policy | constrains | M15-cost-triage | none |
| M16-operator-playbooks | informs | M05-deterministic-policy | none |

## Этапы

| Этап | Статус | Критерии завершения |
|---|---|---|
| P0-evidence-and-governance-baseline | complete | portfolio_roles_documented; claims_separated_by_evidence_class; private_and_public_boundaries_declared; owner_gates_explicit |
| P1-contract-convergence | active | versioned_canonical_envelope; field_level_loss_accounting; no_authority_promotion_tests; cross_repository_shadow_conformance |
| P2-shadow-product-slice | planned | end_to_end_fake_source_no_effect_sink; advisory_authority_type_separation; conflict_and_abstention_tests; privacy_minimized_evidence |
| P3-scientific-validation | planned | single_frozen_candidate_per_claim; family_disjoint_development_and_holdout; multiplicity_control; selective_risk_with_abstention; independent_or_explicit_single_operator_custody; negative_results_preserved |
| P4-privacy_preserving_pilot | owner_gated | rights_cleared_disposable_fixtures; visible_consent; retention_and_deletion_proof; incident_and_rollback_runbook; no_raw_prompt_default_storage |
| P5-bounded-enforcement | owner_gated | os_sandbox_hostile_review; receipt_key_isolation; race_and_crash_recovery_tests; fail_closed_manual_override; rollback_and_kill_switch; independent_security_review |
| P6-productization | owner_gated | license_and_public_private_split; supported_platform_matrix; signed_release_and_sbom; upgrade_and_migration_contract; support_and_vulnerability_process; claims_match_evidence |

## Что пока не заявляется

- `additive_scenario_count`
- `authenticated_source`
- `authentication_service`
- `blocking_authority`
- `calibrated_attack_probability`
- `certification`
- `cheap_model_agreement_as_trust`
- `complete_lineage`
- `complete_telemetry`
- `correctness_oracle`
- `cryptographic_handoff_verification`
- `cryptographic_identity`
- `enforcement`
- `field_validated_verdict`
- `forensic_completeness`
- `general_purpose_capability_token`
- `general_shell_authority`
- `generation2_reuse`
- `hostile_os_non_bypassability`
- `implemented_detector`
- `implemented_product_gate`
- `incident_probability`
- `invoice_truth`
- `lossless_three_model_conversion`
- `model_confidence_as_consent`
- `policy_gateway`
- `production_effectiveness`
- `production_enforcement`
- `production_non_bypassability`
- `provenance_validation`
- `raw_transcript_archive`
- `runtime_isolation`
- `secret_manager`
- `security_control`
- `semantic_intent_detection`
- `semantic_security_control`
- `semantic_truth`
- `stable_product_api`
- `universal_model_judge`
- `validated_accuracy`

## Отдельные решения владельца

- `merge`
- `release_or_tag`
- `deployment`
- `enforcement_activation`
- `real_provider_or_live_endpoint_use`
- `real_camera_or_microphone_use`
- `private_or_personal_data_use`
- `real_sealed_holdout_execution`
- `repository_visibility_or_license_change`

Версия: `2026.07.31-rc1`. Контроль источника: SHA-256 `181a0dd7fad62699693895b1bd5189c91984140a48a35afe811d948efee57fca`.
