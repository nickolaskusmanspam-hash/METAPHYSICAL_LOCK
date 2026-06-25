# 28 — #Ϙ Pushforward & Additivity (Σ_{Ϙ}, Π_{Ϙ} Operators)
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 27 — #Ϙ Multiplicity & Fibers | μ(x′) well‑defined and poly‑bounded |
| 29 — #Ϙ Polynomial Enumeration | Σ_{Ϙ} μ computable in poly‑time |
| 15–17 | Canonical quotient, Lyapunov, polynomial state space |

---

## 1. Operators on the Quotient

Let \(\mathcal{F}(S_{Ϙ}(I))\) denote functions \(f: S_{Ϙ}(I) 	o \mathbb{R}_{\ge 0}\). Define the **additive pushforward**
\[
Σ_{Ϙ}(f) \;:=\; \sum_{x' \in S_{Ϙ}(I)} f(x'),
	ag{#Ϙ 5}
\]
and, when products are meaningful (independent components), define the **multiplicative aggregator**
\[
Π_{Ϙ}(f) \;:=\; \prod_{x' \in S_{Ϙ}(I)} f(x').
	ag{#Ϙ 6}
\]

**Remark.** For #P‑style counting we use \(f=\mu\) on accepting classes; for product‑structured counts (e.g., independent components), we use \(Π_{Ϙ}\).

---

## 2. Functoriality and Commutation

Let \(K\) be the NEAM transition kernel on raw states and \(K_{Ϙ}\) its induced kernel on the quotient.

**Lemma ( #Ϙ 7 — Commutation with closure).**
For any \(f \in \mathcal{F}(S_{Ϙ})\) and any step,
\[
Σ_{Ϙ}ig( K_{Ϙ} f ig) \;=\; Σ_{Ϙ}(f),
\quad
	ext{and}\quad
Π_{Ϙ}ig( K_{Ϙ} f ig) \;=\; Π_{Ϙ}(f)
	ag{#Ϙ 7}
\]
whenever \(K\) is measure‑preserving on fibers and branching is resolved by Ϙ (congruence).

*Sketch.* Each raw transition partitions into fiber transitions that biject under transport (Sheet 15), so the sum/product over classes is invariant. ∎

**Proposition ( #Ϙ 8 — Additivity with multiplicity).**
For the multiplicity measure \(\mu\) of Sheet 27 and any disjoint partition \(S_{Ϙ} = A \sqcup B\),
\[
Σ_{Ϙ}(\mu) \;=\; Σ_{A}(\mu) + Σ_{B}(\mu).
	ag{#Ϙ 8}
\]

Trivial from the definition (finite sum over a disjoint union).

---

## 3. Acceptance Filtering

Let \(Acc \subseteq S_{Ϙ}(I)\) be the set of accepting classes. Define \( \mu_{Acc}(x') = \mu(x') \cdot \mathbf{1}_{Acc}(x')\).

**Lemma ( #Ϙ 9 — Quotient acceptance).**
If acceptance is defined by local syntactic conditions preserved by Ϙ, then \(Acc\) is a union of Ϙ‑classes and
\[
\#f(I) \;=\; Σ_{Ϙ}(\mu_{Acc}).
	ag{#Ϙ 9}
\]

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
