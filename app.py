from flask import Flask, render_template, request
from youtube_api import get_video_data
from summarization_model import summarize_video
from evaluation_model import evaluate_video

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    video_links = request.form['video_links'].splitlines()
    best_video = None
    best_score = float('-inf')
    summary = ""

    for link in video_links:
        video_data = get_video_data(link)
        score = evaluate_video(video_data)
        video_summary = summarize_video(video_data)

        if score > best_score:
            best_score = score
            best_video = video_data
            summary = video_summary

    return render_template('results.html', video=best_video, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
