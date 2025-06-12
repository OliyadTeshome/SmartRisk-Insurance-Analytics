import argparse
from src import data_loader, eda, utils

def main(config_path: str):
    config = utils.load_config(config_path)
    utils.setup_logging()
    df = data_loader.load_data(config['data_path'])
    df = data_loader.clean_data(df)
    summary = eda.eda_summary(df)
    print(summary)
    for col in config.get('eda_columns', []):
        eda.plot_distribution(df, col)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run EDA")
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()
    main(args.config) 