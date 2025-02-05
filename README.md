# Indian Coin Counter with Flask

This project is a Flask-based application for detecting and counting Indian coins. It uses a camera to capture images or allows users to upload images for processing. The application integrates with Roboflow's Object Detection API to identify coins and calculate their total value.

---

## Features
- **Camera Integration**: Capture images directly using your device's camera.
- **Image Upload**: Upload images for processing.
- **Real-Time Detection**: Detect coins in images and calculate their total value.
- **Roboflow API Integration**: Utilizes Roboflow's trained model for coin detection.

---

## Screenshots
### 1. **Camera Interface**

### 2. **Detection Results**
https://coin-detection-u4as.onrender.com/


---

## How It Works
1. **Image Capture**: Users can either capture an image using their device's camera or upload an existing image.
2. **Roboflow API**: The captured/uploaded image is sent to the Roboflow API, which identifies coins and provides their classes and bounding boxes.
3. **Coin Mapping**: Each class corresponds to a coin denomination (e.g., 1 INR, 2 INR, etc.).
4. **Output**: The application calculates and displays the total value and the count of each coin.

---



1. **Frontend**: HTML, CSS, and JavaScript to provide a user interface for camera capture and image upload.
2. **Backend**: Flask handles image processing, integrates with Roboflow API, and serves results to the frontend.
3. **Roboflow**: Processes images and returns detection data.

---

## Installation and Setup

### Prerequisites
- Python 3.x installed on your machine
- Flask library
- OpenCV library
- Roboflow account and API key

### Steps to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/prafulla2121/indian-coin-detection.git
