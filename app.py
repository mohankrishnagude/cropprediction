import pickle
import streamlit as st
import pandas as pd

# Function to load the model
def load_model(model_file):
    try:
        with open(model_file, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error(f"Model file '{model_file}' not found.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        st.stop()

# Function to display prediction form and outcome
def main():
    # Set page background and title styling
    page_bg_img = '''
        <style>
            body {
                background-color: #f0f0f0; /* Light grey background */
            }
            .stApp {
                background: rgba(255, 255, 255, 0.8);
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            .stSidebar {
                position: fixed;
                left: 0;
                width: 15%;
                height: 100%;
                padding: 2rem;
                background-color: #ffffff; /* White background for sidebar */
                border-right: 1px solid #e0e0e0; /* Light grey border on the right */
            }
            .stSidebar a {
                display: block;
                margin-bottom: 1rem;
                text-decoration: none;
                color: #333333; /* Dark grey text */
                font-weight: bold;
            }
            .stSidebar a:hover {
                color: #007bff; /* Blue text on hover */
            }
        </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("", ["Home", "About", "Prototype", "Result", "Contact Us"])

    if menu_selection == "Home":
        st.title("Crop Prediction App")
        st.write("Enter environmental factors to predict suitable crop")

        # Load the model
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

    elif menu_selection == "About":
        st.title("About")
        st.write("This is the About page.")

    elif menu_selection == "Prototype":
        st.title("Prototype")
        st.write("This is the Prototype page.")

    elif menu_selection == "Result":
        st.title("Result")
        st.write("This is the Result page.")

    elif menu_selection == "Contact Us":
        st.title("Contact Us")
        st.write("This is the Contact Us page.")

if __name__ == "__main__":
    main()
