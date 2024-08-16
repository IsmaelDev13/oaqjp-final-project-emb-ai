from flask import Flask, render_template, request
from EmotionDetection.detector import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detector_func():
    text_to_analyze=request.args.get("textToAnalyze")
    if text_to_analyze:
        response= emotion_detector(text_to_analyze)
        response_text = (f"For the given statement, the response is 'anger': {response['anger']}, "
                         f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
                         f"'joy': {response['joy']}, 'sadness': {response['sadness']}. The dominant emotion is "
                         f"{response['dominant_emotion']}.")
    else:
        response_text="No text provided for analysis."

    return response_text
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)