from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not all([name, email, message]):
        return jsonify({"msg": "Please fill all fields"}), 400

    # Read existing data safely
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        except json.JSONDecodeError:
            data = []
    else:
        data = []

    # Append new message
    data.append({
        "name": name,
        "email": email,
        "message": message
    })

    # Save back to file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return jsonify({"msg": "Message submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
