import gradio as gr
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("house-price-prediction\model.pkl", "rb"))

# Define prediction function
def predict(area, bedrooms, bathrooms):
    input_df = pd.DataFrame([[area, bedrooms, bathrooms]], columns=["area", "bedrooms", "bathrooms"])
    prediction = model.predict(input_df)[0]
    return f"Predicted House Price: ₹{prediction:,.2f}"

# Gradio interface
iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Area (sq ft)"),
        gr.Number(label="Bedrooms"),
        gr.Number(label="Bathrooms")
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="🏡 House Price Predictor",
    description="Enter area, bedrooms, and bathrooms to predict house price."
)

if __name__ == "__main__":
    iface.launch()
