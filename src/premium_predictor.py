import pandas as pd
from typing import Any, Optional
from sklearn.ensemble import RandomForestRegressor
try:
    from xgboost import XGBRegressor
    xgb_available = True
except ImportError:
    xgb_available = False

class PremiumPredictor:
    """
    Machine learning model to predict premium values.
    """
    def __init__(self, model_type: str = 'random_forest', **kwargs):
        if model_type == 'xgboost' and xgb_available:
            self.model = XGBRegressor(**kwargs)
        else:
            self.model = RandomForestRegressor(**kwargs)

    def fit(self, X: pd.DataFrame, y: pd.Series) -> None:
        """
        Fit the model to the data.
        """
        self.model.fit(X, y)

    def predict(self, X: pd.DataFrame) -> Any:
        """
        Predict premium values.
        """
        return self.model.predict(X) 