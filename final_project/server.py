from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import json

# Assuming the emotion_detector function is defined in emotion_detection.py
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    data = request.json
    statement = data.get("statement")
    
    if not statement:
        return jsonify({"error": "No statement provided"}), 400
    
    # Process the statement
    result = emotion_detector(statement)
    
    # Prepare the response
    response = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }
    
    # Formatted response
    formatted_response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    
    return jsonify({"response": response, "formatted_response": formatted_response})

if __name__ == '__main__':
    app.run(debug=True)
