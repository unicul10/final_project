import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL and headers for the API request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert the response text to a dictionary
    response_dict = json.loads(response.text)
    
    # Extract the required set of emotions and their scores
    # Accessing the first element in emotionPredictions list and then the emotion dictionary
    emotions = response_dict.get('emotionPredictions', [{}])[0].get('emotion', {})
    
    # Extract relevant emotions
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Find the dominant emotion
    relevant_emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(relevant_emotions, key=relevant_emotions.get)
    
    # Prepare the output format
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result