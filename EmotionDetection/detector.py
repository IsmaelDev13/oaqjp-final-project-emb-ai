import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        print("Raw API Response:", response.json())
        response_data= response.json()
        emotions = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
        
        required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        emotion_scores = {emotion: emotions.get(emotion, 0.0) for emotion in required_emotions}
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
        return emotion_scores
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}