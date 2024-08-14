from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    text_to_detect = request.args.get('textToAnalyze')
    
    if not text_to_detect:
        return "Invalid text! Please try again!."
    
    response = emotion_detector(text_to_detect)
    
    if not response or response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    
    return (
        f"The analysis of your statement yields the following emotions: "
        f"anger: {response['anger']:.4f}, disgust: {response['disgust']:.4f}, "
        f"fear: {response['fear']:.4f}, joy: {response['joy']:.4f}, and "
        f"sadness: {response['sadness']:.4f}. "
        f"The dominant emotion detected is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
