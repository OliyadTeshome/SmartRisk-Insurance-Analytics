import pandas as pd
from src import ab_testing

def test_ab_ttest():
    df = pd.DataFrame({
        'group': ['A', 'A', 'B', 'B'],
        'value': [1.0, 2.0, 3.0, 4.0]
    })
    result = ab_testing.ab_ttest(df, 'group', 'value', 'A', 'B')
    assert 't_stat' in result and 'p_value' in result 