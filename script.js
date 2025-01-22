document.addEventListener('DOMContentLoaded', () => {
    const uploadBtn = document.getElementById('upload-btn');
    const predictBtn = document.getElementById('predict-btn');
    const uploadStatus = document.getElementById('upload-status');
    const predictionResult = document.getElementById('prediction-result');

    // Handle CSV Upload
    uploadBtn.addEventListener('click', () => {
        const fileInput = document.getElementById('csv-file');
        const file = fileInput.files[0];

        if (!file) {
            uploadStatus.textContent = 'Please select a CSV file.';
            uploadStatus.style.color = 'red';
            return;
        }

        const reader = new FileReader();
        reader.onload = () => {
            uploadStatus.textContent = 'CSV file uploaded successfully!';
            uploadStatus.style.color = 'green';
            console.log('Uploaded CSV data:', reader.result); // Placeholder for backend integration
        };
        reader.readAsText(file);
    });

    // Handle Prediction
    predictBtn.addEventListener('click', () => {
        const inputData = document.getElementById('input-data').value.trim();

        if (!inputData) {
            predictionResult.textContent = 'Please enter valid input data.';
            predictionResult.style.color = 'red';
            return;
        }

        // Convert input to array and validate
        const inputArray = inputData.split(',').map(Number);
        if (inputArray.length !== 22 || inputArray.some(isNaN)) {
            predictionResult.textContent = 'Input must contain exactly 22 numeric values.';
            predictionResult.style.color = 'red';
            return;
        }

        // Send data to backend for prediction (placeholder)
        console.log('Input Data for Prediction:', inputArray);

        // Simulate Prediction Result
        setTimeout(() => {
            const isParkinsons = Math.random() > 0.5; // Mock prediction result
            predictionResult.textContent = isParkinsons
                ? 'Positive: Parkinson\'s Detected'
                : 'Negative: No Parkinson\'s Detected';
            predictionResult.style.color = isParkinsons ? 'red' : 'green';
        }, 1000);
    });
});
