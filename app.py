import streamlit as st
import joblib
import pickle
import numpy as np

# Function to load the pre-trained model
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

# Load your model
model = load_model('rf_classifier.pkl')

# Function to display results including images
def display_results():
    st.title("Application Results")
    st.write("Step 1: Hardware Connections")
    
    # Image for hardware connections
    hardware_image_url = "https://res.cloudinary.com/dutz2aydx/image/upload/v1720634630/ds8sgwb7ngwh39ipmrxj.jpg"
    
    # Display hardware connections image
    st.image(hardware_image_url, use_column_width=True)
    
    st.write("Step 2: Application Results")

    # Existing images to display
    image_urls = [
        "https://res.cloudinary.com/dutz2aydx/image/upload/v1720465729/iotjwo8hg3mbpgl1v4we.png",
        "https://res.cloudinary.com/dutz2aydx/image/upload/v1720465808/bgl71lq0vmdbpnn3aeem.png",
        "https://res.cloudinary.com/dutz2aydx/image/upload/v1720465842/k0mxtqt9ldcapovhinui.png",
        "https://res.cloudinary.com/dutz2aydx/image/upload/v1720465875/rzeuysjhufzqds6ivuef.png"
    ]

    # Display existing images in two rows
    col1, col2 = st.columns(2)

    with col1:
        st.image(image_urls[0], use_column_width=True)
        st.image(image_urls[1], use_column_width=True)

    with col2:
        st.image(image_urls[2], use_column_width=True)
        st.image(image_urls[3], use_column_width=True)

# Main function to display the app
def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("", ["Home", "About", "Prototype", "Result", "Educational Resources", "Government Schemes", "Crop Loans", "Contact Us"])

    if menu_selection == "Home":
        st.title("Crop Prediction App")
        st.write("Enter environmental factors to predict suitable crop")

        # Input fields with default values set to 0
        humidity = st.number_input("Enter Humidity (%)", min_value=0, max_value=100, value=0, step=1, format="%d")
        moisture = st.number_input("Enter Moisture (%)", min_value=0, max_value=100, value=0, step=1, format="%d")
        light_intensity = st.number_input("Enter Light Intensity", min_value=0, max_value=5000, value=0, step=1, format="%d")

        # Language selection (for demonstration purposes), moved above the predict button
        language = st.selectbox("Select Language", ["English", "Hindi", "Tamil", "Telugu"])

        if st.button("Predict"):
            # Actual prediction logic
            input_features = np.array([[humidity, moisture, light_intensity]])
            predicted_crop = model.predict(input_features)  # Make prediction using the model

            # Display predicted crop in selected language
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

    elif menu_selection == "Educational Resources":
        st.title("Educational Resources")
        st.write("Explore learning resources related to the future of farming.")
        st.write("This website provides various educational resources for farming and agriculture.")
        
        # Link to external educational resources
        st.markdown("[Click here](https://future-of-farming.colab.newscientist.com/resources) to access the learning resources.")

    elif menu_selection == "Government Schemes":
        st.title("Government Schemes")
        st.write("Discover government schemes related to agriculture and farming.")
        st.write("These schemes aim to support farmers and promote agricultural development.")
        
        # Button linking to government schemes URL
        st.markdown("[Click here](https://pib.gov.in/PressReleaseIframePage.aspx?PRID=2002012) to view government schemes.")

    elif menu_selection == "Crop Loans":
        st.title("Crop Loans")
        st.write("Learn more about choosing the right type of agricultural loans for your farming needs.")
        st.write("This section provides insights into different types of crop loans and their benefits.")
        
        # Button linking to crop loans URL
        st.markdown("[Click here to learn more about Crop Loans](https://bankofmaharashtra.in/blogs/agriculture-loans-choosing-right-type)")
        
        # Link to apply for a loan
        st.markdown("[Click here to apply for a loan](https://www.bankofbaroda.in/banking-mantra/loans-borrowings/articles/how-to-get-an-agriculture-loan)")
        
        # Link to see how many banks provide crop loans
        st.markdown("[Click here to see how many banks provide crop loans](https://www.bankbazaar.com/personal-loan/crop-loan.html)")

    elif menu_selection == "Result":
        display_results()

    elif menu_selection == "About":
        st.title("About")
        st.write("In agriculture planning and decision making, predicting crop outcomes is vital. Using machine learning tools, like the Random Forest classifier has proven effective in forecasting crop yields based on data and relevant environmental factors. This study delves into how Random Forest can be used in crop prediction by analyzing datasets that encompass weather patterns, soil quality and past crop yields. The model's capability to handle relationships between variables makes it well suited for capturing the influences on crop growth. Moreover, a user-friendly website has been created specifically for farmers, incorporating the model to offer time and localized forecasts of crop yields. This platform aims to equip farmers with insights for making informed decisions to enhance productivity and sustainability.")

    elif menu_selection == "Prototype":
        st.title("Prototype")
        st.write("Our prototype for this project has been developed using Tinkercad, an online platform for 3D modeling and simulation. Tinkercad allows us to simulate different environmental conditions and analyze their impact on crop growth and yield predictions. The prototype includes virtual sensors and actuators to replicate real-world scenarios, providing a realistic testing environment for our predictive models.")

    elif menu_selection == "Contact Us":
        st.title("Contact Us")
        st.write("For any inquiries or support, please feel free to reach out to us:")

        st.markdown("- **Email:** [support@croppredictionapp.com](mailto:support@croppredictionapp.com)")
        st.markdown("- **Phone:** +91 86391-50020")

def load_crop_instructions():
    crop_instructions = {
        'Wheat': 'Harvesting season: March to June. Fertilizers: Nitrogen-based fertilizers.',
        'Rice': 'Harvesting season: July to October. Fertilizers: Potassium-rich fertilizers.',
        'Maize': 'Harvesting season: August to October. Fertilizers: Balanced NPK fertilizers.',
        'Barley': 'Harvesting season: April to July. Fertilizers: Phosphorus-based fertilizers.',
        'Oats': 'Harvesting season: June to August. Fertilizers: Organic compost and nitrogen fertilizers.',
        'Sorghum': 'Harvesting season: October to December. Fertilizers: Balanced NPK fertilizers.',
        'Millet': 'Harvesting season: August to October. Fertilizers: Nitrogen and phosphorus fertilizers.',
        'Rye': 'Harvesting season: June to August. Fertilizers: Organic compost and potassium fertilizers.',
        'Quinoa': 'Harvesting season: September to November. Fertilizers: Organic compost and potassium fertilizers.',
        'Soybeans': 'Harvesting season: September to October. Fertilizers: Balanced NPK fertilizers.',
        'Peanuts': 'Harvesting season: October to November. Fertilizers: Potassium-rich fertilizers.',
        'Lentils': 'Harvesting season: April to July. Fertilizers: Phosphorus-based fertilizers.',
        'Chickpeas': 'Harvesting season: April to July. Fertilizers: Nitrogen-based fertilizers.',
        'Kidney beans': 'Harvesting season: July to September. Fertilizers: Balanced NPK fertilizers.',
        'Sunflower': 'Harvesting season: July to October. Fertilizers: Potassium-rich fertilizers.',
        'Canola': 'Harvesting season: June to August. Fertilizers: Nitrogen and phosphorus fertilizers.',
        'Cotton': 'Harvesting season: October to December. Fertilizers: Balanced NPK fertilizers.',
        'Sugarcane': 'Harvesting season: December to March. Fertilizers: Potassium-rich fertilizers.',
        'Potatoes': 'Harvesting season: April to July. Fertilizers: Phosphorus-based fertilizers.',
        'Tomatoes': 'Harvesting season: February to May. Fertilizers: Balanced NPK fertilizers.'
    }
    return crop_instructions

# Run the main function
if __name__ == "__main__":
    main()
