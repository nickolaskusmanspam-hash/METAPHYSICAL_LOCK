# 23 — YM–Ϙ_Spectral_Pinching_and_Energy_Descent (Lattice SU(N))
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 24 — YM–Ϙ_Finite_Time_Stabilization | Ϙ–Lyapunov descent ⇒ stabilization |
| 25 — YM–Ϙ_Continuum_Limit_and_Mass_Gap | Vanishing spacing ⇒ mass gap |

---

## 1. MMK / Ϙ–ς Objects and Notation

- **Lattice:** 4D hypercubic with spacing a, sites x, oriented links (x,μ).  
- **Configuration space:** |X| = Π_{links} SU(N), equipped with product Haar and Wilson action measure.  
- **Kernel K:** one update step (heat‑bath / over‑relax) viewed as a Markov kernel on |X|.  
- **Observables:** plaquette energy E_plaq(U) = Σ_□ (1 − (1/N) Re Tr U_□); gauge‑covariant Laplacian spectrum {λ_k(U)}.  
- **Ϙ–ς closure:** Q = σ_c ∘ σ_s ∘ σ_a ∘ σ_ℓ with  
  σ_c: center projection (Z_N sector),  
  σ_s: spectral pinching (truncate/pinch high eigenmodes of link operators),  
  σ_a: axial gauge normalization,  
  σ_ℓ: admissibility (|1 − (1/N) Re Tr U_□| ≤ ε).  
Idempotence Q^2 = Q and commutativity of σ_i are assumed as per Ϙ–ς Stability.

---

## 2. Pinching Widening of the Infrared Gap

**Lemma (YM–Ϙ 1 — Spectral Pinching Inequality).**  
For admissible U, let Δ(U) = λ_1(U) − λ_0(U) > 0 denote the first non‑trivial spectral gap of the transfer/Laplacian operator. Then
\[
Δ(σ_s U) \ge Δ(U) + c_p \cdot \, \mathcal P_{\!>Λ}(U),
\tag{{YM–Ϙ 1}}
\]
where \(\mathcal P_{\!>Λ}(U)\) quantifies the high‑mode weight beyond Λ and c_p>0 depends only on the pinching profile.

*Sketch (within KUSMAN).* σ_s annihilates/attenuates high modes and therefore raises the Rayleigh quotient of any vector orthogonal to the ground space. Quantization ensures monotone increase of Δ. ∎

---

## 3. Center Projection and Expected Energy Descent

**Lemma (YM–Ϙ 2 — Center‑Projected Energy Descent).**  
For Q‑admissible U,
\[
\mathbb E\big[ E_\text{plaq}(σ_c ∘ K(U)) \mid U \big] \le E_\text{plaq}(U) - c_c \, \Xi(U),
\tag{{YM–Ϙ 2}}
\]
with c_c>0 and \(\Xi(U)\) a non‑negative functional vanishing only on center‑aligned sectors.

*Sketch.* Heat‑bath/over‑relax updates decrease the action in expectation; σ_c removes center fluctuations, producing a uniform decrement unless already centered. ∎

---

## 4. Ϙ–Lyapunov Descent in One Step

Define the potential
\[
Ψ(U) = E_\text{plaq}(U) + α \, Δ(U)^{-1}, \quad α>0.
\tag{{YM–Ϙ 3}}
\]

**Theorem (YM–Ϙ 3 — One‑Step Ϙ–Descent).**  
There exist constants α,γ>0 such that for all Q‑admissible U,
\[
\mathbb E\big[ Ψ(Q ∘ K(U)) \mid U \big] \le Ψ(U) - γ \, Δ(U)^{-1}.
\tag{{YM–Ϙ 4}}
\]

*Sketch.* Combine (YM–Ϙ 1) to control Δ^{-1} via pinching and (YM–Ϙ 2) to decrease E_plaq in expectation. Choose α to absorb cross‑terms; Ϙ–ς Lyapunov equivalence yields strict decrease off the Q‑fixed set. ∎

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
