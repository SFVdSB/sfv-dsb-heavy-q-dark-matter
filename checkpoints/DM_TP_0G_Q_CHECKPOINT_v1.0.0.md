# DM-TP-0G-Q — handoff thermal / portal-freeze-in production theorem gate

**Version:** v1.0.0  
**Status:** FROZEN CHECKPOINT  
**Observed `Y_q` used to construct the production comparators:** NO  
**Pre-unblind commitment SHA-256:** `ca914c584fedcea70c7c607273106454cd1c7b10c6183b99cda33dd13829bb95`  
**New dark coupling introduced:** NO  
**New DM normalization introduced:** NO  
**Historical H8 / `Lambda_mem` used:** NO  
**DE quantities refit:** NO

## Executive verdict

\[
\boxed{\text{portal production operator and heavy-q pair kernel: PASS}}
\]

\[
\boxed{\text{handoff thermal state / absolute loading theorem: NO-PASS}}
\]

\[
\boxed{\text{minimal Pati-Salam+Phi common-bath comparator: STRONG TARGET-BLIND OVERLAP}}
\]

\[
\boxed{\textbf{DM-TP-0G-Q = PRODUCTION MICROPHYSICS PASS / ABSOLUTE ABUNDANCE STILL CONDITIONAL}}
\]

0G-Q improves the theory substantially: the missing heavy-`q` abundance no longer requires an unspecified dark interaction. The frozen action already contains the necessary pair-production operator. The remaining gap is upstream and geometric/thermal: the two-phase handoff has not yet derived the temperature/distribution/sector partition on which the fixed portal acts.

## 1. Exact portal production channels

Write the complex radial field in the true phase as

\[
P=v+\sigma,\qquad \pi=v\theta .
\]

The frozen action contains

\[
\mathcal L\supset
\frac{\sigma}{v}(\partial\pi)^2
-2gv\sigma q^2
-g\sigma^2q^2 .
\]

Therefore no new dark coupling is needed.

For massless Goldstones,

\[
\boxed{
\mathcal M(\pi\pi\to qq;s)
=
\frac{4gs}{s-m_\sigma^2}
}
\]

up to an irrelevant overall sign, and

\[
\sigma(qq\to\pi\pi)
=
\frac{|\mathcal M|^2}{32\pi s\beta_q}.
\]

The radial channel `sigma sigma <-> q q` is also fixed by the same action through the contact term, the s-channel radial cubic, and t/u-channel `q` exchange.

## 2. Correction to the exploratory 0F normalization

`q` is a real self-conjugate `Z_2` scalar. Its standard number equation is

\[
\dot n_q+3Hn_q
=
-\langle\sigma v\rangle
(n_q^2-n_{q,\rm eq}^2).
\]

Hence in freeze-in,

\[
\boxed{
\dot n_q+3Hn_q
\simeq
\langle\sigma v\rangle n_{q,\rm eq}^2 .
}
\]

The exploratory 0F calculation used an extra factor of two. 0G-Q corrects that normalization and uses the exact thermal average of the derived cross sections.

## 3. Hard kinematic result: radial decay is not itself the q source

\[
m_q=8.980477e+14\ {\rm GeV},
\qquad
m_\sigma=1.867281e+14\ {\rm GeV},
\]

so

\[
\boxed{
\frac{2m_q}{m_\sigma}
=9.618771 .
}
\]

Thus `sigma -> q q` is impossible.

Moreover the primary Goldstones from `sigma -> 2 pi` have energy of order `m_sigma/2`; even a head-on first-generation `pi pi` collision has `sqrt(s) <= m_sigma < 2m_q`.

Therefore ordinary perturbative portal production requires a **rescattered high-energy/thermal tail** or a separate direct nonadiabatic handoff process.

## 4. What the frozen handoff does and does not own

The two-phase handoff independently fixes the quench resolution time and proves that visible and hidden stress-carrying channels are accessible. It also supplies a fast action-derived sink once the radial sector is loaded.

But the frozen DE handoff explicitly does **not** fix the absolute channel loading, the exact Bogoliubov partition, or one unique reheating temperature.

Therefore the production equation is now fixed, but its initial thermal state is not.

## 5. Pre-unblind comparator family

Before reopening `Y_q^req`, 0G-Q froze a discrete set of upstream-motivated controls.

| comparator | target-blind `Y_q` |
|---|---:|
| coherent sigma decay without rescattering | `0` |
| amplitude energy -> SM+Phi common bath | `8.868731e-24` |
| amplitude energy -> minimal PS+Phi common bath | `4.970317e-25` |
| amplitude-capacity PS stress-separated hidden bath | `3.545375e-28` |
| full-gap PS stress-separated hidden bath | `4.498711e-15` |

The spread is enormous. This is not numerical instability in the portal kernel; it is direct evidence that the **handoff thermal-state theorem is the remaining abundance problem**.

## 6. High-priority Pati-Salam common-bath comparator

A natural minimal free-field realization of the already-used high-temperature Pati-Salam stress comparator has 21 gauge vectors, 48 visible Weyl fields and four real visible scalar components. If those visible degrees of freedom, the exact Goldstone, and the rapidly equilibrating but Boltzmann-suppressed radial mode share a common bath, the smooth thermal count at the maximum is

\[
g_*=131.085395,\qquad g_{*s}=131.072540 .
\]

Complete thermalization of the independently known amplitude-energy capacity then gives

\[
\boxed{
T_{\max}=3.240553e+13\ {\rm GeV}
}
\]

without using the DM abundance.

The exact tree-level `pi pi` plus `sigma sigma` production integral then gives the target-blind comparator

\[
\boxed{
Y_q^{\rm PS,common}
=4.970317483749e-25 .
}
\]

This number was included in the pre-unblind commitment.

## 7. Holdout comparison

Only after the above comparator set was frozen do we reopen

\[
Y_q^{\rm req}=4.870138477194e-25 .
\]

For the high-priority PS+Phi common-bath comparator,

\[
\boxed{
\frac{Y_q^{\rm pred}}{Y_q^{\rm req}}
=1.020570053
}
\]

or

\[
\boxed{
\Delta Y/Y=+2.057\%.
}
\]

The portal loop expansion marker is

\[
\frac{g^2}{16\pi^2}=0.0339,
\]

so a two-percent tree-level discrepancy is not obviously pathological. This is only a scale diagnostic, not a declared uncertainty band.

## 8. Why this is still not a first-principles abundance closure

The close row cannot be selected because it matches.

The following remain unproved:

1. the handoff loads the full inherited amplitude-energy capacity into excitations;
2. the visible Pati-Salam modes and `Phi` sector share one temperature at the relevant time;
3. the comparator's free-field active-degree count is the actual threshold-complete `g_*(T),g_*s(T)`;
4. no nonthermal handoff tail or direct geometric production adds a comparable `q` component.

Around the PS common-bath row,

\[
\frac{d\ln Y_q}{d\ln\rho_{\rm load}}\simeq13.6,
\qquad
\frac{d\ln Y_q}{d\ln T_{\max}}\simeq54.
\]

A percent-level abundance prediction therefore requires the loading/temperature theorem itself to be sharp.

Post-unblinding, a loading factor `0.998503489` would make this comparator land exactly on the holdout. **That number is explicitly forbidden as a fit.**

## 9. Formal disposition

0G-Q derives the particle-production microphysics but not the absolute thermal initial condition.

\[
\boxed{\textbf{Heavy q remains the preferred conditional particle-DM completion.}}
\]

Recommended next checkpoint:

\[
\boxed{\textbf{DM-TP-0G1-Q — handoff loading, thermalization and active-DOF theorem gate}}
\]

0G1-Q should remain blind to the DM abundance while deriving or falsifying the amplitude loading, sector equilibration, active `g_*`, and maximum q-coupled temperature. Only then should the exact 0G portal kernel be rerun against the frozen holdout.