# U.S. Inflation Persistence with State-Space Models and the Kalman Filter

A reproducible empirical study of monthly U.S. inflation using Kalman filtering,
an augmented annual-observation state-space model, forecast comparison, and
Monte Carlo calibration. The sample contains 936 monthly observations from
January 1947 through December 2024, 925 overlapping twelve-month sums, and
913 common future-year forecast targets.

[Read the full report](report/Inflation_State_Space_Report.pdf)

The report retains the original submission packaging description. The repository
layout and execution instructions below apply to this portfolio version.

## Research Question

How much of monthly U.S. inflation reflects a persistent latent component rather
than transitory noise, and does estimating the same monthly process through
overlapping twelve-month inflation sums improve persistence estimates and forecasts?

## Model

$$y_t = \mu + \alpha_t + \eta_t,$$
$$\alpha_{t+1} = \phi\alpha_t + \varepsilon_{t+1}.$$

The latent component $\alpha_t$ follows a stationary AR(1), with $|\phi|<1$ and
prior $\alpha_1\sim N(0,Q/(1-\phi^2))$. Independent Gaussian observation noise
$\eta_t$ has variance $H$; the state innovation $\varepsilon_t$ has variance $Q$.
The supplied decimal monthly rates are multiplied by 100 to obtain monthly
percentage points; they are not annualized.

Annual observations are rolling sums $z_t=\sum_{j=0}^{11}y_{t-j}$.
A 24-dimensional state carries twelve latent-state lags and twelve observation
shocks, accounting for the dependence introduced by overlapping windows. The
full derivation, joint stationary prior and system matrices appear in Notebook 04
and the report. Estimation uses the Kalman innovation likelihood; reported SEs
use the full likelihood Hessian and the delta method.

## Workflow

1. Specify the monthly latent AR(1) model and stationary prior.
2. Validate estimation on simulated samples of 300, 3,000 and 300,000 months.
3. Estimate historical monthly inflation and inspect filtered and smoothed states.
4. Construct and validate the 24-state overlapping annual-observation model.
5. Compare forecasts of the next complete twelve-month sum on common targets.
6. Diagnose economic persistence using four simulated paths and annual correlations.
7. Calibrate parameter standard errors with 200 Monte Carlo replications at T=936.

The Monte Carlo appendix is a supplementary extension, separate from the six
formal coursework tasks. Every attempt and its validity flags are retained.

## Key Results

Estimates are in monthly percentage-point units; shock parameters are standard deviations.

| Fit | Intercept $\mu$ | Latent persistence $\phi$ | State SD $\sqrt{Q}$ | Observation SD $\sqrt{H}$ | $\phi^{12}$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| Monthly observations | 0.28716 | 0.75269 | 0.20431 | 0.23385 | 0.03306 |
| Annual observations | 0.28740 | 0.87010 | 0.13252 | 0.25965 | 0.18830 |

| Future twelve-month forecast | RMSE (pp) | MAE (pp) |
| --- | ---: | ---: |
| Monthly fit | 2.38659 | 1.76091 |
| Annual-observation fit | 2.20921 | 1.60944 |
| Current annual sum benchmark | 2.43691 | 1.67285 |

| Annual lag-12 correlation $\operatorname{corr}(z_t,z_{t-12})$ | Value |
| --- | ---: |
| Historical sample | 0.60718 |
| Monthly-fit implied | 0.16905 |
| Annual-fit implied | 0.33895 |

The annual-observation fit yields greater latent persistence and lower retrospective
RMSE and MAE. The monthly fit improves on the benchmark in RMSE but has higher MAE.
Both models materially understate the historical correlation between annual windows
that share no months. Successful numerical validation therefore does not establish
complete economic adequacy, and observation correlation differs from $\phi^{12}$.

Forecasts use filtered states and propagate twelve months without intervening
observation updates. Parameters are estimated from the full historical sample,
so this is a retrospective comparison, not genuine out-of-sample evidence.

## Repository Structure

| Path | Contents |
| --- | --- |
| `notebooks/01_Simulate_Monthly_Model.ipynb` | Monthly specification, stationary prior and simulation plot. |
| `notebooks/02_Estimate_Simulated_Data.ipynb` | Three simulation MLEs, convergence and SEs; complete 200-replication supplementary appendix. |
| `notebooks/03_Estimate_Actual_Monthly_Data.ipynb` | CSV audit, monthly MLE, filtering, smoothing and economic interpretation. |
| `notebooks/04_Construct_Annual_Model.ipynb` | Explicit augmented matrices, joint prior and construction checks. |
| `notebooks/05_Estimate_Annual_Model_and_Forecast.ipynb` | Annual simulation validation, independent historical fits and 913 common forecasts. |
| `notebooks/06_Simulate_and_Diagnose.ipynb` | Independent fits, four economic simulations and annual persistence diagnosis. |
| `data/US_inflation47_25.csv` | Unmodified course-supplied monthly data snapshot; the filename ends in 25, but the sample ends in 2024. |
| `report/Inflation_State_Space_Report.pdf` | Final research report, copied without modification. |
| `docs/AI_Prompts_and_Material_Corrections.pdf` | Key AI prompts and material mathematical and implementation corrections. |
| `scripts/run_all_notebooks.py` | Sequential execution in six independent kernels, saving embedded results. |
| `REPRODUCIBILITY_CHECK.md` | Actual clean-install, execution and numerical comparison record. |

Each notebook includes its own required functions and can run independently.
No source module or results from another notebook are needed. Figures and tables
are embedded in executed notebooks rather than duplicated in separate output files.

## Reproducing the Results

Use Python 3.12 and run from the repository root:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
```

On Apple Silicon macOS, install the verified OpenBLAS wheels before the other
requirements. These retain the pinned package versions; this branch addresses
numerical problems observed in a different BLAS configuration during development,
without establishing an upstream library defect.

```sh
python -m pip download --no-cache-dir --only-binary=:all: --no-deps \
  --platform macosx_12_0_arm64 --python-version 312 --implementation cp --abi cp312 \
  --dest .wheels numpy==2.2.6 scipy==1.15.3
python -m pip install --no-index --no-deps \
  .wheels/numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl \
  .wheels/scipy-1.15.3-cp312-cp312-macosx_12_0_arm64.whl
```

On other platforms, proceed directly to the requirements installation. Then run:

```sh
python -m pip install -r requirements.txt
python -m pip check
python scripts/run_all_notebooks.py
```

The script uses the interpreter that launched it, creates a new kernel for each
notebook, stops with a nonzero exit code on the first failure, and saves successful
outputs. It runs all three simulation lengths and all 200 Monte Carlo attempts.
Numba accelerates the likelihood; notebook-defined functions use `cache=False`
and compile in each new kernel. Allow the full analysis to finish: runtime varies
by machine, and the long simulation and repeated fits can take substantial time.

For interactive work, use an existing Jupyter or VS Code frontend, select this
virtual environment and start the notebook kernel in `notebooks/`. Each notebook
reads `../data/US_inflation47_25.csv`. An optional local kernel registration is:

```sh
python -m ipykernel install --prefix .venv --name inflation-state-space \
  --display-name "Inflation state-space (Python 3.12)"
JUPYTER_PATH="$PWD/.venv/share/jupyter" jupyter lab notebooks/
```

The frontend is optional; the reproduction script needs no Jupyter server.
The verified platform is macOS 26.6.2 on Apple Silicon, Python 3.12.14, NumPy 2.2.6
and SciPy 1.15.3 with OpenBLAS. Linux, Windows and Intel macOS clean installations
have not been verified. Windows uses `.venv\Scripts\python.exe` and the corresponding
activation command. Initial installation requires internet access.

## Authors

QIDIAN XING  
MICHAEL SUHERMAN  
GUS GUENTHER  
ENDI ZONANA

## Course Context

MGMTMFE 431 — Advanced Data Analytics and AI  
UCLA Anderson School of Management

This project uses the supplied historical data snapshot. Its upstream provenance
and a separate dataset redistribution license were not specified in the supplied
materials. Instructor assignment documents, slides and private development records
are excluded from this repository.

## AI Assistance

AI was used as a research and coding assistant for model derivation, implementation,
debugging and verification. Key prompts and material corrections are documented
in [AI Prompts and Material Corrections](docs/AI_Prompts_and_Material_Corrections.pdf).

## Academic-use Note

This repository documents completed coursework and is provided for research and
educational reference. It should not be submitted as another student's coursework.
