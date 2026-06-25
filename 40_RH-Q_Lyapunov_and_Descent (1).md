# 40 — RH–Ϙ Lyapunov & Descent (Critical-Line Projection)
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 39 — RH–Ϙ MMK & Closures | Q definition and FE decomposition |
| 41 — RH–Ϙ Fixed‑Set Characterization | Line‑supported tests; Weil positivity |
| 42 — RH–Ϙ Keystone Resolution | Synthesis theorem |

---

## 1. Potential

Let
Ψ(φ) = ||W(φ)||_2^2 + α || ˆφ_⊥ ||_2^2 + β || φ − σ_Weil+ φ ||_2^2,  with α,β>0,
where ˆφ_⊥ denotes Fourier mass off the critical line component induced by σ_HP.

---

## 2. One‑Step Descent

**Theorem (RHϘ‑3 — Lyapunov drop under Q ∘ K_ε).**  
For sufficiently small ε and suitable α,β, there exists γ>0 such that
Ψ( Q ∘ K_ε(φ) ) ≤ Ψ(φ) − γ ⋅ ( || ˆφ_⊥ ||_2^2 + || φ − σ_Weil+ φ ||_2^2 ),
with equality iff φ lies in the Q‑fixed sector.

*Sketch.* K_ε reduces ||W(φ)||_2 (smoothing) and preserves FE symmetry; σ_HP annihilates off‑line mass; σ_Weil+ projects to the positivity cone; σ_Had normalizes without increasing Ψ. ∎

**Corollary (RHϘ‑4 — Finite stabilization).**  
If im(Ψ) is quantized (DMR) or there is a uniform drift gap, iterates of Q ∘ K_ε stabilize in finitely many steps at a Q‑fixed φ*.

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
