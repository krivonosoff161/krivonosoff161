# Case Study: Trading Research System

## Problem

Trading research is easy to fool:

- noisy news looks important;
- backtests overfit;
- public narratives arrive late;
- cheap signals drown useful ones;
- expensive LLM calls get wasted on weak inputs;
- good-looking setups fail when costs, regimes, and forward evidence are added.

## System Direction

The private trading system is built as research infrastructure, not as a public
signal product.

Main components:

- source ingestion;
- normalized machine-readable events;
- cheap layer model for fact extraction;
- code-level orchestration gates;
- expensive model only for candidates;
- Telegram output only for GO/WATCH decisions;
- outcome resolution and no-go audits;
- strategy lab for deterministic research runs;
- private candidate registry.

## Public Boundary

Public repositories show the reusable methods:

- cheap-to-chief routing;
- honest validation;
- LLM routing;
- agent handoff;
- research documentation patterns.

Private repositories hold:

- real candidate results;
- parameter libraries;
- data snapshots;
- market-specific findings;
- operational dashboards.

## Why It Is Useful

The system is designed to answer:

- what did we test;
- why was it rejected;
- what survived validation;
- what needs forward evidence;
- where LLM review helped;
- where it only produced narrative.

The value is not a single prediction. The value is a repeatable research
process.

## Non-Claim

This work does not claim profitability. It is infrastructure for filtering,
measuring, and validating ideas under explicit constraints.
