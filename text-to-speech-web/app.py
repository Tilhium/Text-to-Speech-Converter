from flask import Flask, render_template, request, send_file,jsonify
from gtts import gTTS
import os
import time

app = Flask(__name__)

# Ses dosyalarının saklanacağı klasörü oluştur
audio_folder = "static/audio"  # Ses dosyasının burada saklanmasını sağlıyoruz.
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak():
    text = request.form.get("text")
    lang = request.form.get("lang")

    if not text:
        return "No text provided", 400

    filename = os.path.join(audio_folder, "speech.mp3")

    # Google Text-to-Speech kullanarak sesi oluştur
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    # Dosya URL'sini döndür
    return jsonify({"audio_url": f"/static/audio/speech.mp3"})



@app.route("/reverse_speak", methods=["POST"])
def reverse_speak():
    text = request.form.get("text")
    lang = request.form.get("lang")

    if not text:
        return "No text provided", 400

    reversed_text = text[::-1]  # Metni ters çevir
    filename = os.path.join(audio_folder, "reverse_speech.mp3")

    tts = gTTS(text=reversed_text, lang=lang)
    tts.save(filename)

    # Dosya URL'sini döndür
    return jsonify({"audio_url": f"/static/audio/reverse_speech.mp3"})


if __name__ == "__main__":
    app.run(debug=True)
