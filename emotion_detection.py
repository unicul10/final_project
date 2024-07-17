import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    textObj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=textObj, headers=headers)

    formatted_response = json.loads(response.text)

    emotion_predictions = formatted_response.get('emotionPredictions', [])
    if emotion_predictions:
        emotions = emotion_predictions[0].get('emotion', {})
        dominant_emotion = max(emotions, key=emotions.get)
            
        formatted_emotion = {**emotions, 'dominant_emotion': dominant_emotion}
        return formatted_emotion
    else:
        print("No emotion predictions found in the response.")
        return None

    return (formatted_emotion)
