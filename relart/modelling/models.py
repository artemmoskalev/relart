import numpy as np

class NaivePredictor:
    """This class represents a simple time series model.
    It returns the last seen time series value as the prediction for the next time step.
    Use fit/predict methods to forecast the times series."""
    def __init__(self):
        self.level = None
    
    # train NaivePredictor instance
    # @X - ndarray of features. Can be None.
    # @y - ndarray of training labels. Expected to be 1-dimensional.
    # @value - return the instance of NaivePredictor
    def fit(self, X, y):
        self.level = y.to_numpy().flatten()[-1]
        return self
    
    # forecast the next time step
    # @X - ndarray of features for the time steps where the forecast is needed
    #      Must be 2-dimensional.
    # @value - returns a 1-dimensional ndarray of forecast values
    def predict(self, X):
        yhat = np.ndarray((X.shape[0], ))
        yhat.fill(self.level)
        return yhat
