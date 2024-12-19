import streamlit as st
from about_us import display_about_us
from prediction import display_prediction
import openai





st.set_page_config(
    page_title="Cassava Disease Detection",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom styles (for example, text color for markdown)
st.markdown(
    """
    <style>
    .stMarkdown {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Disease information and actions for affected diseases
disease_info = {
    "Cassava Mosaic Disease": {
        "description": "Caused by cassava mosaic virus (CMV), this disease leads to stunted growth and distorted leaves, reducing cassava yield.",
        "action": "To manage this disease, remove infected plants, use resistant cassava varieties, and apply appropriate pesticides if necessary."
    },
    "Cassava Brown Streak Disease": {
        "description": "Caused by cassava brown streak virus (CBSV), this disease primarily affects the roots, causing discoloration and making them inedible.",
        "action": "Remove affected plants immediately, practice crop rotation, and use virus-resistant varieties."
    },
    "Cassava Bacterial Blight": {
        "description": "Caused by the Xanthomonas axonopodis bacteria, this disease results in leaf wilting, defoliation, and stem dieback.",
        "action": "Prune affected branches, avoid over-watering, and apply copper-based bactericides."
    },
    "Healthy": {
        "description": "The cassava plant shows no signs of disease and is in optimal health.",
        "action": "Continue to care for the plant by maintaining proper watering, fertilization, and pest control."
    }
}

# Sidebar Disease Info Dropdown
st.sidebar.title("Learn About Diseases")
selected_disease = st.sidebar.selectbox("Select a Disease", list(disease_info.keys()))
st.sidebar.write(f"**Description:** {disease_info[selected_disease]['description']}")
st.sidebar.write(f"**What to Do:** {disease_info[selected_disease]['action']}")

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "Prediction", "About Us", "Help"])

# Home Page
if page == "Home":
    st.title('Cassava Disease Detection Demo 🌱')
    st.write("Welcome to the Cassava Disease Detection app!")
    st.write("Learn about common diseases affecting cassava crops:")
    
    for disease, details in disease_info.items():
        st.markdown(f"### {disease}")
        st.write(details["description"])
        st.write(f"**What to do:** {details['action']}")

# Prediction Page
elif page == "Prediction":
    display_prediction()

# About Us Page
elif page == "About Us":
    display_about_us()

# Help Section
elif page == "Help":
    st.title("Help Section")
    st.write("Upload an image to detect crop diseases. Contact us for more assistance.")


