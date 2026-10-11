# Reproducibility Check

## Current Portfolio Edition: October 11, 2026

This record describes actual checks of the personal research presentation. The
original four-author coursework files and previous public version were frozen
before editing in the private development archive. Earlier Git commits are retained.
The report and notebook authorship fields now name QIDIAN XING, following the
author's statement of individual substantive work. No external authorship audit
or independent research replication is asserted.

## Execution Environment

The revised version ran on Apple Silicon macOS with Python 3.12.14, NumPy 2.2.6,
SciPy 1.15.3, pandas 2.2.3, Matplotlib 3.10.3 and Numba 0.61.2. The numerical
packages use the verified OpenBLAS environment installed in a private virtual
environment during the October 10 clean-install check. This revision reused that
environment; it does not claim another clean dependency installation occurred.
No global environment was modified. Dependency pins and the public runner are
byte-identical to the previous version.

The README installation procedure remains unchanged, including its Apple Silicon
wheel branch. Linux, Windows and Intel macOS clean installations remain unverified.

## Actual Fresh-Kernel Execution

An isolated copy of the revised repository ran the public entry point:

```sh
python scripts/run_all_notebooks.py
```

The interpreter was the verified private virtual environment's Python. The runner
completed with exit status 0, executed each notebook in a separate fresh kernel,
and saved all outputs. These successful executed notebooks are the public files.

| Notebook | Executed code cells | Error outputs | Status |
| --- | ---: | ---: | --- |
| 01 | 6 | 0 | Passed |
| 02 | 18 | 0 | Passed |
| 03 | 18 | 0 | Passed |
| 04 | 6 | 0 | Passed |
| 05 | 25 | 0 | Passed |
| 06 | 20 | 0 | Passed |
| Total | 93 | 0 | Passed |

A second independent clean-kernel execution started with notebooks 05 and 06,
then ran 01, 02, 03 and 04. It captured full-precision variables and plot line
coordinates in the private archive without adding capture code to public notebooks.
Both executions ran T=300, 3,000 and 300,000, and all T=936, B=200 Monte Carlo
attempts. Original truth, optimizer settings, seeds and SeedSequence stream
construction were unchanged. All 200 attempts were parameter-valid and SE-valid,
with zero exceptions and zero selected optimizer-flag failures; none was replaced
or removed. Notebooks 05 and 06 independently obtained their required fits.

## Numerical and Implementation Consistency

Comparison used **rtol=1e-6, atol=1e-8**, excluding runtime and environment metadata.
All **1,172,547** compared numerical values were identical;
the maximum absolute difference was **0**.

The comparison covered simulation estimates, likelihoods, full Hessians and
delta-method SEs, inference diagnostics, filtered and smoothed states, augmented
matrices and stationary covariance checks, 913 common forecasts and errors, RMSE
and MAE, latent persistence and annual correlations, four economic simulations,
every Monte Carlo attempt and calibration summaries. Plot line coordinates and
axis limits also matched. Embedded result tables matched excluding timing.
The 19 displayed README numerical entries agree with the report and freshly
computed variables.

Every statistical code cell is unchanged. The only code-text change is a CONFIG
provenance description that is not used in computation; parsing confirms every
other setting is identical. Markdown headings, author metadata and explanatory
presentation were revised. All six notebooks remain executable independently.

The raw CSV remains byte-identical, with SHA256:

`73f7bb1bd87492251b9f0e0ad5a7dbfdef6a2d27d6c97b3cdcdd97ac6de870b7`

## Report and Repository Review

The report was regenerated from an archived copy of the original editable Python
document generator. The original course report and its source remain unmodified.
The revised generator and generated editable Markdown are preserved privately;
they are not notebook runtime dependencies.

All **26 equations**, **9 tables**
and **5 figures** were compared against the original generator. Equation strings,
table contents and figure asset bytes/captions match exactly. Research question,
methods, simulations, both historical fits, annual augmentation, forecasts,
Monte Carlo diagnostics, conclusions and limitations remain present.
The approximately 7.4% retrospective RMSE reduction and the historical/model
annual correlations remain qualified correctly.

The final PDF has **13 pages**. Searchable text and metadata confirm
the sole-author field, research title and absence of Homework 1/course branding.
All final pages were rendered and visually reviewed, including pixel comparison
of unchanged pages after the last narrative correction. No missing elements,
clipping or overlap were observed. Its SHA256 is:

`902a38cdcb4eff461cb4ac9337572d627f039db64d37195938da7d17771120ec`

README relative links and notebook data/AI-document paths were checked. No private
absolute paths, cached external results or original project runtime dependencies
were introduced. The public AI summary is a new document; the historical disclosure
PDF remains archived and in previous commits, rather than being rewritten.

## Boundaries

Validation concerns numerical reproducibility under the specified model. It does
not establish model adequacy, exact finite-sample uncertainty or significant
out-of-sample forecast superiority. Full-sample parameter estimates make the
forecast comparison retrospective. Dataset upstream provenance and a separate
redistribution license were not specified in the supplied materials. No substitute
data, external replication, peer review or new statistical experiment is claimed.
GitHub push and remote checks are recorded separately in the private release audit.
