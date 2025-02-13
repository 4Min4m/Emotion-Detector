# server.py
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Renders the index.html template."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """Detects the dominant emotion in a given text."""
    text = request.form.get('text')
    if not text:
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text)

    if result is None:
        return jsonify({"error": "Error processing text"}), 500

    dominant_emotion = result.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400

    output_string = f"For the given statement, the system response is "

    for emotion, score in result.items():
        if emotion != 'dominant_emotion':
            output_string += f"'{emotion}': {score}, "

    output_string = output_string[:-2] + f". The dominant emotion is {dominant_emotion}."

    return output_string, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
