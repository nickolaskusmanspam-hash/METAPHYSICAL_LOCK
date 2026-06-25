# 36 — Ϙₚ–ςₚ Lyapunov & Height Descent (Rank via Ϙₚ)
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 35 — Ϙₚ–ςₚ MMKₚ Object & Closures | Ϙₚ definition and fixed sector |
| 37 — Ϙₚ–ςₚ L‑Function Bridge & Rank Equality | Order‑of‑vanishing equals rank |
| 38 — Ϙₚ–ςₚ Keystone — BSD in KUSMAN | Synthesis theorem |

---

## 1. Potential and Defect

Let \(\hat h\) be the Néron–Tate height on E(ℚ) extended p‑adically, and let \(\mathrm{rk}\) denote the ℚ‑rank. Define the **defect triple**
\[
\mathrm{def}_p = \big( R_p,\; D_p,\; S_p \big),
\]
where:
- \(R_p\): p‑adic regulator (determinant on a basis of independent points),  
- \(D_p\): Selmer defect = \(\dim_{ℚₚ}\mathrm{Sel}_{BK}(E/ℚ; VₚE) - \mathrm{rk}\),  
- \(S_p\): local obstruction mass (sum of deviations from BK local conditions).

Define the Lyapunov potential
\[
Ψ_p = a\,R_p + b\,D_p + c\,S_p, \quad a,b,c>0.
\tag{BSDₚ‑4}
\]

---

## 2. One‑Step Descent

**Theorem (BSDₚ‑5 — Height/Selmer descent under Ϙₚ).**  
For suitable weights a,b,c and small step size in the NEAM kernel, there exists \(\gamma>0\) such that
\[
Ψ_p\big( \Qₚ \circ K (x) \big) \le Ψ_p(x) - \gamma \cdot \big( D_p(x) + S_p(x) \big),
\tag{BSDₚ‑5}
\]
with equality only on the \(\Qₚ\)-fixed sector.

*Sketch.* σ_{Sel} removes local obstructions (drops S_p), σ_{Hₚ} contracts non‑de Rham components, and σ_{alg} aligns generators to reduce D_p once independence is achieved; weights absorb cross‑terms. ∎

**Corollary (BSDₚ‑6 — Finite stabilization & rank extraction).**  
By Ϙ–ς Lyapunov theory, iteration stabilizes in finitely many steps (or in bounded time in the continuous limit) to the \(\Qₚ\)-fixed sector where \(D_p=0\). The stabilized rank equals \(\dim_{ℚₚ}\mathrm{Sel}_{BK}(E/ℚ; VₚE)\).

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
