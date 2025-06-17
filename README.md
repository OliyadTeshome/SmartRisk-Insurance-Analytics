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
├── dvc_storage/    # DVC-tracked data files ([README](dvc_storage/README.md))
├── notebooks/      # Jupyter notebooks for EDA, modeling, and reporting ([README](notebooks/README.md))
├── src/            # Python modules (data processing, modeling, etc.) ([README](src/README.md))
├── scripts/        # CLI scripts for each stage ([README](scripts/README.md))
├── tests/          # Unit tests for key modules ([README](tests/README.md))
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
- pandas, numpy, scikit-learn, matplotlib, seaborn, xgboost, pytest, dvc[gdrive], gdown

## License
MIT License

## Credits
Developed by the Data Science Team at AlphaCare Insurance Solutions (ACIS).

## Data Version Control (DVC) Setup

This project uses DVC to manage the dataset stored on Google Drive. The dataset is not stored in Git but is tracked using DVC.

### Prerequisites

1. Install DVC and its dependencies:
```bash
pip install -r requirements.txt
```

2. Authenticate with Google Drive:
   - You'll need to authenticate with Google Drive the first time you pull the data
   - Follow the prompts in your browser when running the download script

### Downloading the Data

You can download the data using either of these methods:

1. Using the shell script:
```bash
chmod +x scripts/download_data.sh
./scripts/download_data.sh
```

2. Using the Python script:
```bash
python scripts/download_data.py
```

The data will be downloaded to `data/raw/insurance_data.csv`.

### Data Structure

```
data/
├── raw/           # Original, immutable data
│   └── insurance_data.csv
└── processed/     # Cleaned and processed data
```

### Working with DVC

- To update the data: `dvc pull`
- To check data status: `dvc status`
- To see data changes: `dvc diff`

Note: The actual data files are gitignored, but the `.dvc` files are tracked in Git to maintain version control of the data. 