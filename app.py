import streamlit as st
import pandas as pd
import requests
import os
import pickle
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to load the model (stub implementation for example)
def load_model(model_file):
    return None  # Replace with your actual model loading logic

# Function to load crop instructions (stub implementation for example)
def load_crop_instructions():
    crop_instructions = {
        'Wheat': 'Harvesting season: March to June. Fertilizers: Nitrogen-based fertilizers.',
        'Rice': 'Harvesting season: July to October. Fertilizers: Potassium-rich fertilizers.',
        # Add other crops here...
    }
    return crop_instructions

# Function to get market prices from USDA ERS API
def get_market_prices(api_key):
    url = "https://api.ers.usda.gov/data/fruit-vegetable-prices"
    params = {
        "api_key": api_key,
        "q": "apple",  # Example query for apple, adjust as needed
        "format": "json"
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch market prices. Status code: {response.status_code}")
            st.error(f"Error message: {response.text}")  # Log the full response content
            return None

    except Exception as e:
        st.error(f"Error fetching market prices: {e}")
        return None

# Main function to display the app
def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("", ["Home", "About", "Prototype", "Result", "Contact Us", "Market Prices"])

    if menu_selection == "Home":
        st.title("Crop Prediction App")
        st.write("Enter environmental factors to predict suitable crop")

        # Load the model (replace with your actual model loading logic)
        rf_classifier = load_model('rf_classifier.pkl')

        # Input fields for user to enter values
        humidity = st.number_input("Enter Humidity (%)", min_value=0, max_value=100, value=50, step=1, format="%d")
        moisture = st.number_input("Enter Moisture (%)", min_value=0, max_value=100, value=50, step=1, format="%d")
        light_intensity = st.number_input("Enter Light Intensity", min_value=0, max_value=5000, value=2500, step=1, format="%d")

        # Language selection for Indian languages
        language = st.selectbox("Select Language", ["English", "Hindi", "Tamil", "Telugu"])

        if st.button("Predict"):
            input_data = {
                'Humidity': [humidity],
                'Moisture': [moisture],
                'LightIntensity': [light_intensity]
            }
            input_df = pd.DataFrame(input_data)

            predicted_crop = rf_classifier.predict(input_df)

            # Display predicted outcome in selected language
            if language == "Hindi":
                st.write("पूर्वानुमानित फसल:", predicted_crop[0])
            elif language == "Tamil":
                st.write("கட்டுரையில் விரும்பப்படுகிறது:", predicted_crop[0])
            elif language == "Telugu":
                st.write("అంగారం బాహ్యం:", predicted_crop[0])
            else:
                st.write("Predicted Crop:", predicted_crop[0])

            # Display instructions based on predicted crop
            crop_instructions = load_crop_instructions()
            if predicted_crop[0] in crop_instructions:
                st.subheader("Instructions for Farmers:")
                st.write(crop_instructions[predicted_crop[0]])
            else:
                st.warning("Instructions not available for this crop.")

    elif menu_selection == "Market Prices":
        st.title("Market Prices and Trends")
        st.write("Integrate market prices and trends for various crops to help farmers decide on the most profitable crops to grow.")
        st.write("Provide farmers with current market prices and trends for different crops. This information helps them make informed decisions about which crops to grow for maximum profitability.")

        # Get API key from environment variables
        api_key = os.getenv('USDA_ERS_API_KEY')

        if api_key:
            market_data = get_market_prices(api_key)
            if market_data:
                st.write(market_data)
        else:
            st.error("USDA ERS API key not found. Please check your .env file.")

if __name__ == "__main__":
    main()
