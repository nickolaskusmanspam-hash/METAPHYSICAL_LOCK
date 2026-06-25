# 37 — Ϙₚ–ςₚ L‑Function Bridge & Rank Equality (Order of Vanishing)
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 35 — Ϙₚ–ςₚ MMKₚ Object & Closures | Ϙₚ projector & Selmer closure |
| 36 — Ϙₚ–ςₚ Lyapunov & Height Descent | Rank from stabilized Selmer |
| 38 — Ϙₚ–ςₚ Keystone — BSD in KUSMAN | Synthesis theorem |

---

## 1. p‑adic L‑function as MMK Measure

Inside KUSMAN, model the p‑adic L‑function as a measure \(\mathcal L_p\) on \(\mathbb Z_p^{\times}\) with Mellin transform \(L_p(E,s)\). Define a closure σ_{L_p} enforcing the interpolation property and admissibility.

**Lemma (BSDₚ‑7 — L‑closure idempotence).**  
σ_{L_p} is idempotent and commutes with σ_{Hₚ} and σ_{Sel} on the fixed sector.

---

## 2. Rank = Order of Vanishing (within Ϙₚ–ςₚ)

**Theorem (BSDₚ‑8 — Order equals stabilized Selmer dimension).**  
On the \(\Qₚ\)-fixed sector,
\[
\operatorname{ord}_{s=1} L_p(E,s) \;=\; \dim_{ℚₚ}\mathrm{Sel}_{BK}(E/ℚ; VₚE).
\tag{BSDₚ‑8}
\]

*Sketch.* σ_{L_p} ties \(L_p\) to local Galois data; σ_{Sel} pins the same data via Bloch–Kato conditions. Commutation and idempotence identify zeros with Selmer dimensions. ∎

**Proposition (BSDₚ‑9 — Leading term and regulator).**  
On the fixed sector, the leading term of \(L_p(E,s)\) at s=1 equals the p‑adic regulator times torsion and Tamagawa factors, up to a p‑adic unit in the admissibility closure.

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
