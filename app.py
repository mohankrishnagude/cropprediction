import streamlit as st
import requests

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

        # Input fields for user to enter values (example placeholders)
        humidity = st.number_input("Enter Humidity (%)", min_value=0, max_value=100, value=50, step=1, format="%d")
        moisture = st.number_input("Enter Moisture (%)", min_value=0, max_value=100, value=50, step=1, format="%d")
        light_intensity = st.number_input("Enter Light Intensity", min_value=0, max_value=5000, value=2500, step=1, format="%d")

        if st.button("Predict"):
            # Replace with actual prediction logic
            predicted_crop = "Wheat"  # Example prediction

            st.write(f"Predicted Crop: {predicted_crop}")

    elif menu_selection == "Market Prices":
        st.title("Market Prices and Trends")
        st.write("Integrate market prices and trends for various crops to help farmers decide on the most profitable crops to grow.")
        st.write("Provide farmers with current market prices and trends for different crops. This information helps them make informed decisions about which crops to grow for maximum profitability.")

        api_key = "5vhsIkPyW7gKaQoCbC81U3xF94rDowFK18BHZirS"  # Replace with your actual USDA ERS API key
        market_data = get_market_prices(api_key)
        
        if market_data and "error" not in market_data:
            st.write(market_data)
        elif market_data and "error" in market_data:
            st.error(f"Failed to fetch market prices. Error message: {market_data['error']['message']}")
        else:
            st.error("Failed to fetch market prices. No data returned.")

if __name__ == "__main__":
    main()
