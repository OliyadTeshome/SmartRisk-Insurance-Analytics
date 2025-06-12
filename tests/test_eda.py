import pandas as pd
from src import eda

def test_eda_summary():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    summary = eda.eda_summary(df)
    assert 'a' in summary.columns or 'a' in summary.index

def test_plot_distribution(tmp_path):
    df = pd.DataFrame({'a': [1, 2, 2, 3, 3, 3]})
    eda.plot_distribution(df, 'a', save_path=str(tmp_path / 'plot.png')) 