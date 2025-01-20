from flask import Flask, request, send_file, render_template
from gtts import gTTS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text")
        lang = request.form.get("lang", "en")  # Default to English

        if not text:
            return "No text provided", 400

        tts = gTTS(text=text, lang=lang)
        audio_file = "output.mp3"
        tts.save(audio_file)

        return send_file(audio_file, as_attachment=True, download_name="output.mp3")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)