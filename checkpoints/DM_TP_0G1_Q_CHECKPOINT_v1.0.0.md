# DM-TP-0G1-Q — handoff loading, thermalization and active-DOF theorem gate

**Version:** v1.0.0  
**Status:** FROZEN CHECKPOINT  
**DM abundance used to select loading / thermal state / DOF content:** NO  
**New dark normalization introduced:** NO  
**Historical H8 / `Lambda_mem` used:** NO  
**DE quantities refit:** NO  
**Pre-abundance-consequence theorem hash:** `083f41b772c8788683a57f7f0a221aa226d202f333293e19f137e0ba1b926f47`

## Executive verdict

\[
\boxed{\text{Phi-sector internal equilibration once loaded: PASS / STRONG CONDITIONAL}}
\]

\[
\boxed{\text{visible-sector self-thermalization: CONTROLLED CONDITIONAL PASS}}
\]

\[
\boxed{\text{visible-Phi common-temperature theorem: NO-PASS}}
\]

\[
\boxed{\text{absolute handoff loading theorem: NO-PASS}}
\]

\[
\boxed{\text{threshold-complete Pati-Salam }g_*(T),g_{*s}(T)\text{: NO-PASS}}
\]

\[
\boxed{\textbf{DM-TP-0G1-Q = THERMALIZATION-CAPACITY PASS / UNIQUE THERMAL-STATE NO-PASS}}
\]

The existing theory can thermalize the relevant sectors **if** the appropriate energy and connector are present. What is not yet derived is the interface theorem that says how much handoff energy goes into each sector and whether the visible Pati-Salam plasma and the `Phi` sector share one temperature.

## 1. Absolute loading remains open

The two-phase handoff has the universal geometric source

\[
\delta H=\frac12\int d^3x\sqrt{\gamma}\,\delta\gamma_{\mu\nu}T^{\mu\nu},
\]

and an open post-handoff continuum. This proves accessibility of stress-carrying visible channels, but the frozen handoff audit explicitly leaves the channel-resolved Bogoliubov/energy partition undetermined. It therefore does not derive one exact reheating efficiency or one exact equality between the inherited amplitude-energy capacity and a thermal bath energy.

**Absolute loading: NO-PASS.**

## 2. Field-content audit of the 0G common-bath row

The Pati-Salam gauge algebra contains 21 vectors. Three visible families in

\[
(4,2,1)\oplus(\bar4,1,2)
\]

give 48 Weyl fields.

The older unified-action audit also states that Phase B2 contains a **complex** \((1,2,2)\) bidoublet in its minimal running content. If thermally active, this contributes

\[
\boxed{8\ {\rm real\ scalar\ degrees\ of\ freedom}},
\]

not the four real scalars used in the illustrative 0G common-bath row.

More importantly, the complete Pati-Salam-breaking Higgs sector and its mass thresholds are not frozen in Phase B2. An older explicit breaking completion introduced additional multiplets and VEVs as new structural assumptions.

Therefore the active high-temperature spectrum is not uniquely fixed.

**Threshold-complete `g_*(T),g_*s(T)`: NO-PASS.**

## 3. Target-blind bidoublet capacity control

If the complex bidoublet is active, while all other 0G common-bath assumptions are retained, the relativistic baseline is

\[
42_{\rm gauge}+84_{\rm Weyl}+8_{\rm bidoublet}+1_\pi=135.
\]

Including the thermally suppressed radial mode and using the inherited amplitude-energy capacity gives

\[
\boxed{T_{\rm cap}^{(8)}=3.216308037410e+13\ {\rm GeV}},
\]

\[
g_*=135.082907732,\qquad g_{*s}=135.070385257.
\]

The old four-real-scalar control gives

\[
T_{\rm cap}^{(4)}=3.240553674564e+13\ {\rm GeV},
\]

so

\[
\frac{T_8}{T_4}=0.992518057.
\]

The bidoublet threshold itself is not fixed, so this is a branch/control rather than a replacement thermal history. The ambiguity is precisely the theorem failure.

## 4. Visible-sector self-thermalization

At the eight-real-scalar control,

\[
H=1.635103035161e+09\ {\rm GeV},\qquad H/T=5.083788667450e-05.
\]

For

\[
\Gamma_{\rm gauge}\sim\kappa\alpha_{\rm PS}^2T,
\]

thermalization requires approximately

\[
g_{\rm PS}>0.299331\quad(\kappa=1)
\]

or

\[
g_{\rm PS}>0.532294\quad(\kappa=0.1).
\]

Thus ordinary non-tiny gauge couplings would thermalize the visible sector rapidly. But the numerical Pati-Salam coupling and full breaking thresholds are not uniquely fixed here.

**Visible self-thermalization: CONTROLLED CONDITIONAL PASS.**

## 5. Phi-sector internal equilibration

The inherited radial decay width gives

\[
\frac{\Gamma_{\sigma\to2\pi}}{H}=227.193198.
\]

At the same temperature,

\[
m_\sigma/T=5.805667.
\]

Detailed balance gives the inverse-decay rate per Goldstone

\[
\Gamma_{\pi\pi\to\sigma}^{\rm per\ \pi}
\simeq
2\frac{n_\sigma^{\rm eq}}{n_\pi}
\Gamma_\sigma
\frac{K_1(m_\sigma/T)}{K_2(m_\sigma/T)},
\]

and

\[
\boxed{\Gamma_{\rm inv}/H=10.589526}.
\]

So if the handoff loads the `Phi` sector near this capacity scale, the radial/Goldstone subsystem can build a rescattered high-energy tail. The portal-freeze-in mechanism is therefore not killed by the first-generation decay kinematics found in 0G.

**Phi internal equilibration: PASS / STRONG CONDITIONAL.**

## 6. The decisive failure: no derived visible-Phi thermal connector

Internal thermalization of each sector does not prove

\[
T_{\rm vis}=T_\Phi.
\]

The frozen Pati-Salam gauge action is written schematically with field-dependent kinetic functions `Z_a(Phi,phi)`, but their post-handoff derivatives/normalizations are not fixed well enough to calculate a `Phi`-visible energy-exchange rate. The geometric handoff is a universal transient source; it is not by itself a theorem of sustained thermal contact afterward.

As capacity diagnostics only:

\[
\Gamma\sim\lambda^2T/(8\pi)
\]

would require

\[
\lambda\gtrsim0.035745,
\]

while a dimension-five `sigma F^2/F` interaction with

\[
\Gamma\sim c^2T^3/(8\pi F^2)
\]

would require

\[
c\gtrsim0.196863.
\]

These are modest values, showing common equilibration is plausible, but the current action does not select either coefficient.

\[
\boxed{T_{\rm vis}=T_\Phi\ \text{is not derived}.}
\]

## 7. Post-freeze consequence for the old 0G 2.057% overlap

Only after the theorem findings above were frozen do we revisit the previous abundance comparator.

The 0G common-bath row used four real visible scalar degrees of freedom and gave

\[
Y_q^{(0G)}=4.970317483749\times10^{-25},
\]

2.057% above the frozen holdout.

The field-content audit now shows that the four-scalar high-temperature spectrum is not selected by the action. As a **sensitivity diagnostic only**, if all eight real components of the complex bidoublet are active while the rest of the 0G common-bath assumptions are left unchanged, then using the already-frozen local sensitivity

\[
d\ln Y_q/d\ln T\simeq54
\]

gives approximately

\[
Y_q^{(8),{\rm sens}}\simeq3.313283796057e-25,
\]

or

\[
0.680
\]

times the holdout.

This is not an exact portal rerun and is not a new prediction. It demonstrates that the 2% overlap is spectrum-fragile.

The proper classification of the 0G near-match is therefore demoted to

\[
\boxed{\textbf{interesting target-blind comparator clue, not a robust structural prediction}.}
\]

## 8. Formal claim boundary

**Derived / retained:** stable ultraheavy `q`; portal pair-production operator; nonzero visible handoff accessibility; fast `Phi`-sector internal equilibration if loaded; downstream cold/collisionless `q` cosmology.

**Still not derived:** absolute handoff loading; exact PS gauge coupling/matching at the handoff scale; complete PS-breaking Higgs spectrum and thresholds; visible-`Phi` thermal connector; one common temperature; threshold-complete `g_*,g_*s`; therefore the absolute `Y_q`.

## 9. Verdict and next step

0G1 does not upgrade the heavy-q abundance to first principles. It localizes the remaining gap to the two-phase reheating/interface state rather than to dark microphysics.

\[
\boxed{\textbf{Heavy q remains the preferred conditional particle-DM completion.}}
\]

If first-principles abundance closure remains the goal, the only high-value continuation is

\[
\boxed{\textbf{DM-TP-0G2-Q — Pati-Salam breaking spectrum and Phi-visible connector provenance gate}}
\]

performed without using the DM abundance.

0G2 should derive or falsify the actual Pati-Salam-breaking spectrum, gauge coupling/matching, post-handoff `Phi`-visible connector, equilibration rate/temperature ratio, and threshold-complete thermal degrees of freedom. An older explicit Pati-Salam-breaking completion exists, but it added new multiplets and VEVs as structural assumptions and must not be silently imported as a first-principles answer.

If 0G2 cannot uniquely supply those data, the scientifically clean endpoint is the already-closed **conditional heavy-q dark-matter theory**, not a tuned abundance closure.