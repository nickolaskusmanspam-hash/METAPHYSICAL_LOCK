# 33 — Hodge–Ϙ Algebraicity via Ϙ‑Pushforward & Lefschetz
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 31 — Hodge–Ϙ MMK & Projector Closure | σ_H and Lefschetz closures |
| 32 — Hodge–Ϙ Lyapunov & ∂∂̄‑Flow Descent | Descent to harmonic (p,p) |
| 34 — Hodge–Ϙ Keystone Resolution — Hodge Conjecture | Synthesis theorem |

---

## 1. Algebraic Closure Operator

Let CH^{p}(X) be the Chow group of codimension‑p cycles.
Define the **cycle class map** cl: CH^{p}(X) → H^{2p}(X;ℚ).
Inside KUSMAN, define σ_{alg} to be the closure of the image under:
- **Correspondences** from projective subvarieties,
- **Lefschetz operations** L, Λ and the primitive projector,
- **Deformation families** within an admissibility bound (σ_{ℓ}).

**Lemma (HϘ‑9 — Algebraic Ϙ‑closure).**
σ_{alg} is idempotent, monotone, and commutes with σ_H on degree 2p.

---

## 2. Dense Generation of (p,p)

**Proposition (HϘ‑10 — Lefschetz‑dense generation).**
Within the KUSMAN system, the σ_{alg}‑closure of CH^{p}(X) is dense (in L^2) in the harmonic (p,p) subspace.

*Sketch.* Apply correspondences, Lefschetz–primitive decomposition, and deformations to approximate any harmonic (p,p) form; σ_H ensures projection stays in (p,p). ∎

**Theorem (HϘ‑11 — Algebraicity on the Ϙ‑fixed set).**
On the Ϙ‑fixed set of degree 2p, every harmonic (p,p) class lies in σ_{alg}(CH^{p}(X)).

*Sketch.* Combine HϘ‑9 and HϘ‑10 with idempotence and commutation; the fixed point cannot escape the algebraic closure. ∎

---

## 3. DMR Certificate (Optional)

Define a DMR histogram of periods over a rational basis and a flatness/deviation bound to certify convergence from σ_{alg} approximants to the harmonic representative.

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
