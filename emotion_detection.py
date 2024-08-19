import requests  # Import the requests library to handle HTTP requests
import json #Import json to convert text into JSON dictionaries

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Returning a dictionary containing emotion analysis results
    return response.text  # Return the response text from the API

"""
To test this file, on the CLI run:
python 3.11
import json
from emotion_detection import emotion_detector
response = emotion_detector("I love working with this product")
formatted_response = json.loads(response)
print(formatted_response)
"""