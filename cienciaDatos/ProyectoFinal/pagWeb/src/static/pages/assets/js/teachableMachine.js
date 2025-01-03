// Teachable Machine Code
const URL = "https://teachablemachine.withgoogle.com/models/mAdhhX2wVq/";

let model, webcam, labelContainer, maxPredictions;

async function init() {
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";

    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

    const flip = true; 
    webcam = new tmImage.Webcam(200, 200, flip);
    await webcam.setup(); 
    await webcam.play();
    window.requestAnimationFrame(loop);

    document.getElementById("webcam-container").appendChild(webcam.canvas);
    labelContainer = document.getElementById("label-container");
    for (let i = 0; i < maxPredictions; i++) { 
        labelContainer.appendChild(document.createElement("div"));
    }
}

function stop() {
    console.log('Attempting to stop the camera'); // Mensaje de depuración
    if (webcam && webcam.stream) {
        webcam.stream.getTracks().forEach(track => track.stop());
        webcam.stop(); // Detener la cámara
        webcam = null; // Opcional, limpiar la referencia a webcam
        console.log('Camera stopped'); // Mensaje de confirmación en consola
    } else {
        console.log('No webcam stream found'); // Mensaje de depuración
    }
}



async function loop() {
    webcam.update();
    await predict();
    window.requestAnimationFrame(loop);
}

async function predict() {
    const prediction = await model.predict(webcam.canvas);
    for (let i = 0; i < maxPredictions; i++) {
        const classPrediction =
            prediction[i].className + ": " + prediction[i].probability.toFixed(2);
        labelContainer.childNodes[i].innerHTML = classPrediction;
    }
}
