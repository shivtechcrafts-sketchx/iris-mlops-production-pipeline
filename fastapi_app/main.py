from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

BENTO_URL = "http://localhost:3000/predict"


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def home():
    return {"message": "Iris Prediction API"}


@app.post("/predict")
def predict(data: IrisInput):

    payload = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    response = requests.post(
        BENTO_URL,
        json=payload
    )

    result = response.json()

    return {"prediction": result}

    