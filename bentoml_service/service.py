import bentoml
import numpy as np

# load model
model = bentoml.sklearn.get("iris_model:latest").load_model()

# create service
svc = bentoml.Service("iris_classifier")

@svc.api(input=bentoml.io.NumpyNdarray(), output=bentoml.io.NumpyNdarray())
def predict(input_array: np.ndarray):

    prediction = model.predict(input_array)

    return prediction