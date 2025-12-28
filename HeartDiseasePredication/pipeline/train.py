import yaml, os
import pandas as pd
from pipeline import HeartPipeline
from sklearn.metrics import accuracy_score

os.makedirs('artifacts', exist_ok=True)

raw_config = yaml.safe_load(open('HeartDiseasePredication\\pipeline\\config.yaml'))

config = {
    "model": raw_config["model"],
    "features": {
        "numerical": raw_config["features"]["numerical"],
        "categorical": raw_config["features"]["categorical"]
    }
}

df = pd.read_csv('../Data/values.csv') 


labels = pd.read_csv('../Data/labels.csv')
y = labels.iloc[:180, 1].values  

X = df[config['features']['numerical'] + config['features']['categorical']]

hp = HeartPipeline(config)
hp.fit(X, y)

print("Accuracy:", accuracy_score(y, hp.predict(X)))
print("Feature Importance:", hp.feature_importance())

hp.save()
print("Pipeline Saved Successfully!")
