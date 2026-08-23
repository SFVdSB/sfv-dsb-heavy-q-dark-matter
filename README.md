# SFV/dSB Heavy-q Dark Matter

**Release:** v1.0.0  
**Zenodo DOI:** 10.5281/zenodo.22073295  
**Status:** Conditional particle-dark-matter completion

This repository records the dark-matter rederivation under the frozen SFV/dSB two-phase cosmology. The final retained carrier is the pre-existing real scalar `q`; no new dark field or dark-sector coupling is introduced.

## Main result

The frozen action gives:

- a true-vacuum heavy state `m_q = 8.9804766577e14 GeV`;
- exact `q -> -q` parity and single-particle stability in the frozen EFT;
- cold/collisionless late dynamics;
- an existing `g P^2 q^2` portal that fixes `pi pi -> q q` and `sigma sigma -> q q` production channels.

The remaining non-first-principles quantity is the universal asymptotic post-handoff yield

`Y_q = n_q / s`.

For the reference cosmological abundance `Omega_c h^2 = 0.1200`, the conditional theory requires

`Y_q = 4.8701384772e-25`.

This is **not** claimed as a first-principles abundance prediction. The final 0G2 audit localizes the unresolved physics to the upstream `2+1 -> 3+1` handoff/reheating state: absolute channel loading, the Phi-visible thermal connector, and the threshold-complete Pati-Salam spectrum.

## Paper

- `paper/sfv_dsb_heavy_q_dark_matter_v1.0.0.tex`
- `paper/sfv_dsb_heavy_q_dark_matter_v1.0.0.pdf`

## Repository structure

- `checkpoints/` - formal checkpoint reports from the target-blind derivation program
- `ledgers/` - claim ledgers, numerical controls, model specifications, holdout commitments, and provenance records
- `reproducibility/` - compact scripts for reproducing the final core numerical relations
- `docs/` - final claim boundary and release notes

## Derivation chain

`0A -> 0A.1 -> 0D-A -> 0D-B -> 0D-B1 -> 0D-C -> 0E-Q -> 0F-Q -> 0G-Q -> 0G1-Q -> 0G2-Q`

Important failed or demoted routes are preserved rather than removed. In particular, historical dark-memory/H8 amplitudes and `Lambda_mem` are not inputs to the retained heavy-q abundance theory.

## Related SFV/dSB records

- Gravitational O(4) / CDL completion: DOI `10.5281/zenodo.22070942`
- Phase-B2 quark flavor: DOI `10.5281/zenodo.22059294`
- Two-phase dark-energy cosmology: DOI `10.5281/zenodo.22071079`
- This heavy-q dark-matter release: DOI `10.5281/zenodo.22073295`

## Citation

See `CITATION.cff`.
