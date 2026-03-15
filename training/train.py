import pandas as pd
import mlflow
import mlflow.sklearn
import bentoml

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/iris.csv")

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

mlflow.set_experiment("iris_experiment")

with mlflow.start_run():

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")

    bentoml.sklearn.save_model("iris_model", model)

print("Model saved successfully")