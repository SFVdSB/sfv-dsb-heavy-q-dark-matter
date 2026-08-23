# DM-TP-0F-Q — linear structure, CMB, free-streaming and interaction gate

**Version:** v1.0.0  
**Status:** FROZEN CONDITIONAL CHECKPOINT  
**Conditional abundance datum inherited from 0E-Q:** `Y_q = 4.870138477194e-25`  
**New dark normalization introduced in 0F-Q:** NONE  
**Historical H8 / `Lambda_mem` used:** NO  
**B1E galaxy response combined with particle-q gravity:** NO  
**Galaxy/RAR data opened:** NO

## Executive verdict

\[
\boxed{\text{late collisionless / linear-CDM limit: PASS}}
\]

\[
\boxed{\text{free-streaming / shot-noise / self-interaction gates: PASS}}
\]

\[
\boxed{\text{CMB adiabaticity: CONDITIONAL PASS under one-source universal handoff yield}}
\]

\[
\boxed{\text{exact UV handoff phase-space tail: still not derived}}
\]

\[
\boxed{\textbf{DM-TP-0F-Q = CONDITIONAL LINEAR-STRUCTURE PASS}}
\]

The heavy `q` completion survives the post-background cosmology gate without adding a second dark normalization. Its remaining microscopic weakness is still the production theorem, not late-time structure.

A new production clue also emerges: the already-existing `P^2 q^2` portal permits exponentially small handoff-era freeze-in from a transient hidden scalar/Goldstone bath. A controlled threshold comparator places the required yield in the right class when the relevant maximum bath temperature is near `hbar/(pi tau_q)`. This is retained only as a next-step derivation target.

## 1. Collisionless perturbation limit

For a stable nonrelativistic distribution after the handoff transient,

\[
w_q \simeq \frac{\langle v^2\rangle}{3},
\qquad
v\propto a^{-1}.
\]

The frozen handoff resolution comparator `p tau_q = 1` gives

\[
\frac{p_*}{m_q}=0.112597164013,
\qquad
v_*=0.111890119696,
\qquad
w_*=4.173132961840e-03.
\]

Even under the deliberately hostile assumption that no momentum redshift is credited until the 5 MeV BBN floor,

\[
v_{\rm eq}=1.277479387377e-08,
\qquad
w_{\rm eq}=5.439845283912e-17,
\]

and at recombination

\[
v_{\rm rec}=4.129491501768e-09,
\qquad
w_{\rm rec}=5.684233354393e-18.
\]

Thus by the CMB and matter-growth eras `q` is dynamically indistinguishable from pressureless CDM at the background/linear-stress level.

## 2. Free streaming

Using the same hostile 5 MeV start,

\[
\boxed{
\lambda_{\rm FS}
=3.121383237719e-05\ {\rm Mpc}
=31.214\ {\rm pc}
}.
\]

The corresponding scale is

\[
k_{\rm FS}\sim2.012949012878e+05\ {\rm Mpc}^{-1},
\]

with a simple enclosed-mass comparator

\[
\boxed{M_{\rm FS}\sim6.323981000470e-04\,M_\odot}.
\]

If a normal radiation bath exists by 100 GeV,

\[
\lambda_{\rm FS}\simeq1.157756777562e-09\ {\rm Mpc}.
\]

Within the controlled EFT band,

\[
p\lesssim\hbar/\tau_q
\quad\Rightarrow\quad
p/m_q\lesssim0.113.
\]

A relativistic `p >= m_q` tail requires structure at frequencies `omega tau_q >= 8.88`, above the resolved handoff band. The exact sub-`tau_q` UV tail remains an explicit caveat rather than a fitted warm-DM fraction.

## 3. CMB adiabaticity

The one conditional datum is a universal yield:

\[
n_q=Y_q s.
\]

Since radiation entropy obeys `s proportional to rho_gamma^(3/4)`,

\[
\frac{\delta n_q}{n_q}
=
\frac{\delta Y_q}{Y_q}
+\frac34\frac{\delta\rho_\gamma}{\rho_\gamma}.
\]

Therefore

\[
S_{q\gamma}
=
\delta_q-\frac34\delta_\gamma
=
\boxed{\frac{\delta Y_q}{Y_q}}.
\]

For the one-source universal handoff datum, `delta Y_q=0`, so

\[
\boxed{S_{q\gamma}=0}.
\]

A future microscopic production calculation that generates a coherent spatially varying `Y_q(x)` would falsify this one-datum completion rather than justify a second fitted isocurvature amplitude.

## 4. Shot noise and granularity

The present mean density is

\[
n_{q0}=1.408054436526e-21\ {\rm cm}^{-3}
=4.136862450561e+52\ {\rm Mpc}^{-3}.
\]

Thus

\[
\boxed{P_{\rm shot}=2.417290910566e-53\ {\rm Mpc}^3}.
\]

At a 220 km/s halo speed,

\[
\boxed{\lambda_{\rm dB}=1.881329964794e-27\ {\rm m}}.
\]

Both particle shot noise and quantum pressure are negligible.

## 5. Self-interactions

Even the `s`-wave unitarity ceiling at `v=10^-3 c` gives

\[
\boxed{
\frac{\sigma_{qq}}{m_q}
\lesssim3.789790797255e-42\ {\rm cm^2\,g^{-1}}
}.
\]

The ultraheavy relic is therefore astrophysically collisionless regardless of order-one microscopic scalar couplings.

## 6. Late hidden drag

The leading explicit hidden connector is `g P^2 q^2`, while the radial mode couples derivatively to the Goldstone. A conservative radial-exchange scaling control gives

\[
\Gamma_{\rm drag}/H\sim6.748463475065e-02
\]

even at the full handoff-capacity temperature, falling to \(1.056672284514e-03\) at the amplitude-capacity comparator and \(7.361857566373e-04\) near the production-source temperature. The rate then falls steeply with temperature.

No late acoustic coupling survives to the CMB era.

## 7. Exploratory production-source clue: portal freeze-in

The inherited interactions contain

\[
-2gv\,\sigma q^2
+\frac{\sigma}{v}(\partial\pi)^2.
\]

Near the heavy-pair threshold, a transparent tree-level comparator is

\[
\boxed{
\langle\sigma v\rangle_{qq\leftrightarrow\pi\pi}
\sim\frac{g^2}{4\pi m_q^2}
=5.278976877118e-31\ {\rm GeV}^{-2}
}.
\]

For a `q`-coupled bath with maximum temperature `T_h << m_q`, detailed balance gives the freeze-in equation

\[
\frac{dY_q}{dx}
\simeq
\frac{2n_{q,\rm eq}^2\langle\sigma v\rangle}{sHx},
\qquad x=m_q/T.
\]

The exploratory comparator gives a required source temperature

\[
\boxed{T_{h,\rm req}=3.211862520324e+13\ {\rm GeV}},
\]

with

\[
\boxed{
\frac{T_{h,\rm req}}{\hbar/(\pi\tau_q)}
=0.997883817563
}.
\]

This is a strong conceptual source clue: a handoff-created scalar/Goldstone transient can yield exponentially subthreshold portal freeze-in of stable `q`. It respects `Z_2`, produces pairs, and makes the tiny yield arise from an exponential rather than a tiny new coupling.

It is not yet a first-principles abundance theorem because the actual maximum temperature and thermalization history of the `q`-coupled hidden bath remain underived.

## 8. Relation to the old exponential clue

A thermal pair source has \(Y_q\propto e^{-2m_q/T_h}\) at leading exponential order. If \(T_h\simeq\hbar/(\pi\tau_q)\), then \(e^{-2m_q/T_h}\simeq e^{-2\pi m_q\tau_q}\). The old coincidence may therefore be pointing to an effective handoff temperature and portal-freeze-in exponent rather than directly to a Landau-Zener probability.

This is a hypothesis, not a closure.

## 9. Formal disposition

0F-Q passes with no new dark normalization: pressureless by equality/CMB, tiny free streaming, negligible shot noise, negligible self-interaction, negligible late hidden drag, and adiabatic under the one-source universal-yield condition.

Therefore

\[
\boxed{\textbf{heavy q remains the preferred conditional particle-DM completion.}}
\]

The next high-value checkpoint is

\[
\boxed{\textbf{DM-TP-0G-Q — handoff thermal/portal freeze-in production theorem gate}}
\]

performed blind to `Y_q^{req}` until the transient production result is frozen.
