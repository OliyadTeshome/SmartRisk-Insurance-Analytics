import argparse
from src import data_loader, ab_testing, utils

def main(config_path: str):
    config = utils.load_config(config_path)
    utils.setup_logging()
    df = data_loader.load_data(config['data_path'])
    df = data_loader.clean_data(df)
    for test in config['ab_tests']:
        result = ab_testing.ab_ttest(df, test['group_col'], test['value_col'], test['group_a'], test['group_b'])
        print(f"A/B Test {test['group_col']} ({test['group_a']} vs {test['group_b']}): {result}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run A/B Tests")
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()
    main(args.config) 