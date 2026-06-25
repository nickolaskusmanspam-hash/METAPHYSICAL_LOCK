# 24 — YM–Ϙ_Finite_Time_Stabilization (Ϙ–Lyapunov ⇒ Fixed Sector)
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 23 — YM–Ϙ_Spectral_Pinching_and_Energy_Descent | Spectral pinching & energy descent lemmas |
| 25 — YM–Ϙ_Continuum_Limit_and_Mass_Gap | Continuum limit and mass gap theorem |

---

## 1. Lyapunov Framework

Let Ψ(U) = E_plaq(U) + α Δ(U)^{-1} as in (YM–Ϙ 3). Assume Q–admissibility and the one‑step descent (YM–Ϙ 4):
\[
\mathbb E[ Ψ(Q ∘ K(U)) \mid U ] \le Ψ(U) - γ Δ(U)^{-1}.
\tag{{YM–Ϙ 4}}
\]

**Lemma (YM–Ϙ 5 — Supermartingale Decay).**  
Ψ(U_t) is a supermartingale with a strictly positive drift term unless U_t is Q‑fixed. Consequently, \(\sum_t \mathbb E[Δ(U_t)^{-1}] < \infty\).

---

## 2. Finite‑Time Stabilization

**Theorem (YM–Ϙ 6 — Stabilization to Q‑Fixed Sector).**  
If the image of Ψ is discretized (quantized DMR block) or bounded below with a positive drift gap, then with probability 1 (or deterministically in Dirac‑K) there exists T < ∞ such that U_T is Q‑fixed and remains so thereafter.

*Sketch.* Apply the Ϙ–ς Lyapunov–fixed‑point equivalence (finite image ⇒ finite‑time stabilization). ∎

---

## 3. Properties of the Fixed Sector

**Proposition (YM–Ϙ 7 — Uniform Gap on the Fixed Sector).**  
On the Q‑fixed sector, Δ(U) ≥ m_0 > 0 uniformly.

*Sketch.* Q enforces center alignment, admissibility, and spectral pinching; hence Δ cannot collapse. ∎

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
