''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion analysis function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection analysis over it using emotion_detector()
        function. The output returned shows the detected emotions and their % score.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the dominant emotion and score from the response
    dominant_emotion = response.get('dominant_emotion', 'UNKNOWN')
    if dominant_emotion is None:
        # Return a specific message if dominant_emotion is None
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment label and score
    return f"The emotions detected are {response}. The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
