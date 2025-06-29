from flask import Flask, render_template, request
import numpy as np
import onnxruntime as rt
import json

app = Flask(__name__)

# Load ONNX model and class labels
session = rt.InferenceSession("iris_model.onnx")
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

with open("class_labels.json", "r") as f:
    class_labels = json.load(f)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sl = float(request.form['swidth'])
        sw = float(request.form['sheight'])
        pl = float(request.form['pwidth'])
        pw = float(request.form['pheight'])

        input_data = np.array([[sl, sw, pl, pw]], dtype=np.float32)
        prediction = session.run([output_name], {input_name: input_data})
        class_index = int(prediction[0][0])
        predicted_class = class_labels[class_index]

        return render_template("index.html", data=predicted_class)

    except Exception as e:
        return render_template("index.html", data=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
