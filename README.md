
## 📧 Project 1: Email/SMS Spam Classifier

> A real-time classifier that detects whether a message is **SPAM** or **NOT SPAM**, using traditional ML techniques.

### 🚀 Overview

This project demonstrates how to build and deploy a **spam detection system** using machine learning and natural language processing (NLP). The model is trained on the [UCI SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection), and the user interface is built using **Streamlit**.

### 🧠 How It Works

1. 🧹 **Preprocessing**  
   Text messages are cleaned and vectorized using **TF-IDF** to transform text into numerical features.

2. 🤖 **Model**  
   A **Multinomial Naive Bayes** classifier is trained on thousands of labeled SMS messages.

3. 🖥️ **Web App**  
   Users enter a message, click "Check Spam", and get instant feedback with visual labels.

### 💻 Tech Stack

| Tool           | Description                                 |
|----------------|---------------------------------------------|
| `Python`       | Core programming language                   |
| `scikit-learn` | For training the spam detection model       |
| `Streamlit`    | Interactive web interface                   |
| `Joblib`       | To save/load the ML model                   |
| `UCI Dataset`  | Public dataset with spam/ham labels         |

### ✉️ Example Predictions

| Message                                               | Prediction  |
|-------------------------------------------------------|-------------|
| "Congratulations! You’ve won a free cruise!"          | 🚨 SPAM     |
| "Hi, are you free this weekend to catch up?"          | ✅ NOT SPAM |
| "Urgent! Your account is at risk. Click the link now" | 🚨 SPAM     |
| "Reminder: Your appointment is at 4:30 PM tomorrow."  | ✅ NOT SPAM |

---
