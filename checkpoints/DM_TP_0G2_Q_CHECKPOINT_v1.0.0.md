# DM-TP-0G2-Q — Pati–Salam breaking spectrum and Phi-visible connector provenance gate

**Version:** v1.0.0  
**Status:** FROZEN CHECKPOINT  
**DM abundance used:** NO  
**New DM normalization introduced:** NO  
**Historical H8 / `Lambda_mem` used:** NO  
**DE quantities refit:** NO  
**Theorem SHA-256:** `6bdc9e911cc2ca3b0c462d287cb209e87f405bb696fa714cde0b9a7be9430ac7`

## Executive verdict

\[
\boxed{\text{visible Pati-Salam thermalization capacity: ROBUST PASS}}
\]

\[
\boxed{\text{complete PS-breaking spectrum from frozen Phase B2: HARD NO-PASS}}
\]

\[
\boxed{\text{derived post-handoff Phi-visible connector: NO-PASS}}
\]

\[
\boxed{\text{pure gravitational common-bath thermalization: HARD NO-PASS}}
\]

\[
\boxed{\textbf{DM-TP-0G2-Q = UV/INTERFACE PROVENANCE STOP}}
\]

0G2 reaches the clean stop rule for first-principles heavy-q abundance under the current frozen architecture. The Pati-Salam gauge sector can thermalize itself, and the Phi sector can thermalize itself once loaded. What the frozen theory does not contain is a unique bridge fixing their common thermal state and the full Pati-Salam breaking spectrum.

This is not a dark-particle failure. It is an upstream action-completeness/interface failure.

---

## 1. Pati-Salam gauge matching is not the main blocker

Phase B2 already carries minimal one-loop Pati-Salam running inputs at

\[
\Lambda_{\rm seed}=2.4100\times10^{14}\ {\rm GeV}.
\]

At the target-blind handoff thermal-capacity control

\[
T=3.216308037410e+13\ {\rm GeV},
\]

the inherited minimal-running values give approximately

\[
g_4=0.607043249,\qquad g_R=0.527994319.
\]

Using the later enlarged-field-content beta-function control gives

\[
g_4=0.600493907,\qquad g_R=0.520042855.
\]

The numerical variation is modest enough that the visible sector remains strongly interacting on a Hubble time in either branch.

For the schematic gauge rate

\[
\Gamma_{\rm gauge}\sim\kappa\alpha^2T,
\]

the explicit controls are

\[
(\Gamma/H)_{g_4,\kappa=1}=16.914973,
\qquad
(\Gamma/H)_{g_R,\kappa=1}=9.680767,
\]

and even with an order-ten suppression of the rate coefficient,

\[
(\Gamma/H)_{g_4,\kappa=0.1}=1.619672,
\qquad
(\Gamma/H)_{g_R,\kappa=0.1}=0.911065.
\]

Thus the visible Pati-Salam plasma can self-thermalize comfortably.

The missing theorem is not “are the gauge interactions strong enough?”

---

## 2. Complete Pati-Salam breaking cannot be derived from Phase B2

The frozen Phase-B2 repository contains the gauge/flavor architecture and a complex \((1,2,2)\) bidoublet, but not the complete Pati-Salam breaking Higgs sector or its vacuum.

A previous explicit completion used fields such as

\[
\Sigma_C\sim(15,1,1),\qquad
\Delta_R\sim(1,1,3),\qquad
H_R\sim(4,1,2),
\]

but that audit explicitly classified the fields, their scalar potential, VEVs and Yukawa coefficients as **new structural inputs**, not consequences of Phase B2.

Later scalar-completion work made the non-uniqueness even sharper: the full allowed scalar action contains a large coefficient family, and the zero-temperature symmetry data do not select one thermal history. The complete threshold generator can be written symbolically, but the masses and transition trajectory cannot be evaluated without choosing unfrozen coefficients.

Therefore there is no unique action-derived list

\[
\{m_i(T),g_i,T_i\}
\]

and consequently no unique

\[
g_*(T),\qquad g_{*s}(T).
\]

This is a hard provenance stop, not a numerical inconvenience.

---

## 3. The Phi-visible connector is not fixed

The frozen common action retains the Pati-Salam gauge kinetic structure schematically as

\[
-\frac14\sum_a Z_a(\Phi,\phi)F^a_{MN}F^{aMN},
\]

but the post-handoff field derivatives/normalizations of the functions \(Z_a\) are not fixed as a numerical interaction capable of yielding a definite Phi-visible energy-exchange rate.

The later explicit Pati-Salam scalar action also states that no direct renormalizable portal between the immutable bounce scalars and the Pati-Salam scalar basis is authorized at tree level.

Therefore the current action does not calculate

\[
\Gamma_{\Phi\leftrightarrow{\rm vis}}.
\]

Capacity diagnostics show that a modest connector would be sufficient:

\[
\lambda_{\rm eq}\sim0.035745
\]

for a generic renormalizable interaction, or

\[
c_{\rm eq}\sim0.196863
\]

for a dimension-five \(\sigma F^2/F\)-type operator.

But these are required values, not action-derived coefficients.

---

## 4. Gravity cannot replace the missing connector

A purely gravitational relativistic scattering rate scales parametrically as

\[
\Gamma_{\rm grav}\sim\frac{T^5}{M_4^4}.
\]

Relative to radiation-era expansion,

\[
\frac{\Gamma_{\rm grav}}H
\sim O(1)\left(\frac{T}{M_4}\right)^3.
\]

At the target-blind handoff control,

\[
\boxed{
\frac{\Gamma_{\rm grav}}H
\sim5.987522979150e-16 .
}
\]

This is far below unity.

Therefore universal gravitational coupling can source both sectors during the nonadiabatic handoff, but ordinary post-handoff gravity cannot thermalize them into one common bath.

\[
\boxed{\text{gravity is not the missing thermal connector}.}
\]

---

## 5. Consequence for the heavy-q abundance

The heavy-q production operator is already derived:

\[
\pi\pi,\sigma\sigma\rightarrow qq.
\]

The Phi sector has a fast internal \(\sigma\leftrightarrow\pi\pi\) equilibration capacity, and the visible Pati-Salam sector has a fast self-thermalization capacity.

But without

1. a unique handoff loading fraction,
2. a unique Phi-visible connector,
3. a unique PS-breaking threshold spectrum,

the theory cannot derive the one quantity that the exponentially sensitive freeze-in integral requires:

\[
f_{\Phi}(p,t),\quad f_{\rm vis}(p,t)
\]

or their thermal reduction \(T_\Phi(t),T_{\rm vis}(t)\).

Therefore 0G2 does not authorize another abundance rerun. Selecting one spectrum or temperature history because it reproduces the holdout would be tuning.

---

# 6. Your N_star / Lambda_mem suspicion

This checkpoint gives a fairly clean answer.

## N_star

Your instinct about \(N_\star\) is **directionally right**, but the important object is not merely the number

\[
N_\star=57.8401844744.
\]

The frozen two-phase DE theory explicitly lists **deriving \(N_\star\) from a global/material-flow/reconstruction trigger** and **deriving the exact handoff energy partition/reheating** as separate future priorities.

However, physically they may be two outputs of the same missing handoff dynamics.

If a future material-flow theorem derives the condition

\[
{\cal C}_{\rm handoff}[{\rm screen,bulk,matter}]=0
\]

that selects \(N_\star\), that same theorem could also fix:

- the time-dependent reconstruction operator;
- the channel-resolved Bogoliubov weights;
- the release/loading fractions;
- the post-handoff sector temperatures.

So

\[
\boxed{
\textbf{deriving the mechanism that fixes }N_\star
\textbf{ may indeed be what closes q production.}
}
\]

But simply replacing the frozen numerical \(N_\star\) by a first-principles derivation of the same number would not, by itself, determine the Pati-Salam Higgs spectrum or Phi-visible connector.

## Lambda_mem

Here the answer is different.

In the frozen two-phase DE theory, historical `H8/Lambda_mem as dark energy` is explicitly retired. `Lambda_mem` belongs to the separate historical DM/memory reconstruction sector and remains an unresolved composite spectral stiffness.

It does not enter:

- the heavy-q mass;
- the `g P^2q^2` production portal;
- the Pati-Salam gauge couplings;
- the PS-breaking scalar spectrum;
- the Phi-visible thermal connector;
- the q freeze-in Boltzmann kernel.

Therefore

\[
\boxed{
\textbf{deriving historical }\Lambda_{\rm mem}
\textbf{ is not required for the heavy-q abundance route.}
}
\]

If by “lambda_mem of the DE derivation” the intended quantity was instead the late DE scale \(L_{\rm IR}\), the conclusion is similar: \(L_{\rm IR}\) controls the deep-IR late geometry, not the \(10^{13}\)-GeV handoff thermal partition.

---

## 7. Scoped no-go theorem

Under the currently frozen two-phase + Phase-B2 action:

1. the high-temperature Pati-Salam breaking spectrum is not uniquely fixed;
2. the Phi-visible post-handoff energy-exchange coefficient is not uniquely fixed;
3. gravity cannot establish the missing common bath;
4. the handoff channel partition is explicitly unfrozen.

Therefore

\[
\boxed{
\textbf{no unique absolute heavy-q yield follows from the current frozen action.}
}
\]

This is a scoped no-go for **first-principles abundance at the present action freeze**. It is not a no-go for the heavy-q particle or for the portal-freeze-in mechanism.

---

## 8. Final DM classification

The strongest honest endpoint is now

\[
\boxed{
\textbf{DERIVED: }
q\text{ existence, mass, }Z_2\text{ stability, coldness, collisionless structure,
and production operator}
}
\]

plus

\[
\boxed{
\textbf{CONDITIONAL: one universal handoff occupation/yield }Y_q.
}
\]

The heavy-q branch therefore remains the preferred conditional DM completion of the frozen two-phase cosmology.

---

## 9. Recommended disposition

I do **not** recommend another DM-specific repair checkpoint immediately.

The unresolved object is upstream:

\[
\boxed{
\textbf{the physical }2+1\rightarrow3+1
\textbf{ handoff/material-flow theorem.}
}
\]

That is exactly the natural target of the separate DE-flow derivation program.

A future handoff theorem should be required to predict, without using DM:

- \(N_\star\);
- the handoff temporal operator;
- absolute energy loading/partition;
- whether visible and Phi sectors share a bath;
- the relevant reconstruction/thermal connector.

If that upstream project closes these quantities, DM-TP should re-enter at 0G with the heavy-q portal kernel already frozen and perform one final blind abundance prediction.

Until then, further Pati-Salam completion chosen inside DM-TP would add UV structure specifically to repair an abundance target and would weaken the model rather than strengthen it.
