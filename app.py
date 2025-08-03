from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and label encoder
model, label_encoder = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = int(request.form["age"])
        gender = request.form["gender"]
        salary = float(request.form["salary"])
        interest = int(request.form["interest"])

        # Encode gender
        gender_encoded = label_encoder.transform([gender])[0]

        # Prepare features
        features = np.array([[age, gender_encoded, salary, interest]])

        prediction = model.predict(features)[0]

        result = "✅ Yes - User will likely click the ad" if prediction == 1 else "❌ No - User will not click the ad"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
