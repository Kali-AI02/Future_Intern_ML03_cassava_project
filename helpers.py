import cv2
import os
import tensorflow as tf
import numpy as np

# Disable oneDNN optimizations for consistent numerical results
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Preprocessing function
def preprocess_image(image):
    image = cv2.resize(image, (128, 128))
    image = image / 255.0
    return image

# Prediction function
def predict(image):
    try:
        # Load the trained model (ensure the path is correct)
        model = tf.keras.models.load_model('models/temp_model.h5')
        preprocessed_image = preprocess_image(image)
        input_image_reshaped = np.reshape(preprocessed_image, [1, 128, 128, 3])
        prediction = model.predict(input_image_reshaped)
        result = np.argmax(prediction)
        return "Affected" if result == 1 else "Not Affected"
    except Exception as e:
        return f"Error: {str(e)}"

