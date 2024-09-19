from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_emotionDetector():
    text_to_analyse = request.args.get('textToAnalyze')
    emotions_response = emotion_detector(text_to_analyse)
    result = f"For the given statement, the system response is "

    result = result + ', '.join(f"'{k}': {v}" for k,v in emotions_response.items() if k != 'dominant_emotion') + f". The dominant emotion is {emotions_response['dominant_emotion']}."
    return result

@app.route("/")
def sent_index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)