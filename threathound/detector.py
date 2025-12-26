from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self, contamination=0.05, random_state=42):
        self.model = IsolationForest(
            contamination=contamination,
            random_state=random_state
        )

    def train(self, features: np.ndarray):
        self.model.fit(features)

    def detect(self, features: np.ndarray):
        return self.model.predict(features)
