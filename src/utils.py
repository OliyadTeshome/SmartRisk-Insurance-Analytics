import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import ttest_ind, ttest_1samp, chi2_contingency

sns.set(style="whitegrid")

def plot_loss_ratio_by_category(df, category_col, title="Loss Ratio by Category"):
    df = df.copy()
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"].replace(0, pd.NA)
    grouped = df.groupby(category_col)["TotalClaims", "TotalPremium"].sum()
    grouped["LossRatio"] = grouped["TotalClaims"] / grouped["TotalPremium"]
    grouped = grouped.sort_values("LossRatio", ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=grouped.index, y=grouped["LossRatio"], palette="viridis")
    plt.title(title)
    plt.ylabel("Loss Ratio")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_claim_severity_distribution(df, title="Claim Severity Distribution"):
    df = df[df["TotalClaims"] > 0].copy()
    plt.figure(figsize=(10, 6))
    sns.histplot(df["TotalClaims"], bins=50, kde=True, color="darkorange")
    plt.title(title)
    plt.xlabel("Total Claims")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def plot_claim_frequency_by_category(df, category_col, title="Claim Frequency by Category"):
    df = df.copy()
    df["HasClaim"] = df["TotalClaims"] > 0
    freq = df.groupby(category_col)["HasClaim"].mean().sort_values(ascending=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=freq.index, y=freq.values, palette="Blues_d")
    plt.title(title)
    plt.ylabel("Claim Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_boxplot(df, numerical_col, group_col, title="Boxplot"):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=group_col, y=numerical_col, data=df, palette="Set2")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_barplot(df, category_col, value_col, title=None):
    """
    Create a bar plot for categorical variables.
    
    Args:
        df (pd.DataFrame): Input dataframe
        category_col (str): Column name for categories
        value_col (str): Column name for values to plot
        title (str, optional): Plot title
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(x=category_col, y=value_col, data=df, palette="viridis")
    if title:
        plt.title(title)
    else:
        plt.title(f'{value_col} by {category_col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
