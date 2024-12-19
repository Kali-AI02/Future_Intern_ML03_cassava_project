import streamlit as st
import cv2
import numpy as np
from helpers import preprocess_image, predict

def display_prediction():
    st.title("Prediction")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read and display the uploaded image
        image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Call prediction function
        prediction = predict(image)
        st.write(f"Prediction: {prediction}")

