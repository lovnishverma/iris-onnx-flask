---
title: ONNX
emoji: 📉
colorFrom: blue
colorTo: pink
sdk: docker
pinned: false
license: mit
short_description: deploying ML model in flask
---


## 🌸 Iris Flower Classifier (Flask + ONNX)

This project is a simple Flask web application that predicts the species of an Iris flower based on its measurements using a pre-trained **Logistic Regression model**. The model is exported in **ONNX (Open Neural Network Exchange)** format, allowing for efficient, framework-independent inference.

---

### 🚀 Live Demo

> 📌 Enter sepal length, sepal width, petal length, and petal width
> 📌 Get predicted Iris species: *Setosa*, *Versicolor*, or *Virginica*

---

### 📁 Project Structure

```
.
├── app.py                  # Flask web app
├── iris_model.onnx         # ONNX-trained model
├── Dockerfile              # Dockerfile For HuggingFace   
├── class_labels.json       # Class label mapping
├── requirements.txt        # Required Python packages
└── templates/
    └── index.html          # HTML form for input
```

---

### 💡 Features

* 🧠 Trained with `scikit-learn` Logistic Regression
* 🔄 Converted to ONNX for optimized runtime inference
* 🌐 Deployed with Flask and HTML frontend
* 🪄 Clean input form with real-time result display

---

### 📦 Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/lovnishverma/iris-onnx-flask.git
   cd iris-onnx-flask
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App**

   ```bash
   python app.py
   ```

4. **Open in Browser**

   ```
   http://127.0.0.1:5000
   ```

---

### 🧪 Test Example

Try the following values:

```text
Sepal Length: 5.7
Sepal Width: 3.2
Petal Length: 5.2
Petal Width: 1.9
```

Output:

```
Predicted Flower Type: virginica
```

---

### 🤖 Why ONNX instead of Pickle or Joblib?

| Feature             | Pickle/Joblib                          | ONNX                                            |
| ------------------- | -------------------------------------- | ----------------------------------------------- |
| 🔒 Security         | Unsafe for web apps (can execute code) | Safer (no code execution risk)                  |
| 🔄 Interoperability | Python only                            | Works across platforms/languages                |
| ⚡ Speed             | OK in Python                           | Faster inference (especially with ONNX Runtime) |
| ☁️ Deployment       | Limited                                | Ideal for production, Docker, or cloud          |
| 📦 Size & Format    | Python-specific                        | Efficient binary format, language-independent   |

> ✅ **ONNX** is preferred when deploying machine learning models in production or cross-platform environments.

---

### 📚 Requirements

```txt
flask
onnxruntime
numpy
gunicorn
```

---

### 📜 License

This project is licensed under the [MIT License](LICENSE).

---

### 🙋‍♂️ Author

Made with ❤️ by [Lovnish Verma](https://lovnishverma.github.io)

---
