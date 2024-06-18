from flask import Flask, jsonify, request
from flask_cors import CORS
from utils.classify import classify_image
from utils.episodes import get_episodes, get_episode, get_recommendations

app = Flask(__name__)
CORS(app)

# Endpoint for classifying the character and getting a random quote
@app.route('/classify', methods=['POST'])
def classify_image_route():
    # Receive Base64-encoded image data from the request
    data_url = request.json.get('image_data')

    # Decode Base64 data to obtain the raw image data
    _, base64_data = data_url.split(',', 1)
    response = classify_image(base64_data)

    # Return the detected character and associated quote as JSON response
    return jsonify(response), 200

@app.route("/episodes", methods=["GET"])
def get_episodes_route():
    episodes = get_episodes()
    return jsonify(episodes), 200

@app.route("/episodes/<int:season>/<int:episode>", methods=["GET"])
def get_episode_route(season, episode):
    episodes = get_episode(season, episode)
    return jsonify(episodes), 200

@app.route("/recommendations/<int:season>/<int:episode>", methods=["GET"])
def get_recommendations_route(season, episode):
    top_n = request.args.get('top_n', default=10, type=int)  # Get top_n from query parameter, default to 10 if not provided
    recommendations = get_recommendations(season, episode, top_n)
    return jsonify(recommendations), 200

if __name__ == "__main__":
    app.run()