# Novelty Functional for LLM Outputs

**Deterministic measurement of informational novelty relative to a language model**

**Version:** 1.0.0

---

## Overview

This repository implements a **minimal, production-ready novelty functional** for Large Language Model (LLM) outputs.

The objective is to measure:

> **How informationally novel is a given text *to the model itself*?**

Unlike embedding similarity, surface diversity, or sampling-based metrics, this approach operates **directly on the model’s predictive distribution and parameter sensitivity**, yielding a deterministic, auditable scalar.

---

## Core Concept

Novelty is defined as the interaction between:

1. **Distributional Certainty**  
   How concentrated the model’s next-token prediction is.

2. **Parameter Sensitivity**  
   How strongly the input activates model parameters.

3. **Length Normalization**  
   A penalty preventing trivial inflation from long or repetitive inputs.

All components are model-internal and architecture-aware.

---

## Formal Definition

Let:

- \( p_\theta \) be the model’s next-token distribution  
- \( U \) be the uniform distribution over the vocabulary  
- \( \theta \) be model parameters  
- \( x \) be the input text  

### KL Divergence (Certainty)

\[
\mathrm{KL}(p_\theta \,\|\, U)
\]

Measures how non-uniform (confident) the model’s prediction is.

---

### Diagonal Fisher Information (Sensitivity)

\[
\mathrm{Tr}(F_\theta(x)) =
\sum_i \left(\frac{\partial \log p_\theta(x)}{\partial \theta_i}\right)^2
\]

Measures parameter sensitivity to the input.

---

### Novelty Functional

\[
\mathrm{Novelty}(x) =
\frac{
\mathrm{KL}(p_\theta \,\|\, U)
\cdot
\mathrm{Tr}(F_\theta(x))
}{
\left(\frac{\text{tokens}(x)}{N}\right) + \varepsilon
}
\]

Where:
- \( N \) is an attention normalization constant (default: 512)
- \( \varepsilon \) ensures numerical stability

---

## Interpretation

| Score | Meaning |
|-----|--------|
| **High** | Confident prediction + high parameter sensitivity |
| **Medium** | Predictable structure with some informative signal |
| **Low** | Generic, boilerplate, or memorized content |

This is **model-relative novelty**, not semantic creativity or linguistic diversity.

---

## Why This Matters

This functional is useful when you need:

- Deterministic novelty scoring (no sampling variance)
- Model-aware evaluation (not embedding heuristics)
- Auditable metrics suitable for regulated environments
- Signal detection for:
  - Prompt quality assessment
  - Dataset curation / deduplication
  - Memorization detection
  - Redundancy filtering
  - Agent self-evaluation

---

## Design Principles

- **Diagonal Fisher only** — tractable, stable, explainable  
- **No Monte Carlo sampling** — fully deterministic  
- **Layer-selective computation** — scalable to large models  
- **Single-file implementation** — easy to audit and integrate  

---

