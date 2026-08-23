# DM-TP-0E-Q — minimal conditional heavy-q cosmology and production-datum gate

**Version:** v1.0.0  
**Status:** FROZEN CONDITIONAL CHECKPOINT  
**Galaxy/RAR data used:** NO  
**Historical H8 used as input:** NO  
**Historical `Lambda_mem` used as input:** NO  
**`N_star`, `L_IR`, or `rho_DE` refit for DM:** NO  
**Old `exp(-2 pi m_q tau_q)` clue used to choose the conditional datum:** NO  
**Number of new universal DM history/state normalizations admitted:** ONE

## Executive verdict

\[
\boxed{\text{heavy-}q\text{ particle existence/mass/stability: DERIVED}}
\]

\[
\boxed{\text{homogeneous cosmology given one universal yield }Y_q: PASS}
\]

\[
\boxed{\text{absolute handoff production theorem: STILL NO-PASS}}
\]

\[
\boxed{\textbf{DM-TP-0E-Q = MINIMAL CONDITIONAL COSMOLOGICAL-DM PASS}}
\]

This checkpoint implements the stop-rule proposed after Routes A/B/C. It does **not** pretend that the two-phase handoff has derived the heavy-`q` occupation. Instead it asks whether exactly one universal post-handoff production datum is enough to make the rest of the cosmology predictive.

The answer is yes at the homogeneous/background level.

---

# 1. Derived particle data retained from B1

The currently frozen EFT has an exact

\[
q\rightarrow-q
\]

parity and a parity-even true vacuum \(q_T=0\). Therefore the lightest `q`-odd excitation is stable within the frozen EFT.

The true-vacuum Hessian gives a genuine massive eigenstate. Using the frozen handoff controls,

\[
m_q\tau_q=8.8812183572,
\qquad
\tau_q=6.509369532781e-39\ {\rm s},
\]

one obtains

\[
\boxed{m_q=8.980476657703e+14\ {\rm GeV}}
\]

or

\[
\boxed{m_q\simeq1.600915376114e-09\ {\rm g}}.
\]

Relative to the microscopic action scale,

\[
\frac{m_q}{F}=5.069796241105.
\]

No particle-mass parameter is introduced in 0E-Q.

---

# 2. The single conditional datum

Define the asymptotic post-handoff `q` yield

\[
\boxed{
Y_q\equiv
\left.\frac{n_q}{s_{\rm vis}}\right|_{\rm after\ immediate\ handoff/transient}
}
\]

after an ordinary visible entropy density exists and after any very short initial number-changing transient.

This is the **only** new universal DM normalization admitted in the conditional theory.

It is global, dimensionless, independent of the late DE ruler, not identified with H8 or `Lambda_mem`, not identified with a guessed Bogoliubov coefficient, and not chosen from the observed abundance until the mapping below is frozen.

After number-changing processes become negligible,

\[
\dot n_q+3Hn_q=0,
\qquad
\dot s+3Hs=0,
\]

so

\[
\boxed{Y_q={\rm constant}}.
\]

---

# 3. Homogeneous abundance becomes fully determined by Y_q

For a nonrelativistic population,

\[
\rho_q=m_q n_q=m_qY_q s.
\]

Therefore today

\[
\Omega_q h^2
=
\frac{m_qY_q s_0}{\rho_c/h^2}.
\]

Using the standard entropy/critical-density conversion constants, but **not yet the dark-matter target**, the frozen conditional mapping is

\[
\boxed{
\Omega_q h^2
=
2.463995645338e+23\,Y_q .
}
\]

Equivalently,

\[
\boxed{
Y_q=
\frac{\Omega_qh^2}{2.463995645338e+23}.
}
\]

This mapping was frozen before opening the standard `Omega_c h^2` holdout.

---

# 4. Radiation-to-q evolution

For a thermal radiation bath,

\[
\rho_r=\frac{\pi^2}{30}g_*T^4,
\qquad
s=\frac{2\pi^2}{45}g_{*s}T^3.
\]

Hence, while `q` is nonrelativistic,

\[
\boxed{
\frac{\rho_q}{\rho_r}
=
\frac43\frac{g_{*s}}{g_*}\frac{m_qY_q}{T}.
}
\]

Thus the conditional state has exactly the desired matter/radiation scaling, apart from known entropy-degree-of-freedom factors.

---

# 5. Pair annihilation does not generate a hidden freeze-out parameter

Exact `Z_2` parity forbids one-particle decay but allows `qq` annihilation into even-sector states. A deliberately hostile partial-wave unitarity bound gives

\[
\langle\sigma v\rangle\lesssim\frac{4\pi}{m_q^2v}.
\]

At the maximum handoff radiation-equivalent temperature capacity,

\[
\frac{\Gamma_{\rm ann}}H\lesssim3.165075408503e+05\,Y_q.
\]

Annihilation becomes competitive only for

\[
\boxed{Y_q\gtrsim3.159482384886e-06}.
\]

Therefore the tiny nonthermal abundance of interest is effectively collisionless and does not acquire a second freeze-out normalization.

---

# 6. Coldness and phase-space boundary

For the action-derived handoff resolution comparator \(p_*\tau_q\sim1\),

\[
\frac{p_*}{m_q}=0.112597164013,
\qquad
v_*=0.111890119696,
\qquad
w_*=4.173132961840e-03.
\]

The resolved characteristic modes are already nonrelativistic and cool as \(p\propto a^{-1}\). B1 showed that the exact high-momentum tail of `beta_q(k)` is not derived, so 0E-Q does not claim an exact primordial phase-space distribution.

A conservative free-streaming control gives \(\lambda_{\rm FS}\simeq3.12\times10^{-5}\,\mathrm{Mpc}\) when momentum redshift is withheld until the 5 MeV BBN floor.

---

# 7. Conditional theory freeze before abundance holdout

At this point the heavy-`q` background theory is frozen as

\[
\boxed{
\{\text{derived }m_q,\ Z_2\text{ stability}\}
+
\{\text{one universal conditional }Y_q\}.
}
\]

Its homogeneous predictions include \(n_q=Y_qs\), \(\rho_q=m_qY_qs\), \(\rho_q\propto a^{-3}\), and \(\Omega_qh^2=2.463995645338e+23Y_q\).

No observational DM density has been used to choose these relations.

---

# 8. Holdout unblind: required universal q yield

Using the standard reference \(\Omega_ch^2=0.1200\) after the mapping was frozen gives

\[
\boxed{Y_q^{\rm req}=4.870138477194e-25.}
\]

This is approximately one stable `q` quantum per \(2.05\times10^{24}\) entropy quanta. At this yield even the hostile annihilation bound gives \(\Gamma/H\lesssim1.54\times10^{-19}\).

The present cosmic mean density is \(n_{q0}=1.408054436526e-21\,\mathrm{cm^{-3}}\), corresponding to a mean spacing of roughly 89.2 km.

---

# 9. Required handoff energy fraction

At the full handoff temperature capacity the required conditional yield corresponds to

\[
\boxed{\rho_q/\rho_r\simeq8.55\times10^{-24}},
\]

and at the inherited amplitude-energy temperature comparator to \(1.71\times10^{-23}\). These are targets for a future production theorem, not fitted inputs.

---

# 10. Equality and baryon-ratio consistency

The required `q` yield gives a `q`-only equality temperature of approximately 0.679 eV. Adding the reference baryon density gives the standard cold-matter equality chronology. The density ratio is \(\rho_q/\rho_b=5.3643\), while the ultraheavy mass implies a tiny particle-number ratio \(n_q/n_b\simeq5.60\times10^{-15}\).

---

# 11. Exponential clue remains non-derivational

The quarantined number

\[
e^{-2\pi m_q\tau_q}=5.825743513015e-25
\]

is numerically within about 19.6% of the required yield. This remains a clue only: a schematic quench suppression is not yet a derived entropy-normalized integrated occupation.

---

# 12. Formal classification

DM-TP has **not** produced first-principles absolute dark matter because the two-phase handoff still does not derive `Y_q`.

But after exhausting the zero-new-input alternatives, heavy `q` satisfies the intended conditional endpoint:

\[
\boxed{
\text{particle, mass, stability, matter redshifting derived; }Y_q\text{ one universal conditional history datum}.
}
\]

Therefore

\[
\boxed{\textbf{DM-TP-0E-Q = CONDITIONAL COSMOLOGICAL-DM PASS}}
\]

at the homogeneous/background level.
