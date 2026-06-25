# 27 — #Ϙ Multiplicity Measure & Fiber Structure (Counting in the Ϙ–ς Quotient)
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 15 — Ϙ–ς_MN_Canonical_Quotient | Canonical labeling and literal transport π |
| 16 — Ϙ–ς_Lyap_Lyapunov_and_Progress | Lyapunov & branch‑or‑simplify progress |
| 17 — Ϙ–ς_Poly-States_Polynomial_State_Space | Polynomial bound on Ϙ‑classes |

---

## 1. Setup and Definitions

Let \(I\) be an input of size \(n\). Let \(S(I)\) be the set of **reachable raw solver states** under NEAM steps and Ϙ‑closure, and let \(S_{Ϙ}(I)\) be the set of **Ϙ‑classes** (Sheet 17). Denote the canonical projection \(p: S(I) 	o S_{Ϙ}(I)\).

**Definition ( #Ϙ multiplicity on the quotient).**
For \(x' \in S_{Ϙ}(I)\), define the **multiplicity measure**
\[
\mu(x') \;:=\; \#\{\, x \in S(I) : p(x)=x' \,\}.
	ag{#Ϙ 1}
\]

When counting witnesses (e.g., #SAT), we restrict \(S(I)\) to states consistent with acceptance and keep the same definition.

---

## 2. Fiber Structure and Bounds

**Lemma ( #Ϙ 2 — Fiber decomposition under transport).**
If \(x' \in S_{Ϙ}(I)\) has canonical representative \(\widehat x\) (Sheet 15), then every fiber element \(x\in p^{-1}(x')\) is obtained by composing \(\widehat x\) with a literal‑transport bijection \(\pi\) that respects width and polarity. Moreover, all such \(\pi\) are determined by the canonical labeling \(L\) in \(n^{O(1)}\) time.

*Sketch.* Direct from Sheet 15’s transport and congruence lemmas; each raw state canonicalizes to \(\widehat x\) with an induced \(\pi\). ∎

**Proposition ( #Ϙ 3 — Polynomial fiber bound).**
For fixed constants \((k_0,r)\) and precision \(b=\Theta(\log n)\), there exists a polynomial \(p\) such that \(\mu(x') \le p(n)\) for all \(x' \in S_{Ϙ}(I)\).

*Sketch.* Each raw trajectory is a sequence of at most \(n^{O(1)}\) steps (Sheet 16: strict Lyapunov descent). At each step, bounded‑width moves generate at most \(n^{O(1)}\) distinct raw successors that collapse to the same quotient class by canonicalization (Sheet 15). Multiply the polynomial step and branching bounds to get a polynomial fiber bound. ∎

---

## 3. Computability of μ

**Theorem ( #Ϙ 4 — Polynomial‑time multiplicity evaluation).**
There is an \(n^{O(1)}\)‑time algorithm that, given \(x' \in S_{Ϙ}(I)\), computes \(\mu(x')\).

*Sketch (DP on the quotient).* Build the finite transition system on \(S_{Ϙ}(I)\) (Sheet 17). For each edge \(x' 	o y'\), compute the number of raw lifts using the canonical transport maps; dynamic‑program over a topological order induced by the Lyapunov potential (no positive cycles by Sheet 16). Summing contributions yields \(\mu(x')\). ∎

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
