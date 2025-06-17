# scripts

This folder contains command-line interface (CLI) scripts for running various stages of the data science pipeline, including data download, EDA, modeling, and reporting.

## Contents
- `download_data.py` / `download_data.sh`: Download and set up data using DVC and Google Drive.
- `run_eda.py`: Run exploratory data analysis.
- `run_ab_tests.py`: Execute A/B testing procedures.
- `train_regression.py`: Train regression models by zip code.
- `train_premium_model.py`: Train machine learning models for premium prediction.
- `generate_report.py`: Generate summary reports from analysis and modeling.

> **Note:** Scripts are designed to be run from the command line and use configuration files from the `configs/` folder. 