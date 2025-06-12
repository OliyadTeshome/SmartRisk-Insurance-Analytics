# SmartRisk-Insurance-Analytics

**A predictive analytics and risk modeling toolkit for auto insurance in South Africa**

## Business Context
AlphaCare Insurance Solutions (ACIS) aims to optimize auto insurance premiums and attract low-risk customers using data-driven insights. This project provides a modular toolkit for risk profiling, A/B hypothesis testing, and predictive modeling tailored to the South African market.

## Problem Statement
How can ACIS leverage data science to accurately profile risk, test business hypotheses, and predict optimal premiums to maximize profitability while minimizing risk exposure?

## Project Structure
```
SmartRisk-Insurance-Analytics/
│
├── data/           # Raw and processed datasets
├── notebooks/      # Jupyter notebooks for EDA, modeling, and reporting
├── src/            # Python modules (data processing, modeling, etc.)
├── scripts/        # CLI scripts for each stage
├── tests/          # Unit tests for key modules
├── reports/        # Results, visuals, deliverables
├── configs/        # YAML/JSON config files
├── docs/           # Documentation
├── workflow/       # Automation scripts (Makefile, bash, etc.)
└── README.md       # Project overview
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SmartRisk-Insurance-Analytics.git
   cd SmartRisk-Insurance-Analytics
   ```
2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## How to Run
- **Scripts:**
  - EDA: `python scripts/run_eda.py --config configs/eda_config.yaml`
  - A/B Testing: `python scripts/run_ab_tests.py --config configs/ab_test_config.yaml`
  - Regression: `python scripts/train_regression.py --config configs/regression_config.yaml`
  - Premium Model: `python scripts/train_premium_model.py --config configs/premium_model_config.yaml`
  - Report: `python scripts/generate_report.py --config configs/report_config.yaml`
- **Notebooks:**
  - Open and run the notebooks in the `notebooks/` directory for stepwise analysis.

## Example Usage
```bash
python scripts/run_eda.py --config configs/eda_config.yaml
```

## Dependencies
- Python 3.8+
- pandas, numpy, scikit-learn, matplotlib, seaborn, xgboost, pyyaml, loguru, jupyter, pytest

## License
MIT License

## Credits
Developed by the Data Science Team at AlphaCare Insurance Solutions (ACIS). 