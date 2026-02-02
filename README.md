# Identity-Geometry

**Fisher-Rao information geometry + rational inattention novelty scoring for LLM outputs.**

Lightweight, research-grade Python library for computing **novelty and information density** in language models. Provides reproducible **diagonal Fisher trace**, **KL divergence**, and a **novelty functional** that combines both measures.

---

Overview

This repository provides a minimal, production-ready method for measuring informational novelty in Large Language Model (LLM) outputs.

The metric answers one question:

How much new information does this text contain from the model’s own perspective?

Unlike embedding similarity or sampling-based diversity metrics, this approach uses signals internal to the model, producing a deterministic and auditable score.

What “Novelty” Means

Novelty here does not mean creativity or style.

A text is considered novel if:

The model makes a confident, non-generic prediction

The input meaningfully activates model parameters

The score is not inflated by length or repetition

This is model-relative informational novelty.

How It Works

The score combines three internal signals:

Prediction confidence

Parameter sensitivity

Length normalization

These are combined into a single scalar value.

How to Interpret the Score

High score
The input is informative and strongly affects the model.

Medium score
Mostly predictable with some meaningful signal.

Low score
Generic, boilerplate, or well-memorized content.

Why This Is Useful

Deterministic novelty scoring

Model-aware evaluation

Auditable and production-safe

Common uses:

Prompt quality evaluation

Dataset curation and deduplication

Memorization detection

Redundancy filtering

Agent self-evaluation
