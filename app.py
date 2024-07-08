import streamlit as st
from streamlit_carousel import st_carousel

# Function to display results
def display_results():
    st.title("Application Results")
    st.write("Step 2: Application Results")

    # Images to display in the carousel
    image_urls = [
        "https://res.cloudinary.com/dutz2aydx/image/upload/v1720465729/iotjwo8hg3mbpgl1v4we.png",
        "https://res.cloudinary.com/dutz2aydx/image/upload/v1720465808/bgl71lq0vmdbpnn3aeem.png",
        "https://res.cloudinary.com/dutz2aydx/image/upload/v1720465842/k0mxtqt9ldcapovhinui.png",
        "https://res.cloudinary.com/dutz2aydx/image/upload/v1720465875/rzeuysjhufzqds6ivuef.png"
    ]

    # Display carousel with images
    st_carousel(images=image_urls)

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
            predicted_crop = "Wheat"  # Example prediction

            st.write(f"Predicted Crop: {predicted_crop}")

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

    elif menu_selection == "Result":
        display_results()

    elif menu_selection == "Contact Us":
        st.title("Contact Us")
        st.write("For any inquiries or support, please reach out to us:")
        st.write("- Email: contact@example.com")
        st.write("- Phone: +1234567890")

if __name__ == "__main__":
    main()
