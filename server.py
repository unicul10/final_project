"""
This module contains the server implementation for the Emotion Detection application.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Handles the emotion detection for the given statement.
    """
    data = request.json
    statement = data.get("statement")

    if not statement:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Process the statement using the emotion_detector function
    result = emotion_detector(statement)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400

    # Prepare the response
    formatted_response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': "
        f"{result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': "
        f"{result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion'],
        "formatted_response": formatted_response
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
