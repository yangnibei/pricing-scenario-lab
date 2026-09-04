# Pricing Scenario Lab

**Yang Nibei · Business Analytics Portfolio · 10 / 10**

> How sensitive is contribution profit to price and demand assumptions?

[Portfolio](https://github.com/yangnibei) · [Results & decisions](REPORT.md) · [Python analysis](analysis.py)

![Pricing Scenario Lab: reproducible analysis](analysis.svg)

## Business brief

This explicitly synthetic decision lab explores a focused business question using **Constant-elasticity scenarios, break-even economics, sensitivity analysis**. Read the results alongside their assumptions before acting on them.

## Approach

Constant-elasticity scenarios, break-even economics, sensitivity analysis. The implementation contains input and reconciliation assertions. Each run writes an aggregate report, machine-readable metrics and the chart shown above.

## Reproduce

Python 3.11+ recommended. From this repository:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest -v
python analysis.py
```

On Windows, activate with `.venv\\Scripts\\activate`. Use `--data-dir /absolute/path/to/cache` and `--output-dir /absolute/path/to/results` to keep downloads and regenerated outputs elsewhere. The first public-data run requires internet access. Raw data stays in the ignored `data/` directory; it is not redistributed in this repository. Runs reuse cached archives and record their SHA-256 hashes in `results.json`.

## Data & attribution

Generated locally by the documented model and fixed random seed (where randomness applies). No external data or private information.

## Limitations

Prices, costs and elasticities are explicit assumptions, not estimated market facts or a deployable pricing recommendation.

This repository is an educational portfolio case study, not paid client work, employment evidence or a production system. Code and documentation were developed with AI assistance and executed against the stated data; that does not imply independent third-party validation.

## Repository guide

- `analysis.py`: project-specific calculations and checks.
- `utils.py`: download, provenance and reporting helpers.
- `test_analysis.py`: offline helper unit tests.
- `REPORT.md`: generated findings and decision boundaries.
- `results.json`: aggregate metrics and source provenance.
- `analysis.svg`: reproducible figure.

