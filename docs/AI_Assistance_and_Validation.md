# AI Assistance and Validation

**Author: QIDIAN XING**

## Scope and attribution

AI served as a research and coding assistant for model derivation, Python
implementation, numerical debugging, result interpretation and reproducibility
checks. This is a new portfolio summary of documented activity, not a verbatim
transcript or a reassignment of historical prompts. The personal edition follows
the author's statement that the substantive research, implementation, analysis and
report were completed individually with AI assistance. It does not certify manual
authorship of every line, an independent human audit or external replication.

The original four-author coursework report and AI disclosure remain in the local
development archive and earlier Git commits. No historical record is rewritten,
and no assertion is made that the other named individuals contributed nothing.

## Derivation and implementation

AI assistance covered the monthly latent Gaussian AR(1) model, stationary prior,
Kalman innovation likelihood, maximum-likelihood estimation, full-likelihood
Hessian and delta-method standard errors, filtering, smoothing and forecast
propagation. The annual model explicitly retains twelve latent lags and twelve
monthly observation shocks. This 24-state representation accounts for overlap;
zero additional annual measurement variance does not imply zero monthly noise.

## Documented validation

Simulation parameter recovery uses the original truth, seeds and samples of 300,
3,000 and 300,000 months. The annual likelihood is also checked on rolling sums of
the same original 3,000-month sample. Historical fits retain 936 monthly data points,
925 annual observations and 913 common complete-future-year forecast targets.
Forecasts use filtered states with no intervening observation updates.

Earlier development checks compared innovation likelihoods against dense Gaussian
joint densities and checked stationary covariance, lag shifts, smoothing moments,
forecast propagation and metric/date alignment. These are numerical implementation
checks, not independent research replication or proof of model adequacy.

The supplementary Monte Carlo study retains T=936, B=200 and master seed 20261003,
with the original SeedSequence spawning and generate_state procedure. All attempts,
validity flags and failures are retained. The existing results contain 200
parameter-valid and 200 SE-valid fits, with no exceptions. Mean-SE / empirical-SD
ratios are approximately 0.951, 0.914, 1.066 and 1.006 for the mean, persistence,
state-shock SD and observation-shock SD; corresponding 95% coverage is 0.915,
0.940, 0.940 and 0.970. Finite Monte Carlo uncertainty and validity conditioning
limit the interpretation of these diagnostics.

## Material corrections

- Innovation timing: form the predictive distribution before observing the current
  value; after it arrives, compute its innovation and likelihood before updating
  the state. The original computational order was correct; the explanation changed.
- Standard errors: use model-based asymptotic Hessian/delta-method language, retain
  full-likelihood scaling and parameter transformations, and avoid claims of exact
  finite-sample or misspecification-robust uncertainty.
- Forecast loss: the monthly fit has lower RMSE but higher MAE than the benchmark.
  The annual fit has lower values of both metrics in this retrospective sample;
  these point comparisons do not establish significant out-of-sample superiority.
- Dependencies: remove machine-local wheel paths and document the verified Apple
  Silicon OpenBLAS installation branch. The precise cause of earlier numerical
  anomalies was not established; no upstream library defect is asserted.
- Calibration: retain the predeclared 200-stream repeated-sampling check without
  selecting favorable seeds, dropping attempts or changing the original experiments.

## Reliability and economic adequacy

Numerical validation supports computation of the specified model. It does not
establish that constant Gaussian dynamics capture historical inflation regimes.
Historical annual lag-12 correlation is 0.60718, versus 0.33895 implied by the annual
fit and 0.16905 by the monthly fit. These are observed-sum correlations, distinct
from latent persistence phi^12. Parameters estimated over the full historical
sample make the forecast exercise retrospective, not genuinely out of sample.

## Personal portfolio revision

The user requested presentation, attribution and documentation changes while
preserving the scientific analysis and Git history. This edition replaces group
title pages with a sole-author research presentation, removes course branding from
the report, and replaces the public historical AI PDF with this explicitly new
summary. Statistical code, data, parameters, seeds and random-stream construction
are retained. One descriptive CONFIG provenance string is updated; it is not used
in statistical computation. The revised version completed two separate fresh-kernel executions of all six
notebooks, including the 300,000-month experiment and all 200 Monte Carlo attempts.
Comparison of 1,172,547 numerical values found a maximum absolute difference of zero.
All 93 public code cells have executed outputs without errors. The regenerated
13-page report retains all 26 equations, nine tables and five figures; searchable
text, metadata and every rendered page were reviewed. Details and platform limits
are recorded in [Reproducibility Check](../REPRODUCIBILITY_CHECK.md).
