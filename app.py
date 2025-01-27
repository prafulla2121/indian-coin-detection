from flask import Flask, request, render_template, jsonify
import requests
import cv2
import numpy as np

app = Flask(__name__)

# Roboflow API endpoint and key
API_URL = "https://detect.roboflow.com/coin-detection-948ts/1"
API_KEY = "8zyjP9CboCunG1Rf0seX"

# Coin values based on class names
COIN_VALUES = {
    "0": 1,  # Example: Class 0 corresponds to 1 INR
    "1": 1,  # Update these mappings based on your model
    "2": 2,
    "3": 5,
    "4": 10,
    "5": 20
}

# Route for the web interface
@app.route("/")
def index():
    return render_template("index.html")

# Route to process uploaded or captured images
@app.route("/detect_coins", methods=["POST"])
def detect_coins():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Read the image
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert the image to bytes for the API
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = img_encoded.tobytes()

    # Send the image to Roboflow
    response = requests.post(
        f"{API_URL}?api_key={API_KEY}",
        files={"file": img_bytes}
    )
    predictions = response.json().get("predictions", [])

    # Initialize coin count and total value
    coin_count = {value: 0 for value in COIN_VALUES.values()}
    total_value = 0

    # Process predictions
    for prediction in predictions:
        class_name = prediction["class"]
        value = COIN_VALUES.get(class_name, 0)
        total_value += value
        if value in coin_count:
            coin_count[value] += 1

    # Format the outputs
    coin_count_str = ", ".join([f"{value}:{count}" for value, count in coin_count.items() if count > 0])
    return jsonify({"coin_count": coin_count_str, "total_value": total_value})

if __name__ == "__main__":
    app.run()
