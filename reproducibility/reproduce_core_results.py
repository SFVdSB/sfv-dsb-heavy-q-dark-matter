#!/usr/bin/env python3
"""Reproduce the core numerical relations of the v1.0.0 heavy-q paper."""
import math
hbar_GeVs=6.582119569e-25
tau_q=6.509369532780626e-39
mq_tau=8.881218357202066
Yq=4.870138477193871e-25
s0=2891.2
rho_c_h2=1.05375e-5
H0=67.4
Omega_r=9.2e-5
Omega_m=0.315
T0_eV=2.348e-4
gs0=3.91
z_eq=3405.0
M4=2.435e18
T_g2=3.216308037410144e13
gstar_g2=135.082907732
mq=mq_tau*hbar_GeVs/tau_q
omega_coeff=mq*s0/rho_c_h2
omega=omega_coeff*Yq
p_over_m=1/mq_tau
v=p_over_m/math.sqrt(1+p_over_m**2)
w=v*v/3
c_kms=299792.458
a_eq=1/(1+z_eq)
a5=T0_eV/(0.005*1e9)*(gs0/10.75)**(1/3)
pref=c_kms/H0
lambda_rad=pref*v*a5/math.sqrt(Omega_r)*math.log(a_eq/a5)
lambda_mat=pref*v*a5/math.sqrt(Omega_m)*2*(1/math.sqrt(a_eq)-1)
lambda_fs=lambda_rad+lambda_mat
Mpc_cm=3.0856775814913673e24
n0_cm3=Yq*s0
n0_Mpc3=n0_cm3*Mpc_cm**3
Pshot=1/n0_Mpc3
H_g2=math.sqrt(math.pi**2*gstar_g2/90)*T_g2*T_g2/M4
grav_GammaH=(T_g2/M4)**3/math.sqrt(math.pi**2*gstar_g2/90)
print(f"m_q = {mq:.12e} GeV")
print(f"Omega_q h^2 / Y_q = {omega_coeff:.12e}")
print(f"Omega_q h^2 at frozen conditional Y_q = {omega:.12f}")
print(f"p/m (p tau_q=1) = {p_over_m:.12f}")
print(f"v_birth = {v:.12f}")
print(f"w_birth = {w:.12e}")
print(f"conservative lambda_FS = {lambda_fs:.12e} Mpc = {lambda_fs*1e6:.3f} pc")
print(f"n_q0 = {n0_cm3:.12e} cm^-3")
print(f"P_shot = {Pshot:.12e} Mpc^3")
print(f"0G2 H(T_control) = {H_g2:.12e} GeV")
print(f"pure-gravity Gamma/H control = {grav_GammaH:.12e}")
