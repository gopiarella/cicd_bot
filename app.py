from flask import Flask, request, render_template
import os
from google import genai

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ.get("GOOGLE_GEMINI_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def chat():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["message"]
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=user_input
        )
        response_text = response.text

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
