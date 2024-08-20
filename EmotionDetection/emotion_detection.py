import requests
import json
import operator

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):

    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create a dictionary with the text to be analyzed    
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers    
    response = requests.post(url, json = myobj, headers=header)
    
    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract emotion scores from the response
    if response.status_code == 200:
        anger_score   = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score    = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score     = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    # If the response status code is 400, set scores to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        anger_score = None
        sadness_score = None

    # Create a Disctionary with emotions and scores
    emotions = {'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    # Calculate the dominant emotion only if the status code is 200
    if response.status_code == 200:
        dominant_emotion = max(emotions.items(), key=operator.itemgetter(1))[0]
    else:
        dominant_emotion = None

    # Add the dominant emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion
    
    # Return the label and score in a dictionary
    return emotions