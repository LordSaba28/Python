from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Your anime folder
ANIME_FOLDER = r"C:\Users\Saba\Videos\Anime"


@app.route("/")
def home():
    files = os.listdir(ANIME_FOLDER)

    # filter only video files (basic)
    videos = [f for f in files if f.endswith((".mp4", ".mkv", ".webm"))]

    return render_template("index.html", videos=videos)


@app.route("/video/<filename>")
def video(filename):
    return send_from_directory(ANIME_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)
