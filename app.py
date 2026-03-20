from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

model = None
model_path = os.path.join(os.getcwd(), "model_params.json")

try:
    with open(model_path, "r") as file:
        model = json.load(file)
except Exception as e:
    print("MODEL LOAD ERROR:", e)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/healthz")
def healthz():
    return "ok", 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            return render_template("index.html", prediction_text="Model not loaded")
        
        hours = float(request.form["hours"])
        prediction = model["slope"] * hours + model["intercept"]

        return render_template(
            "index.html",
            prediction_text=f"Predicted Marks: {round(prediction, 2)}"
        )
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")