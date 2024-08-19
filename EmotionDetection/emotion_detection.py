"""
Made using NLP library for Emotion Analysis function of the Watson NLP Library
"""
import requests  # Import the requests library to handle HTTP requests
import json #Import json to convert text into JSON dictionaries

def emotion_detector(text_to_analyze):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Check if emotion predictions are present
    if 'emotionPredictions' not in formatted_response or not formatted_response['emotionPredictions']:
        return "Error: No emotion predictions found in the response."

    # Extract the required emotions and their scores. 
    #If the emotion does not exist in the dictionary, the method will return 0.0
    emotions = formatted_response.get('emotionPredictions', [{}])[0].get('emotion', {})
    anger_score = emotions.get('anger', 0.0)
    disgust_score = emotions.get('disgust', 0.0)
    fear_score = emotions.get('fear', 0.0)
    joy_score = emotions.get('joy', 0.0)
    sadness_score = emotions.get('sadness', 0.0)

    # Determine the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
        }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Returning a dictionary containing emotion analysis results
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }

"""
To test this file, on the CLI run:
python 3.11
import json
from emotion_detection import emotion_detector
response = emotion_detector("I am so happy I am doing this")
print(response)
"""
