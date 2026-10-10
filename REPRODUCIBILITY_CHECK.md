# Reproducibility Check

Validation date: October 10, 2026. This record concerns the portfolio repository,
not historical test counts from earlier coursework packages.

## Environment and Installation

A copy containing only the repository files was placed in a new temporary directory.
A new project-local virtual environment was created without system site packages.
The documented Apple Silicon wheel branch was downloaded from PyPI and installed,
followed by the pinned direct requirements. `python -m pip check` returned
`No broken requirements found.` No global Python installation was changed.

| Component | Verified version |
| --- | --- |
| OS / architecture | macOS 26.6.2 / arm64 |
| Python | 3.12.14 |
| NumPy / BLAS | 2.2.6 / OpenBLAS 0.3.29 |
| SciPy / BLAS | 1.15.3 / OpenBLAS 0.3.28 |
| pandas | 2.2.3 |
| Matplotlib | 3.10.3 |
| Numba | 0.61.2 |
| IPython / ipykernel | 9.17.1 / 7.4.0 |
| nbformat / nbclient | 5.11.1 / 0.11.0 |
| jupyter-client | 8.10.0 |

The executed installation and reproduction commands, from the copied repository root,
were equivalent to the README commands:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip download --no-cache-dir --only-binary=:all: --no-deps \
  --platform macosx_12_0_arm64 --python-version 312 --implementation cp --abi cp312 \
  --dest .wheels numpy==2.2.6 scipy==1.15.3
python -m pip install --no-index --no-deps \
  .wheels/numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl \
  .wheels/scipy-1.15.3-cp312-cp312-macosx_12_0_arm64.whl
python -m pip install --no-cache-dir -r requirements.txt
python -m pip check
python scripts/run_all_notebooks.py
```

The test used the available Python 3.12.14 interpreter to create the environment,
then invoked `.venv/bin/python` directly in place of activating it. The numerical
packages and notebook kernels ran inside this fresh environment.

## Actual Execution

The public runner completed 01 through 06 sequentially, with a new kernel for each
notebook and exit status 0. All executed outputs were saved. Its six notebook runs
took approximately 52 seconds on this host, including initial font-cache creation;
installation time is excluded and runtime on other machines may differ substantially.

| Notebook | Executed code cells | Error outputs | Status |
| --- | ---: | ---: | --- |
| 01 — Simulate Monthly Model | 6 | 0 | Passed |
| 02 — Estimate Simulated Data | 18 | 0 | Passed |
| 03 — Estimate Actual Monthly Data | 18 | 0 | Passed |
| 04 — Construct Annual Model | 6 | 0 | Passed |
| 05 — Estimate Annual Model and Forecast | 25 | 0 | Passed |
| 06 — Simulate and Diagnose | 20 | 0 | Passed |
| Total | 93 | 0 | Passed |

A second development-only execution used six additional clean kernels, starting
with 05 and 06. Both independently read the CSV and estimated their required monthly
and annual fits. This run captured full-precision in-memory variables for comparison;
the capture code and private logs are not repository dependencies.

Both executions computed T=300, 3,000 and 300,000 and the complete T=936, B=200
supplementary Monte Carlo experiment. All 200 attempts were retained: 200
parameter-valid, 200 SE-valid, zero exceptions and zero selected optimizer-flag
failures. The original SeedSequence stream list and fingerprint were unchanged.
Numba compilation signatures were checked in the independent kernels.

A separate intentional-error probe of the actual runner returned status 1, stopped
before the next notebook, and did not overwrite the failed notebook. This probe is
a script behavior check, not an additional econometric experiment.

## Numerical and Artifact Consistency

Full-precision comparison used **rtol=1e-6, atol=1e-8**, with runtime and environment
metadata excluded. All **1,172,547** compared numeric values matched the preserved
completed version exactly; maximum absolute difference was **0**.

The comparison included parameter estimates, full-Hessian/delta-method SEs,
likelihoods and inference diagnostics, filtered and smoothed states, augmented
matrices and covariance checks, all 913 forecasts and errors, RMSE and MAE,
annual correlations and latent persistence, four simulated economic paths, and
all 200 Monte Carlo replication and calibration records. Plot line data and axes
also matched. All embedded result tables matched the baseline, excluding runtime.

Notebook source changes were limited to the relative CSV path and its associated
working-directory message. No model functions, parameters, seeds, optimization
settings, formulas or task sizes changed. The final notebooks contain five freshly
computed embedded plots and no error outputs. All 19 displayed numerical entries
in README Key Results were checked against the report and freshly computed variables.

The report and AI disclosure PDFs were copied byte-for-byte; SHA256 values are:

| Artifact | SHA256 |
| --- | --- |
| Report | `d839658de0349901010b56a54ea30728a52689c79194e26f5708356a60c5fefc` |
| AI disclosure | `f560119a82e15886f6de56eb41c6425192127ecaa49ef2c8cfdc4623d26c24a2` |
| Raw CSV | `73f7bb1bd87492251b9f0e0ad5a7dbfdef6a2d27d6c97b3cdcdd97ac6de870b7` |

The raw CSV also remained byte-identical to the supplied file. The report has 13 pages;
the AI disclosure has 6. The report's original submission-archive reference is preserved
under the unchanged-PDF requirement; README provides the current repository procedure.

## Scope and Limitations

Linux, Windows and Intel macOS clean installations remain unverified. Dependencies
are pinned directly; transitive dependencies are resolved during installation rather
than frozen as a full environment. Jupyter kernels require local sockets: the first
attempt in a sandbox that denied loopback failed before computation, and the successful
runs used an execution environment that permits those sockets.

No runtime references to the original development directory, personal absolute paths
or saved external results are present in the notebooks or runner. The repository
excludes instructor assignment PDFs, slides, old ZIPs, private review and development
files, temporary wheels, caches and virtual environments. No license was added.

The supplied course materials contained no explicit public-release prohibition found
in this review. Dataset provenance and a separate redistribution license were not
specified. Public release would include the unchanged CSV; this is not a claim that
its redistribution license has been established. GitHub publication and remote checks
are separate from the local validation documented here.
