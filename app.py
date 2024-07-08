import streamlit as st

# Function to get market prices from USDA ERS API
# Main function to display the app
def main():
    # Define the CSS styles
    page_bg_img = '''
        <style>
            body {
                background-color: #A3F7F0; /* Light grey background */
            }
            .stApp {
                background: #A3F7F0;
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

    # Inject the CSS into the Streamlit app
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Sidebar navigation
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.radio("", ["Home", "About", "Prototype", "Result", "Contact Us", "Educational Resources", "Government Schemes", "Market Prices"])

    # Main content based on menu selection
    if menu_selection == "Home":
        st.title("Crop Prediction App")
        st.write("Enter environmental factors to predict suitable crop")
        humidity = st.number_input("Enter Humidity (%)", min_value=0, max_value=100, value=50, step=1, format="%d")
        moisture = st.number_input("Enter Moisture (%)", min_value=0, max_value=100, value=50, step=1, format="%d")
        light_intensity = st.number_input("Enter Light Intensity", min_value=0, max_value=5000, value=2500, step=1, format="%d")
        if st.button("Predict"):
            predicted_crop = "Wheat"
            st.write(f"Predicted Crop: {predicted_crop}")

    elif menu_selection == "Educational Resources":
        st.title("Educational Resources")
        st.write("Explore learning resources related to the future of farming.")
        st.write("This website provides various educational resources for farming and agriculture.")
        st.markdown("[Click here](https://future-of-farming.colab.newscientist.com/resources) to access the learning resources.")

    elif menu_selection == "Government Schemes":
        st.title("Government Schemes")
        st.write("Discover government schemes related to agriculture and farming.")
        st.write("These schemes aim to support farmers and promote agricultural development.")
        st.markdown("[Click here](https://pib.gov.in/PressReleaseIframePage.aspx?PRID=2002012) to view government schemes.")

    elif menu_selection == "Market Prices":
        st.title("Market Prices and Trends")
        st.write("Integrate market prices and trends for various crops to help farmers decide on the most profitable crops to grow.")
        st.write("Provide farmers with current market prices and trends for different crops. This information helps them make informed decisions about which crops to grow for maximum profitability.")

if __name__ == "__main__":
    main()
