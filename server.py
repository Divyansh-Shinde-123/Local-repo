from flask import Flask, request, jsonify
import urllib.parse

app = Flask(__name__)

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdqbnBMkPS-zAaLcsI3RqYf56oSK2CXYProWJToR9IjBPawow/formResponse"

ENTRIES = {
    "name": "entry.1047757487",
    "email": "entry.91624104",
    "message": "entry.1585277958"
}

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not name or not email or not message:
        return jsonify({"msg": "All fields required"}), 400

    form_data = {
        ENTRIES["name"]: name,
        ENTRIES["email"]: email,
        ENTRIES["message"]: message
    }

    encoded = urllib.parse.urlencode(form_data)
    full_url = GOOGLE_FORM_URL + "?" + encoded

    return jsonify({"msg": "Message sent successfully!", "url": full_url})

if __name__ == "__main__":
    app.run(debug=True)
