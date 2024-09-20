"""This module provides the web server application for emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_emotiondetector():
    """Route handler for emtionDecetor"""
    text_to_analyse = request.args.get('textToAnalyze')
    emotions_response = emotion_detector(text_to_analyse)

    if emotions_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    result = "For the given statement, the system response is "

    result = result + ', '.join(f"'{k}': {v}" for k,v in emotions_response.items()\
     if k != 'dominant_emotion')\
     + f". The dominant emotion is {emotions_response['dominant_emotion']}."
    return result

@app.route("/")
def sent_index_page():
    """Route handler for main page"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
