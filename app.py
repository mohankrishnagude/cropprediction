import streamlit as st

# Main function to display the app
def main():
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("", ["Home", "About", "Prototype", "Result", "Contact Us", "Educational Resources", "Government Schemes"])

    if menu_selection == "Home":
        st.title("Crop Prediction App")
        st.write("Enter environmental factors to predict suitable crop")

        # Input fields for user to enter values (example placeholders)
        humidity = st.number_input("Enter Humidity (%)", min_value=0, max_value=100, value=50, step=1, format="%d")
        moisture = st.number_input("Enter Moisture (%)", min_value=0, max_value=100, value=50, step=1, format="%d")
        light_intensity = st.number_input("Enter Light Intensity", min_value=0, max_value=5000, value=2500, step=1, format="%d")

        if st.button("Predict"):
            # Replace with actual prediction logic
            predicted_crop = ["Wheat"]  # Example prediction list

            # Language selection (for demonstration purposes)
            language = st.selectbox("Select Language", ["English", "Hindi", "Tamil", "Telugu"])

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

if __name__ == "__main__":
    main()
