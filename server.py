''' Server code for analyzing and detecting emotion through text using Watsons NLP '''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

''' app routes for the emotion detector and rendering index page '''
@app.route("/emotionDetector", methods=['GET', 'POST'])
def emo_detector():
    ''' takes the input of the user and calls the emotion_detector function to
    analyze the emotion from the text and provides the dominant emotion '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is {result}"

@app.route("/")
def render_index_page():
    ''' renders the index page / index.html '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
