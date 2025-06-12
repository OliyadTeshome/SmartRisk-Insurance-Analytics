import argparse
from src import data_loader, regression_model, utils

def main(config_path: str):
    config = utils.load_config(config_path)
    utils.setup_logging()
    df = data_loader.load_data(config['data_path'])
    df = data_loader.clean_data(df)
    model = regression_model.ZipcodeRegressionModel()
    model.fit(df, config['zipcode_col'], config['X_cols'], config['y_col'])
    print(f"Trained regression models for zip codes: {list(model.models.keys())}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Regression by Zip Code")
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()
    main(args.config) 