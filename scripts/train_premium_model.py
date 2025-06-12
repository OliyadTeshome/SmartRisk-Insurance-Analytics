import argparse
from src import data_loader, premium_predictor, utils

def main(config_path: str):
    config = utils.load_config(config_path)
    utils.setup_logging()
    df = data_loader.load_data(config['data_path'])
    df = data_loader.clean_data(df)
    X = df[config['X_cols']]
    y = df[config['y_col']]
    model = premium_predictor.PremiumPredictor(model_type=config.get('model_type', 'random_forest'))
    model.fit(X, y)
    print(f"Trained premium prediction model: {model.model}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Premium Prediction Model")
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()
    main(args.config) 