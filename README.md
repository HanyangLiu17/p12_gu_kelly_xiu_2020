# P12: Empirical Asset Pricing via Machine Learning

FINM 32800 final project: replication and update of Gu, Kelly, and Xiu (2020).

**Status: initial project scaffold. Replication results are not yet available.**

## Team

| Member | GitHub |
| --- | --- |
| Ivonne Li | [ivonnejq](https://github.com/ivonnejq) |
| Sally Cheng | [ChengSanli](https://github.com/ChengSanli) |
| Henry Liu | [HanyangLiu17](https://github.com/HanyangLiu17) |
| Jiarui Feng | [JiaruiFeng2004](https://github.com/JiaruiFeng2004) |

## Research question

Can machine learning improve out-of-sample stock return prediction by capturing
nonlinear interactions among firm characteristics and macroeconomic conditions?

## Replication and update

- [ ] Build 94 stock characteristics, eight macro predictors, industry dummies,
  and the macro-characteristic interactions with point-in-time discipline.
- [ ] Table 1: monthly out-of-sample stock-level predictive performance.
- [ ] Table 3: Diebold-Mariano forecast comparisons.
- [ ] Table 5: portfolio-level out-of-sample R-squared.
- [ ] Figures 4 and 5 and Table 4: characteristic and macro variable importance.
- [ ] Tables 7 and 8 and Figure 9: machine-learning portfolio performance.
- [ ] Update the evaluation through the latest month jointly supported by the
  required data sources; commit that end date after checking coverage.
- [ ] Publish the report, cleaned-data tour notebook, and ChartBook site.

The initial replication dates are March 1957 through December 2016, with
out-of-sample evaluation beginning in 1987. Do not randomly shuffle time periods.

## Extension (proposed; awaiting consultation agreement)

Build a configurable data-availability stress-testing module. At prediction
time, impose additional one- and three-month accounting-data delays and
pre-specified, fixed-seed missingness scenarios. Keep trained models fixed,
apply the baseline imputation procedure, and recompute predictions and
portfolios. Compare predictive R-squared, stock rankings, returns, and Sharpe
ratios in ChartBook comparison pages.

This is a proposal, not an approved scope or a completed implementation.
After the consultation, record the agreed scenarios, models, acceptance
criteria, computing reductions, and meeting date in this section. The sample
update and this extension are separate deliverables.

## Data and validation

| Source | Purpose | Access |
| --- | --- | --- |
| CRSP on WRDS | Stock returns, market equity, trading characteristics | Licensed |
| Compustat and CRSP-Compustat links on WRDS | Accounting characteristics and firm links | Licensed |
| Amit Goyal's website | Welch-Goyal macro predictors | Public |
| Dacheng Xiu's supporting materials | Characteristic definitions and reference checks | Public, subject to availability |

Validation will check stock-month uniqueness, link validity, availability-date
lags, time splits, filter counts, and missingness/coverage over time. Reconcile
selected characteristics with independent references where available. Set
tolerances before inspecting replication results. Produce a coverage table
and an annual coverage figure with explanatory captions.

Raw licensed data, passwords, tokens, and local `.env` files must stay outside
Git. No data access credentials are required to run the initial scaffold checks.

## Setup and run

Use Python 3.12. From a clean clone:

```bash
git clone https://github.com/HanyangLiu17/p12_gu_kelly_xiu_2020.git
cd p12_gu_kelly_xiu_2020
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

For the initial scaffold checks:

```bash
python -m pip install -r requirements-ci.txt
python -m doit
```

For the full template environment, install `requirements.txt` instead. LaTeX
reports will also require a LaTeX distribution. Copy `.env.example` to a local
`.env` and enter your own WRDS username when developing the data pulls.
Keep analysis dates in `src/settings.py`, not in `.env`.

Available tasks:

```bash
python -m doit list
python -m doit config
python -m doit tests
python -m doit site  # requires ChartBook from requirements.txt
```

Currently, the default pipeline creates local directories and runs inherited
template helper tests. It does **not** yet download the research panel, train
models, or reproduce the paper. Add those tasks as the project is implemented.
The `site` task builds the current project documentation to `docs/`; GitHub
Pages publication is a later project milestone.

## Repository structure

- `src/`: settings, template helpers, and data-source examples; project cleaning
  and analysis should live in separate modules here.
- `dodo.py`: initial PyDoit entry point.
- `reports/`: LaTeX templates; replace example content with the project report.
- `docs_src/` and `chartbook.toml`: ChartBook documentation and artifact registry.
- `_data/` and `_output/`: ignored local data and generated outputs.
- `.github/`: scaffold checks and pull request checklist.

The scaffold retains optional template examples. They are not project results
and are not part of the default pipeline. `requirements.txt` is the authoritative
installation file for this project's pip workflow.

## Collaboration and submission

Use feature branches and pull requests. Each PR must be reviewed by another
group member before merging. Each member should author a merged PR and review
a teammate's PR. Everyone should understand the full pipeline.

The graded version is `main` as it stands 24 hours before the final meeting.
The final project must run from a clean clone following this README alone.

## Template provenance

Generated with `cruft create` from
[cookiecutter_chartbook](https://github.com/backofficedev/cookiecutter_chartbook).
The template commit and rendering context are recorded in `.cruft.json`.
Post-generation cleanup hooks were disabled to preserve optional template files.

## Reference and course requirements

Gu, Shihao, Bryan Kelly, and Dacheng Xiu. 2020. "Empirical Asset Pricing via
Machine Learning." *The Review of Financial Studies* 33(5): 2223-2273.
[DOI](https://doi.org/10.1093/rfs/hhaa009).

- [Project description](https://finm-32800.github.io/FinalProject/potential_final_projects.html)
- [Final project rubric](https://finm-32800.github.io/FinalProject/final_project_rubric.html)
