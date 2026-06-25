# 35 — Ϙₚ–ςₚ MMKₚ Object & p-adic Closures (BSD Setup)
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 36 — Ϙₚ–ςₚ Lyapunov & Height Descent | Rank/defect descent under Ϙₚ |
| 37 — Ϙₚ–ςₚ L‑Function Bridge & Rank Equality | Order‑of‑vanishing equals rank |
| 38 — Ϙₚ–ςₚ Keystone — BSD in KUSMAN | Synthesis theorem |

---

## 1. MMKₚ Objects (Elliptic Curve over ℚ)

Fix a prime p and an elliptic curve E/ℚ with minimal Weierstrass model.

- **Local state space**: |Xₚ| = E(ℚₚ) × H¹_f(ℚₚ, VₚE), with VₚE the p‑adic Tate module tensored with ℚₚ.  
- **Measure**: μₚ = Haar on E(ℚₚ) × Gaussian on the linear space H¹_f.  
- **Kernel**: Kₚ = one NEAM step combining (i) group update P ↦ P+Q for Q in a fixed generating set; (ii) local cohomology update by functoriality.  
- **Metric**: dₚ from the p‑adic norm on coordinates and linear norm on H¹_f.

**Global object (restricted product)**: |X| = ∏′_ℓ |X_ℓ| with product kernel K and measure μ = ∏′ μ_ℓ; we focus on the p‑factor and suppress others into admissibility conditions.

---

## 2. Ϙₚ–ςₚ Closures

Define the composite p‑adic closure
\[
\Qₚ = σ_{Hₚ} \circ σ_{Sel} \circ σ_{alg} \circ σ_{ℓₚ},
\]
with:
- **σ_{Hₚ} (p‑adic Hodge/De Rham projector)**: projection to the crystalline/de Rham subspace respecting the Hodge filtration on VₚE.  
- **σ_{Sel} (Selmer closure)**: imposes Bloch–Kato local conditions (finite at all ℓ, crystalline at p), collapsing to the Bloch–Kato Selmer group \(\mathrm{Sel}_{BK}(E/ℚ; VₚE)\).  
- **σ_{alg} (algebraic closure)**: closure under rational points, isogenies, and endomorphisms of E; acts on both E(ℚₚ) and H¹ spaces via functoriality.  
- **σ_{ℓₚ} (admissibility)**: bounds conductor and local denominators; enforces integrality where needed.

**Lemma (BSDₚ‑1 — Idempotence & Commutation).**  
Each σ_* is idempotent; on their natural sublattices they commute. Hence \(\Qₚ^2=\Qₚ\) and is order‑independent (Ϙ–ς stability).

**Proposition (BSDₚ‑2 — Fixed‑sector Identification).**  
The \(\Qₚ\)-fixed sector identifies canonically with \(E(ℚ) \otimes ℚₚ\) paired with \(\mathrm{Sel}_{BK}(E/ℚ; VₚE)\) via the p‑adic Kummer map inside the MMKₚ object.

---

## 3. Spectral Contraction at p

**Proposition (BSDₚ‑3 — Local spectral contraction).**  
Under \(Kₚ\) followed by \(σ_{Hₚ}\), non‑crystalline (non‑de Rham) components decay in norm; thus \(σ_{Hₚ}\) acts as a projector with Lyapunov decrease on the orthogonal complement.

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
