const video = document.getElementById("webcam");
const canvas = document.getElementById("canvas");
const fileInput = document.getElementById("file-input");
const resultsDiv = document.getElementById("results");

// Start webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
        video.srcObject = stream;
    })
    .catch((err) => {
        console.error("Error accessing webcam:", err);
    });

function captureWebcam() {
    const context = canvas.getContext("2d");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
}

function uploadImage() {
    let imageData;

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const reader = new FileReader();
        reader.onload = () => {
            imageData = reader.result;
            sendToBackend(imageData);
        };
        reader.readAsDataURL(file);
    } else {
        imageData = canvas.toDataURL("image/png");
        sendToBackend(imageData);
    }
}

function sendToBackend(imageData) {
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ image: imageData }),
    })
    .then((response) => response.json())
    .then((data) => {
        resultsDiv.innerHTML = `<p>Total Value: ₹${data.total_value}</p>`;
        for (const [coin, count] of Object.entries(data.coin_counts)) {
            resultsDiv.innerHTML += `<p>${coin}: ${count}</p>`;
        }
    })
    .catch((err) => {
        console.error("Error:", err);
    });
}
