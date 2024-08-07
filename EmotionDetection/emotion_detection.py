import requests

def emotion_detector(text):
    # URL for the emotion detection service
    url = "http://your-emotion-detection-service-endpoint"
    
    if not text.strip():  # Check if the text is blank or contains only whitespace
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Make the request to the emotion detection service
    response = requests.post(url, json={"text": text})

    # Handle response errors
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # If the request was successful, process the response
    response_json = response.json()

    # Extract emotion scores
    emotion_scores = response_json.get('emotionPredictions', [{}])[0].get('emotion', {})
    dominant_emotion = max(emotion_scores, key=emotion_scores.get, default=None)

    return {
        'anger': emotion_scores.get('anger', None),
        'disgust': emotion_scores.get('disgust', None),
        'fear': emotion_scores.get('fear', None),
        'joy': emotion_scores.get('joy', None),
        'sadness': emotion_scores.get('sadness', None),
        'dominant_emotion': dominant_emotion
    }
