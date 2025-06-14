"""
Exploratory Data Analysis (EDA) module for SmartRisk Insurance Analytics.
Contains reusable functions for data analysis and visualization.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional
import yaml
import logging
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Set up logging
log_dir = Path('reports/logs')
log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_dir / 'eda.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def load_config(config_path: str = 'configs/eda_config.yaml') -> Dict:
    """Load EDA configuration from YAML file."""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def load_data(config: Dict) -> pd.DataFrame:
    """Load and perform initial data validation."""
    try:
        df = pd.read_csv(config['data_path'])
        logger.info(f"Successfully loaded data with shape: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise

def analyze_missing_values(df: pd.DataFrame, config: Dict) -> Tuple[pd.DataFrame, List[str]]:
    """
    Analyze missing values and identify columns to drop based on threshold.
    Returns cleaned dataframe and list of dropped columns.
    """
    missing_pct = (df.isnull().sum() / len(df)) * 100
    cols_to_drop = missing_pct[missing_pct > config['missing_threshold'] * 100].index.tolist()
    
    if cols_to_drop:
        logger.info(f"Dropping columns with >{config['missing_threshold']*100}% missing values: {cols_to_drop}")
        df = df.drop(columns=cols_to_drop)
    
    return df, cols_to_drop

def impute_missing_values(df: pd.DataFrame, config: Dict) -> pd.DataFrame:
    """Impute missing values based on column type."""
    for col in config['categorical_columns']:
        if col in df.columns and df[col].isnull().any():
            df[col] = df[col].fillna(df[col].mode()[0])
            logger.info(f"Imputed categorical column {col} with mode")
    
    for col in config['numerical_columns']:
        if col in df.columns and df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())
            logger.info(f"Imputed numerical column {col} with median")
    
    return df

def calculate_loss_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate loss ratio (TotalClaims/TotalPremium) for different groupings."""
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium']
    return df

def plot_loss_ratio_by_category(df: pd.DataFrame, category: str, config: Dict) -> None:
    """Plot loss ratio distribution by category."""
    plt.figure(figsize=tuple(config['plot_settings']['figure_size']))
    sns.set_style(config['plot_settings']['style'])
    sns.set_context(config['plot_settings']['context'])
    
    ax = sns.barplot(data=df, x=category, y='LossRatio', palette=config['plot_settings']['palette'])
    plt.title(f'Loss Ratio by {category}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save plot
    save_path = Path(config['output_paths']['plots']) / f'loss_ratio_{category.lower()}.png'
    plt.savefig(save_path, dpi=config['plot_settings']['dpi'])
    plt.close()
    logger.info(f"Saved loss ratio plot for {category} to {save_path}")

def analyze_outliers(df: pd.DataFrame, columns: List[str], config: Dict) -> Dict[str, Tuple[float, float]]:
    """Analyze outliers using IQR method and return bounds."""
    outlier_bounds = {}
    for col in columns:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outlier_bounds[col] = (lower_bound, upper_bound)
            
            # Plot outliers
            plt.figure(figsize=tuple(config['plot_settings']['figure_size']))
            sns.boxplot(data=df, y=col)
            plt.title(f'Outlier Analysis - {col}')
            plt.tight_layout()
            
            save_path = Path(config['output_paths']['plots']) / f'outliers_{col.lower()}.png'
            plt.savefig(save_path, dpi=config['plot_settings']['dpi'])
            plt.close()
            logger.info(f"Saved outlier plot for {col} to {save_path}")
    
    return outlier_bounds

def analyze_temporal_trends(df: pd.DataFrame, config: Dict) -> None:
    """Analyze temporal trends in claims and premiums."""
    # Convert TransactionMonth to datetime if not already
    if not pd.api.types.is_datetime64_any_dtype(df['TransactionMonth']):
        df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'])
    
    # Monthly trends
    monthly_stats = df.groupby(df['TransactionMonth'].dt.to_period('M')).agg({
        'TotalClaims': ['sum', 'count'],
        'TotalPremium': 'sum'
    }).reset_index()
    
    # Plot monthly trends
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=tuple(config['plot_settings']['figure_size']))
    
    # Claim frequency
    sns.lineplot(data=monthly_stats, x='TransactionMonth', y=('TotalClaims', 'count'), ax=ax1)
    ax1.set_title('Monthly Claim Frequency')
    ax1.tick_params(axis='x', rotation=45)
    
    # Claim severity
    monthly_stats['ClaimSeverity'] = monthly_stats[('TotalClaims', 'sum')] / monthly_stats[('TotalClaims', 'count')]
    sns.lineplot(data=monthly_stats, x='TransactionMonth', y='ClaimSeverity', ax=ax2)
    ax2.set_title('Monthly Claim Severity')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    save_path = Path(config['output_paths']['plots']) / 'temporal_trends.png'
    plt.savefig(save_path, dpi=config['plot_settings']['dpi'])
    plt.close()
    logger.info(f"Saved temporal trends plot to {save_path}")

def analyze_vehicle_claims(df: pd.DataFrame, config: Dict) -> None:
    """Analyze claims by vehicle make and model."""
    # Top 10 makes by total claims
    make_claims = df.groupby('VehicleMake')['TotalClaims'].agg(['sum', 'count']).reset_index()
    make_claims['AverageClaim'] = make_claims['sum'] / make_claims['count']
    make_claims = make_claims.sort_values('sum', ascending=False).head(10)
    
    # Plot top makes
    plt.figure(figsize=tuple(config['plot_settings']['figure_size']))
    sns.barplot(data=make_claims, x='VehicleMake', y='AverageClaim', palette=config['plot_settings']['palette'])
    plt.title('Top 10 Vehicle Makes by Average Claim Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    save_path = Path(config['output_paths']['plots']) / 'top_vehicle_makes.png'
    plt.savefig(save_path, dpi=config['plot_settings']['dpi'])
    plt.close()
    logger.info(f"Saved vehicle make analysis plot to {save_path}")
    
    # Save summary to CSV
    summary_path = Path(config['output_paths']['summaries']) / 'vehicle_claims_summary.csv'
    make_claims.to_csv(summary_path, index=False)
    logger.info(f"Saved vehicle claims summary to {summary_path}")

def generate_summary_report(df: pd.DataFrame, config: Dict) -> None:
    """Generate comprehensive summary report of the analysis."""
    summary = {
        'Dataset Shape': df.shape,
        'Numerical Summary': df[config['numerical_columns']].describe().to_dict(),
        'Categorical Summary': {col: df[col].value_counts().to_dict() 
                              for col in config['categorical_columns'] if col in df.columns},
        'Missing Values': df.isnull().sum().to_dict(),
        'Loss Ratio Summary': {
            'Overall': df['LossRatio'].mean(),
            'By Province': df.groupby('Province')['LossRatio'].mean().to_dict(),
            'By Gender': df.groupby('Gender')['LossRatio'].mean().to_dict()
        }
    }
    
    # Save summary to YAML
    summary_path = Path(config['output_paths']['summaries']) / 'eda_summary.yaml'
    with open(summary_path, 'w') as f:
        yaml.dump(summary, f, default_flow_style=False)
    logger.info(f"Saved EDA summary report to {summary_path}")

def eda_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a summary of the dataset including basic statistics.
    
    Args:
        df (pd.DataFrame): Input dataframe
        
    Returns:
        pd.DataFrame: Summary statistics
    """
    summary = pd.DataFrame({
        'count': df.count(),
        'mean': df.mean(numeric_only=True),
        'std': df.std(numeric_only=True),
        'min': df.min(numeric_only=True),
        '25%': df.quantile(0.25, numeric_only=True),
        '50%': df.quantile(0.5, numeric_only=True),
        '75%': df.quantile(0.75, numeric_only=True),
        'max': df.max(numeric_only=True)
    })
    return summary

def plot_distribution(df: pd.DataFrame, column: str, save_path: str = None) -> None:
    """
    Plot the distribution of a numerical column.
    
    Args:
        df (pd.DataFrame): Input dataframe
        column (str): Column name to plot
        save_path (str, optional): Path to save the plot. If None, plot is displayed.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=column, kde=True)
    plt.title(f'Distribution of {column}')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

def main():
    """Main function to run the complete EDA pipeline."""
    try:
        # Load configuration
        config = load_config()
        
        # Create output directories if they don't exist
        for path in config['output_paths'].values():
            Path(path).mkdir(parents=True, exist_ok=True)
        
        # Load and process data
        df = load_data(config)
        df, dropped_cols = analyze_missing_values(df, config)
        df = impute_missing_values(df, config)
        
        # Calculate loss ratio
        df = calculate_loss_ratio(df)
        
        # Generate plots and analysis
        for category in ['Province', 'Gender', 'VehicleType']:
            if category in df.columns:
                plot_loss_ratio_by_category(df, category, config)
        
        # Analyze outliers
        outlier_bounds = analyze_outliers(df, ['TotalClaims', 'TotalPremium'], config)
        
        # Analyze temporal trends
        analyze_temporal_trends(df, config)
        
        # Analyze vehicle claims
        analyze_vehicle_claims(df, config)
        
        # Generate summary report
        generate_summary_report(df, config)
        
        logger.info("EDA pipeline completed successfully")
        
    except Exception as e:
        logger.error(f"Error in EDA pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    main() 