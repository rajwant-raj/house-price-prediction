# house-price-prediction
# 🏠 House Price Prediction ML Project with gradio

This project uses a Machine Learning model to predict house prices based on features such as area, number of bedrooms, and bathrooms. The model is trained using a housing dataset and deployed using a Gradio web app.

Predict the price of a house based on area, bedrooms, and bathrooms using a trained machine learning model — all wrapped in a simple, user-friendly Gradio app.

📌 What’s Inside
This project does 3 main things:

📊 Uses a dataset (Housing.csv) to train a model

🧠 Predicts house prices using features like area, bedrooms, and bathrooms

🌐 Launches a Gradio web app so anyone can use it without writing code

🎯 Features
No coding needed — just run and interact!

Fast, real-time predictions in your browser

Clean Gradio interface

Uses LinearRegression from scikit-learn

🧠 Model Input & Output
Inputs:

📏 Area (in sq. feet)

🛏 Bedrooms

🛁 Bathrooms

Output:

💰 Predicted House Price (in ₹)


---

## 📂 Project Structure

house_price_prediction/
│
├── app.py # Streamlit app
├── model.pkl # Trained ML model (Linear Regression)
├── Housing.csv # Dataset used for training
├── requirements.txt # Python dependencies
└── README.md # Project overview

yaml
Copy
Edit

---

## 🚀 Features

- 📈 Trains a regression model to predict house prices
- 🧠 Uses `LinearRegression` from Scikit-learn
- 🌐 Deploys a live prediction UI using Streamlit
- ✅ Supports real-time predictions with user input

---

## 📊 Dataset Description

`Housing.csv` contains sample housing data. Key features:

- `area`: Area in square feet
- `bedrooms`: Number of bedrooms
- `bathrooms`: Number of bathrooms
- `price`: Target variable (House price in ₹)

---

## 🧠 Model Used

- Algorithm: `LinearRegression`
- Library: `scikit-learn`
- Metrics:
  - MAE
  - RMSE
  - R² Score

---
🛠️ How to Run the App
1. Clone or download this repo
bash
Copy
Edit
git clone https://github.com/yourusername/house-price-gradio.git
cd house-price-gradio
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the app
bash
Copy
Edit
python app.py
Gradio will open a link in your browser like:
http://127.0.0.1:7860

🙌 Author
AI/ML Enthusiast 🚀
rajwamt-raj 

📬 Contact
LinkedIn: [your-linkedin-url]
