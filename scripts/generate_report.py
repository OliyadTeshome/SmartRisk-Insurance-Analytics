import argparse
from src import utils

def main(config_path: str):
    config = utils.load_config(config_path)
    utils.setup_logging()
    print(f"Generating report using config: {config_path}")
    # Placeholder: Add report generation logic here

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Report")
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()
    main(args.config) 