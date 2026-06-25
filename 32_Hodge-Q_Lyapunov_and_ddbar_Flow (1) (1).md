# 32 — Hodge–Ϙ Lyapunov & ∂∂̄‑Flow Descent
**Version:** 1.0  
**Date:** 2025-10-08  
**Series:** KUSMAN Framework — Core Verification Series v1.6

---

## Cross‑References
| Sheet | Purpose |
|:--|:--|
| 31 — Hodge–Ϙ MMK & Projector Closure | Hodge projector σ_H and Ϙ idempotence |
| 33 — Hodge–Ϙ Algebraicity via Ϙ‑Pushforward & Lefschetz | Algebraic closure to (p,p) classes |
| 34 — Hodge–Ϙ Keystone Resolution — Hodge Conjecture | Synthesis theorem |

---

## 1. Potential and Flow

Fix degree 2p. For a closed class [α] ∈ H^{2p}(X;ℝ), choose any representative α.
Define the Lyapunov potential
\[
Ψ_{p}(α) = \| (α)_{⊥}^{(p,p)} \|_{L^2}^2 + βig( \|∂α\|_{L^2}^2 + \| ar∂ α\|_{L^2}^2 ig), \quad β>0.
	ag{HϘ‑5}
\]
Let Φ_t be either the heat flow K_t or a ∂∂̄‑flow on degree 2p forms.

**Theorem (HϘ‑6 — Lyapunov–Ϙ descent).**
For suitable β and small t>0,
\[
Ψ_{p}( \Q ∘ Φ_t(α) ) \le Ψ_{p}(α),
\quad 	ext{with strict inequality unless } α 	ext{ is Ϙ‑fixed in } (p,p).
	ag{HϘ‑6}
\]

*Sketch.* σ_H removes non‑harmonic content; σ_{alg}, σ_{top}, σ_{ℓ} preserve (p,p) and admissibility. Orthogonal projection drops the ⊥‑component; flow reduces ∂, ar∂ norms. ∎

**Corollary (HϘ‑7 — Finite stabilization).**
If im(Ψ_p) is quantized (DMR) or bounded below with a positive drift gap, then the iteration of \Q∘Φ_t stabilizes in finitely many steps at a harmonic (p,p) fixed point representing [α].

---

## 2. Transport‑Invariance

**Lemma (HϘ‑8 — Transport invariance).**
If two representatives are Ϙ‑equivalent, their Ψ_p values agree; descent is well‑defined on Ϙ‑classes.

---

**Footer:**  
— KUSMAN Framework — Core Verification Series v1.6
