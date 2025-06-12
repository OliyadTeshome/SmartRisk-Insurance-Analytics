import pandas as pd
from sklearn.linear_model import LinearRegression
from typing import Tuple, Any

class ZipcodeRegressionModel:
    """
    Linear regression model by zip code.
    """
    def __init__(self):
        self.models = {}

    def fit(self, df: pd.DataFrame, zipcode_col: str, X_cols: list, y_col: str) -> None:
        """
        Fit a linear regression model for each zip code.
        """
        for zipcode, group in df.groupby(zipcode_col):
            X = group[X_cols]
            y = group[y_col]
            model = LinearRegression()
            model.fit(X, y)
            self.models[zipcode] = model

    def predict(self, zipcode: Any, X: pd.DataFrame) -> Any:
        """
        Predict using the model for a specific zip code.
        """
        model = self.models.get(zipcode)
        if model is None:
            raise ValueError(f"No model found for zipcode {zipcode}")
        return model.predict(X) 