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
        
        # List of YouTube video links
        youtube_videos = [
            "https://www.youtube.com/watch?v=2tgitJwyRXE",
            "https://www.youtube.com/watch?v=u97eldevr2g&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG",
            "https://www.youtube.com/watch?v=4dDOzYd01Oc&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=2",
            "https://www.youtube.com/watch?v=Lj5jtYO4twQ&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=3",
            "https://www.youtube.com/watch?v=Udv1We1LE7k&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=4",
            "https://www.youtube.com/watch?v=PjJIvYc7vHo&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=5",
            "https://www.youtube.com/watch?v=92Ey4MbjXO4&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=6",
            "https://www.youtube.com/watch?v=HO7r663ECkA&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=7",
            "https://www.youtube.com/watch?v=MYpUX8qffH4&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=8",
            "https://www.youtube.com/watch?v=cpGpUy6iw30&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=9",
            "https://www.youtube.com/watch?v=srxHs-8Nv3o&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=10",
            "https://www.youtube.com/watch?v=QxK4YbPrWXk&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=11",
            "https://www.youtube.com/watch?v=65Djs709ZwU&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=12",
            "https://www.youtube.com/watch?v=mya51C2cGwI&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=13",
            "https://www.youtube.com/watch?v=opCjbRYe6aw&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=14",
            "https://www.youtube.com/watch?v=-c6OuXMSWeE&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=15",
            "https://www.youtube.com/watch?v=DiNQW6Q35Kg&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=16",
            "https://www.youtube.com/watch?v=vUSuyDY0NUA&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=17",
            "https://www.youtube.com/watch?v=_ZhtIqeRmuw&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=18",
            "https://www.youtube.com/watch?v=7vbGoceUUgs&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=19",
            "https://www.youtube.com/watch?v=Kytp4Uyaj6E&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=20",
            "https://www.youtube.com/watch?v=R8z4T8EhFU0&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=21",
            "https://www.youtube.com/watch?v=XTfnWvfIP8o&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=22",
            "https://www.youtube.com/watch?v=leA9WWUXwdg&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=23",
            "https://www.youtube.com/watch?v=8NLEdLrZDoI&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=24",
            "https://www.youtube.com/watch?v=RCqf4NzdbFI&list=PL3PuCslSVB8tgJNr0kVAODvFN0ncbQVNG&index=25"
        ]

        # Display YouTube videos in rows of three
        for i in range(0, len(youtube_videos), 3):
            col1, col2, col3 = st.columns(3)
            with col1:
                if i < len(youtube_videos):
                    st.video(youtube_videos[i])
            with col2:
                if i + 1 < len(youtube_videos):
                    st.video(youtube_videos[i + 1])
            with col3:
                if i + 2 < len(youtube_videos):
                    st.video(youtube_videos[i + 2])

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
