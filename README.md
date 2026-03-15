# 🌸 Iris MLOps Production Pipeline

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=180&section=header&text=Iris%20MLOps%20Pipeline&fontSize=40&fontColor=ffffff"/></p><p align="center"><img src="https://readme-typing-svg.herokuapp.com?color=00F7FF&size=25&center=true&vCenter=true&width=700&lines=End-to-End+Machine+Learning+Deployment;MLflow+Experiment+Tracking;BentoML+Model+Serving;FastAPI+Backend+API;Streamlit+Interactive+UI"/></p>


🚀 Project Overview

This project demonstrates a complete MLOps workflow for deploying a Machine Learning model into a production-ready system.

Instead of only training a model, this project shows the full lifecycle of an ML system:

- Model Training
- Experiment Tracking
- Model Packaging
- API Development
- UI Integration
- End-to-End Prediction Pipeline

The model predicts the species of an Iris flower based on four features.

---

🧠 Machine Learning Problem

The Iris dataset contains measurements of iris flowers.

Input Features

Feature| Description
Sepal Length| Length of sepal
Sepal Width| Width of sepal
Petal Length| Length of petal
Petal Width| Width of petal

Target Classes

0 → Setosa
1 → Versicolor
2 → Virginica

---

⚙️ MLOps Architecture

            ┌─────────────────────┐
            │    Streamlit UI     │
            │  User Input Layer   │
            └──────────▲──────────┘
                       │
                       │
            ┌──────────┴──────────┐
            │       FastAPI       │
            │     REST Backend    │
            └──────────▲──────────┘
                       │
                       │
            ┌──────────┴──────────┐
            │       BentoML       │
            │    Model Server     │
            └──────────▲──────────┘
                       │
                       │
            ┌──────────┴──────────┐
            │   ML Model (SKL)    │
            │  Iris Classifier    │
            └─────────────────────┘

---

🔬 Experiment Tracking

Experiments are tracked using MLflow

Dataset
   ↓
Model Training
   ↓
MLflow Logging
   ↓
Model Registry

This allows tracking:

- Model metrics
- Training parameters
- Experiment history

---

🧩 Tech Stack

<p align="center"><img src="https://skillicons.dev/icons?i=python,fastapi,docker,git" /></p>Tool| Purpose
Python| Core programming language
MLflow| Experiment tracking
BentoML| Model serving
FastAPI| Backend API
Streamlit| User interface
Docker| Deployment container

---

📂 Project Structure

iris-mlops-production-pipeline
│
├── training
│   └── train.py
│
├── bentoml_service
│   └── service.py
│
├── fastapi_app
│   └── main.py
│
├── streamlit_app
│   └── app.py
│
├── data
│   └── iris.csv
│
├── requirements.txt
├── Dockerfile
└── README.md

---

▶️ How to Run the Project

1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/iris-mlops-production-pipeline
cd iris-mlops-production-pipeline

---

2️⃣ Install Dependencies

pip install -r requirements.txt

---

3️⃣ Train Model

python training/train.py

---

4️⃣ Start BentoML Server

bentoml serve bentoml_service.service:svc

---

5️⃣ Start FastAPI

python -m uvicorn fastapi_app.main:app --reload

---

6️⃣ Run Streamlit UI

streamlit run streamlit_app/app.py

---

🌐 Application URLs

Service| URL
Streamlit UI| http://localhost:8501
FastAPI Docs| http://127.0.0.1:8000/docs
BentoML Server| http://localhost:3000

---

✨ Features

✔ End-to-End ML Pipeline
✔ MLflow Experiment Tracking
✔ BentoML Model Serving
✔ FastAPI REST API
✔ Streamlit Interactive UI

---

🔮 Future Improvements

- Docker deployment
- CI/CD pipeline
- Cloud deployment
- Model monitoring

---

👨‍💻 Author

Shiv Kumavat

Built with ❤️ using Python & MLOps tools.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,100:0f2027&height=120&section=footer"/></p>
