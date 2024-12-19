import streamlit as st

def display_about_us():
    st.title("About Us")
    st.write("We are dedicated to providing innovative solutions to help farmers detect crop diseases.")
    st.write("**Location:** Kigali, Rwanda")
    st.write("**Contact:** +250 788 123 456")
    st.write("**Email:** info@cropdetect.com")

    # Add map for location
    st.map(data={"lat": [-1.94995], "lon": [30.05885]}, zoom=12)

    # Add social media links
    st.write("Follow us on:")
    st.write("[Facebook](https://facebook.com) | [Twitter](https://twitter.com) | [LinkedIn](https://linkedin.com)")

