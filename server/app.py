# Restart flask server on save: flask run --reload
import cv2
import base64
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, jsonify, request
from flask_cors import CORS
from neo4j import GraphDatabase, basic_auth
from dotenv import load_dotenv
import tensorflow as tf
import logging
from tensorflow.keras.models import load_model
import sys
# Allows us to access environmental variables
import os

friends_model = load_model('friends_100.keras')

# Loading environmental variables from the .env file
load_dotenv()
uri = os.getenv("URI")
username = os.getenv("USER")
password = os.getenv("PASSWORD")

# Logging for debugging connection with Neo4j Aura
# handler = logging.StreamHandler(sys.stdout)
# handler.setLevel(logging.DEBUG)
# logging.getLogger("neo4j").addHandler(handler)
# logging.getLogger("neo4j").setLevel(logging.DEBUG)

# Creating a neo4j driver with custom SSL context options
driver = GraphDatabase.driver(uri, auth=basic_auth(username, password), database="neo4j")

app = Flask(__name__)
CORS(app)

# Getting all employees
def get_quote(tx, name):
    query = """
            WITH timestamp() AS currentTimestamp
            MATCH (author:Author {name: $name})-[:HAS_QUOTE]->(quote:Quote)
            WITH quote, rand() * toFloat(currentTimestamp) AS randomOrder
            RETURN quote
            ORDER BY randomOrder
            LIMIT 1
            """
    return tx.run(query, name=name).data()[0]

@app.route("/quote", methods = ["GET"])
def get_quote_route():
    with driver.session() as session:
        quote = session.execute_read(get_quote, "Chandler")
    response = quote
    return jsonify(response), 200

@app.route('/classify', methods=['POST'])
def classify_image():
    # Receive Base64-encoded image data from the request
    data_url = request.json.get('image_data')
    
    # Decode Base64 data to obtain the raw image data
    _, base64_data = data_url.split(',', 1)
    image_data = base64.b64decode(base64_data)
    
    # Convert raw image data to a NumPy array
    nparr = np.frombuffer(image_data, np.uint8)
    
    # Decode the image array using OpenCV
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # # Display the image for debugging purposes
    # plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # plt.axis('off')
    # plt.show()

    resize = tf.image.resize(image, (256,256))
    # plt.imshow(resize.numpy().astype(int))
    # plt.show()

    prediction = friends_model.predict(np.expand_dims(resize/255, 0))[0]
    class_labels = ['Chandler', 'Joey', 'Monica', 'Phoebe', 'Rachel', 'Ross']

    for i, prob in enumerate(prediction):
        print(f'{class_labels[i]}: {prob:.4f}')
    
    # Get the index of the maximum value
    max_index = np.argmax(prediction)
    character = class_labels[max_index]

    # Get the maximum value
    max_value = prediction[max_index]

    # Print the index and value of the maximum value
    print("Character:", character)
    print("Confidence:", max_value)

    with driver.session() as session:
        quote = session.execute_read(get_quote, character)
    quote = quote["quote"]

    # Return the detected character and associated quote as JSON response
    return jsonify({
        "character": character,
        "confidence": float(max_value),
        "quote": quote
    })

# Running our app (provided its the main programme and isn't imported as a module)
if __name__ == "__main__":
    app.run()