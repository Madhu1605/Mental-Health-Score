# 🧠 Mental Health Score Prediction

## 🚀 Live Demo

👉 [Try the Mental Health Score Prediction App](https://mental-health-score123.streamlit.app/)

## 📌 About the Project

Mental Health Score Prediction is a Machine Learning project that predicts an estimated mental health score based on information related to a user's personal profile, academic background, digital habits, lifestyle, and stress level.

The project provides an interactive web application where users can enter their information and receive a predicted mental health score out of 10.

## ✨ Features

- 🧠 Mental health score prediction
- 👤 Personal profile inputs
- 🎓 Academic and digital habit inputs
- 📱 Daily screen-time and phone-unlock tracking
- 🏃 Lifestyle information
- 😓 Stress-level selection
- ⚡ FastAPI backend for prediction
- 🎨 Interactive Streamlit frontend
- ☁️ Deployed online

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- FastAPI
- Pydantic
- Uvicorn
- Streamlit
- Requests
- Jupyter Notebook

## 📊 Input Features

The application uses the following information:

| Category | Features |
|---|---|
| Personal Profile | Age, Gender, Country |
| Academic | Academic Level |
| Digital Habits | Screen Time, Daily Phone Unlocks, Most-used Platform |
| Usage Purpose | Networking, Education, Entertainment, News |
| Lifestyle | Study Hours, Physical Activity, Sleep |
| Stress | Low, Medium, High, Very High |

## ⚙️ How It Works

```text
User Input
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
Trained Machine Learning Model
    ↓
Predicted Mental Health Score
    ↓
Result displayed to the user