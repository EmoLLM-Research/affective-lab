# Affective-Lab: Research Log

This log tracks ongoing hypotheses, architectural decisions, mathematical formalizations, and community feedback for persistent affective state modeling in LLM inference loops.

---

## [Entry 001] - Initial Theoretical Framework & Baseline Design
**Date:** October 2026  
**Focus:** Establishing core state representations and homeostatic decay.

### 1. The Core Problem
Standard autoregressive LLMs are stateless across turns. Roleplay system prompts provide static behavioral hints, but fail to exhibit natural emotional inertia, fatigue, or gradual recovery over extended multi-turn interactions.

### 2. Baseline Architecture: 3D PAD Space
We adopt Mehrabian’s **Pleasure-Arousal-Dominance (PAD)** model as an initial continuous manifold bounded to $[-1, 1]$:
* **Pleasure ($P$):** Valence valence $[-1.0, 1.0]$ (Negative/Sad $\leftrightarrow$ Positive/Happy)
* **Arousal ($A$):** Energy level $[-1.0, 1.0]$ (Calm/Sleepy $\leftrightarrow$ Excited/Agitated)
* **Dominance ($D$):** Control level $[-1.0, 1.0]$ (Submissive $\leftrightarrow$ Dominant/Confident)

### 3. Temporal Homeostasis & Decay
To simulate emotional recovery, states decay exponentially back toward a resting baseline personality vector over elapsed conversation time ($t$):
$$\frac{dS}{dt} = -\lambda (S - S_{baseline}) + \Delta S_{impulse}$$
Where $\lambda$ represents the homeostatic decay rate coefficient.

---

## [Entry 002] - Mathematical Critique & High-Dimensional Extensions
**Date:** October 2026  
**Context:** Community peer review feedback from Andre Zapico (`drezaptmp`) on PyTorch forums.

### 1. Identified Limitations of 1D/3D Bounding
* Forcing complex human affect onto rigid $[-1.0, 1.0]$ unidimensional intervals or simple 3D axes can be overly reductive. Human emotion exhibits multi-dimensional, non-linear coupling rather than acting as a simple "x-axis".
* Word vector embeddings alone are often naive for capturing true conversational emotional dynamics without proper regularization.

### 2. Proposed Refinements (Hypothesis 02)
* **Latent Space Clustering & PCA Regression:** Explore unsupervised clustering or Principal Component Analysis (PCA) on high-dimensional embedding spaces mapped to specific behavioral outcomes of interest, rather than relying solely on hand-tuned PAD coordinates.
* **Out-of-Sample Validation:** Design rigorous evaluation metrics to test whether multi-turn state drift matches target trajectories without prompt degradation.

### 3. Action Items
* Benchmark the standard 3D PAD homeostatic decay model against a PCA-reduced latent state representation.
* Open collaboration channels for quantitative contributors to formalize tensor state transitions.
