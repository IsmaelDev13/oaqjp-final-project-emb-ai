from flask import Flask, render_template, request, jsonify
from EmotionDetection.detector import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_detector_func():
    text_to_analyze=request.args.get("textToAnalyze")
    if not text_to_analyze:
        return jsonify({
            'anger':None,
            'disgust':None,
            'fear': None,
            'joy': None,
            'sadness':None,
            'dominant_emotion':None,
            'message': "Invalid text! Please try again!"
        }),400

    
    try:
        # Call the emotion detector function
        response = emotion_detector(text_to_analyze)
        if response.get('dominant_emotion') is None:
            return jsonify({
                'anger': response.get('anger'),
                'disgust': response.get('disgust'),
                'fear': response.get('fear'),
                'joy': response.get('joy'),
                'sadness': response.get('sadness'),
                'dominant_emotion': None,
                'message': "Invalid text! Please try again!"
            }), 400
        # Return the response in JSON format with a 200 status code
        return jsonify({
            'anger': response.get('anger'),
            'disgust': response.get('disgust'),
            'fear': response.get('fear'),
            'joy': response.get('joy'),
            'sadness': response.get('sadness'),
            'dominant_emotion': response.get('dominant_emotion')
        }), 200
    
    except Exception as e:
        # Handle unexpected errors and return a 500 status code
        return jsonify({
            'error': str(e),
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 500

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)