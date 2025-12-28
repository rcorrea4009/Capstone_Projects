import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class HeartPipeline:
    def __init__(self, config):
        self.config = config
        self.model = RandomForestClassifier(
            n_estimators=config['model']['n_estimators'],
            max_depth=config['model']['max_depth']
        )

        self.preprocessor = ColumnTransformer([
            ('num', StandardScaler(), config['features']['numerical']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), config['features']['categorical'])
        ])

        self.pipeline = Pipeline([
            ('prep', self.preprocessor),
            ('clf', self.model)
        ])

    def fit(self, X, y):
        self.pipeline.fit(X, y)
        return self

    def predict(self, X):
        return self.pipeline.predict(X)

    def predict_proba(self, X):
        return self.pipeline.predict_proba(X)

    def feature_importance(self):
        feature_names = self.config['features']['numerical'] + self.config['features']['categorical']
        importances = self.model.feature_importances_
        return sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)

    def save(self):
        with open('artifacts/heart_pipeline.pkl', 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load():
        with open('artifacts/heart_pipeline.pkl', 'rb') as f:
            return pickle.load(f)
