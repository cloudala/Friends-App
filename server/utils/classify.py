import cv2
import base64
import numpy as np
from tensorflow.keras.models import load_model
from utils.quotes import get_quote

friends_model = load_model('./models/friends_100.keras')

def classify_image(base64_data):
    image_data = base64.b64decode(base64_data)
    
    # Convert raw image data to a NumPy array
    nparray = np.frombuffer(image_data, np.uint8)
    
    # Decode the image array using OpenCV
    image = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

    # Resize the image using OpenCV
    image_resized = cv2.resize(image, (256, 256))

    # Normalize the image and add an extra dimension
    image_normalized = image_resized / 255.0
    image_expanded = np.expand_dims(image_normalized, axis=0)

    # Make the prediction
    prediction = friends_model.predict(image_expanded)[0]
    class_labels = ['Chandler', 'Joey', 'Monica', 'Phoebe', 'Rachel', 'Ross']
    
    # Get the index of the maximum value
    max_index = np.argmax(prediction)
    character = class_labels[max_index]

    # Get the confidence value for our prediction
    confidence = float(prediction[max_index])

    # Get a random quote by character
    quote = get_quote(character)

    # Return the detected character and associated quote as JSON response
    return {
        "character": character,
        "confidence": confidence,
        "quote": quote
    }