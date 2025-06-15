import pytest
import pandas as pd
import numpy as np
from src.utils import (
    plot_loss_ratio_by_category,
    plot_claim_severity_distribution,
    plot_claim_frequency_by_category,
    plot_boxplot
)

def test_plot_loss_ratio_by_category():
    # Create sample data
    data = {
        'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
        'TotalClaims': [1000, 2000, 1500, 1200, 1800, 1600],
        'TotalPremium': [5000, 8000, 7000, 6000, 9000, 7500]
    }
    df = pd.DataFrame(data)
    
    # Test function execution
    plot_loss_ratio_by_category(df, 'Category')
    
def test_plot_claim_severity_distribution():
    # Create sample data
    data = {
        'TotalClaims': np.random.gamma(2, 1000, 1000)
    }
    df = pd.DataFrame(data)
    
    # Test function execution
    plot_claim_severity_distribution(df)
    
def test_plot_claim_frequency_by_category():
    # Create sample data
    data = {
        'Category': ['A', 'B', 'C'] * 100,
        'TotalClaims': np.random.choice([0, 1000], 300)
    }
    df = pd.DataFrame(data)
    
    # Test function execution
    plot_claim_frequency_by_category(df, 'Category')
    
def test_plot_boxplot():
    # Create sample data
    data = {
        'Category': ['A', 'B', 'C'] * 50,
        'Value': np.random.normal(100, 20, 150)
    }
    df = pd.DataFrame(data)
    
    # Test function execution
    plot_boxplot(df, 'Value', 'Category')
