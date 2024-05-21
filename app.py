import streamlit as st
import joblib
import os

# Load the pipelines
model_path = os.path.dirname(os.path.abspath(__file__))

try:
    sentiment_pipeline = joblib.load(os.path.join(model_path, 'sentiment_pipeline.pkl'))
    categorization_pipeline = joblib.load(os.path.join(model_path, 'categorization_pipeline.pkl'))
    st.write("")
except Exception as e:
    st.write(f"Error loading models: {e}")

# Function to classify feedback
def classify_feedback(feedback_text):
    # Predict sentiment
    prediction = sentiment_pipeline.predict([feedback_text])
    return prediction[0]

# Function to categorize products
def categorize_product(product_description):
    # Predict category
    prediction = categorization_pipeline.predict([product_description])
    return prediction[0]

# Streamlit App
st.title("Product Feedback and Categorization")

st.header("Sentiment Analysis")
feedback_text = st.text_area("Enter feedback text:")
if st.button("Classify Sentiment"):
    if feedback_text:
        sentiment = classify_feedback(feedback_text)
        st.write(f"The predicted sentiment is: {sentiment}")
    else:
        st.write("Please enter feedback text.")

st.header("Product Categorization")
product_description = st.text_area("Enter product description:")
if st.button("Categorize Product"):
    if product_description:
        category = categorize_product(product_description)
        st.write(f"The predicted category is: {category}")
    else:
        st.write("Please enter product description.")
