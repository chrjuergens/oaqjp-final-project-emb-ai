import json
import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    input_json = { "raw_document": { "text": text_to_analyze } }
    analysis_response = requests.post(url=URL, json=input_json, headers=HEADERS)
    formatted_output = json.loads(analysis_response.text)
    emotionPredictions = formatted_output['emotionPredictions']     # returns a list
    emotions = {}
    for item in emotionPredictions:
        if isinstance(item, dict) and 'emotion' in item.keys():     # identifies the correct list item
            emotions.update(item['emotion'])                        # retrieves 'emotion' data 
            break
    max_score_key = max(emotions.items(), key=lambda x: x[1])       # identifies item with max value
    emotions['dominant_emotion'] = max_score_key[0]                 # adds 'dominant_emotion'
    return emotions

if __name__ == '__main__':
    print(emotion_detector(text_to_analyze='I love this new technology!'))