Here’s the **final, concise, fully technical README** ready for GitHub — copy-paste, minimal, scientific, PhD-rigorous:

---

### **README.md**

````markdown
# Identity-Geometry

Lightweight Python library for **Fisher-Rao information geometry** and **rational inattention-inspired novelty scoring** of LLM outputs.

## Installation

```bash
pip install git+https://github.com/yourname/identity-geometry.git
````

## Overview

* **FisherInfo**: diagonal Fisher trace of model loss w.r.t parameters.
* **KLDivergence**: KL(p || uniform) on last-token softmax outputs.
* **NoveltyFunctional**: heuristic novelty score combining KL and token-length attention proxy:

[
\text{Novelty}(x) = \frac{\mathrm{KL}(\text{softmax}(logits_x) \parallel \text{uniform})}{n_\text{tokens}/\text{normalizer} + 0.1}
]

## Usage

```python
from identity_geometry import NoveltyFunctional
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "facebook/opt-125m"
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)

nov = NoveltyFunctional()
text = "Quantum entanglement was first discussed in 1935."
score = nov.compute(text, model, tokenizer)
print(score)
```

## Configuration

* `FisherConfig`: method, num_samples, batch_size, device
* `KLConfig`: epsilon, prior_temperature
* `NoveltyConfig`: fisher, kl, attention_normalizer

## Notes

* Minimal research-grade implementation: **diagonal Fisher only, KL vs uniform**.
* Device-aware (`cuda` if available).
* Fully typed, modular, pip-installable.
* Intended for **reproducible experiments on LLM novelty**.

**License:** Apache 2.0

```

