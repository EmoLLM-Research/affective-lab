
# 🧠 affective-lab

**Experimental research sandbox investigating persistent emotional state modeling, cognitive dynamics, and affective feedback loops for Large Language Models.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Active Research](https://img.shields.io/badge/Status-Active%20Research-success.svg)]()
[![Python Version](https://img.shields.io/badge/Python->=3.9-blue.svg)]()

</div>

---

## 🔬 About the Project

Standard Large Language Models are stateless autoregressive predictors—they respond to input prompts without any internal continuity of mood, emotional memory, or homeostatic recovery. **`affective-lab`** is an open-source research repository dedicated to exploring how continuous affective computing models (such as Pleasure-Arousal-Dominance vector spaces and temporal decay equations) can be integrated around LLMs to simulate persistent, realistic emotional states.

---

## 🧭 Core Research Objectives

* **Continuous Affect State Space:** Mapping emotional dimensions into mathematical coordinates $(P, A, D) \in [-1.0, 1.0]^3$.
* **Temporal Homeostasis & Decay:** Testing differential equations and exponential decay models that allow synthetic emotions to naturally return to a baseline personality over time.
* **Impulse Appraisal Pipelines:** Investigating how incoming dialogue generates emotional delta impulses $(\Delta P, \Delta A, \Delta D)$ based on semantic intent and intensity.
* **Behavioral Steering:** Evaluating how continuous state coordinates can dynamically shape prompt instructions without breaking core model alignment or reasoning capabilities.

---

## 📂 Repository Structure

```text
affective-lab/
├── notebooks/         # Jupyter notebooks for interactive prompt & mood testing
├── experiments/       # Standalone Python simulation scripts
├── data/              # Evaluation datasets and prompt test cases
├── results/           # Experimental logs, charts, and output samples
└── RESEARCH_LOG.md    # Active lab notebook tracking daily hypotheses and findings
```

🧮 Mathematical Framework (PAD Model)We ground our affective simulations in Mehrabian's PAD Emotional Model:Pleasure ($P$): Valence (Negative/Pain vs. Positive/Joy)Arousal ($A$): Energy level (Calm vs. Excited/Agitated)Dominance ($D$): Control/Confidence (Submissive vs. In Control)States evolve dynamically across interaction turns using exponential decay toward a resting baseline personality vector $(P_0, A_0, D_0)$ over elapsed time.

🚀 Getting StartedClone the repository and explore the experimental notebooks:Bashgit clone [https://github.com/YourOrg/affective-lab.git](https://github.com/YourOrg/affective-lab.git)
cd affective-lab
