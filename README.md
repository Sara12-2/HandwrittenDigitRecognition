## 🔢 Project : Handwritten Digit Classifier (CNN-based)

> A real-time digit recognition system using *Convolutional Neural Networks* trained on the MNIST dataset.

### 🚀 Overview

This project uses deep learning to classify handwritten digits (0–9) from images. It is trained on the *MNIST* dataset and deployed via *Streamlit* with an interactive UI that lets users draw a digit or upload an image for prediction.

### 🧠 How It Works

1. 🖼 *Image Input*  
   Users can draw a digit on the canvas or upload a 28x28 pixel grayscale image.

2. 🔄 *Preprocessing*  
   The image is reshaped and normalized before being fed to the model.

3. 🧠 *Model Architecture*  
   A CNN with multiple layers:
   - Conv2D + ReLU + MaxPooling
   - Dense (Fully Connected)
   - Softmax output layer for 10-class classification

4. ⚡ *Prediction*  
   The model predicts the digit with high accuracy, and displays the result instantly.

### 💻 Tech Stack
```bash

| Tool            | Description                              |
|-----------------|------------------------------------------|
| Python        | Core programming language                |
| TensorFlow/Keras | For building and training the CNN    |
| Streamlit     | User-friendly web app interface          |
| NumPy | For image handling and preprocessing     |
| MNIST         | Benchmark dataset for handwritten digits |
```

### 🔍 Example Predictions
```bash
| Input Image        | Predicted Digit |
|--------------------|-----------------|
| (Drawn "5")        | 5 ✅             |
| (Uploaded "3.png") | 3 ✅             |

```

