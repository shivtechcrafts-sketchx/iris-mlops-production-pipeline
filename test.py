import requests

data = [[5.1,3.5,1.4,0.2]]

response = requests.post(
    "http://localhost:3000/predict",
    json=data
)

print(response.json())