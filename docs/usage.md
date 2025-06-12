# Usage Guide

## Running Scripts

- EDA:
  ```bash
  python scripts/run_eda.py --config configs/eda_config.yaml
  ```
- A/B Testing:
  ```bash
  python scripts/run_ab_tests.py --config configs/ab_test_config.yaml
  ```
- Regression:
  ```bash
  python scripts/train_regression.py --config configs/regression_config.yaml
  ```
- Premium Model:
  ```bash
  python scripts/train_premium_model.py --config configs/premium_model_config.yaml
  ```
- Report:
  ```bash
  python scripts/generate_report.py --config configs/report_config.yaml
  ```

## Running Notebooks

Open any notebook in the `notebooks/` directory using Jupyter:
```bash
jupyter notebook
``` 