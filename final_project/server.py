# server.py
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  # Import from your package

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    text = request.form.get('text')  # Get text from the form
    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = emotion_detector(text)
    if result is None:  # Handle cases when emotion_detector returns None (errors)
        return jsonify({"error": "Error processing text"}), 500

    dominant_emotion = result.get('dominant_emotion', 'Unknown')
    output_string = f"For the given statement, the system response is "

    for emotion, score in result.items():
        if emotion != 'dominant_emotion':
            output_string += f"'{emotion}': {score}, "
    
    output_string = output_string[:-2] + f". The dominant emotion is {dominant_emotion}." #remove last comma and space, add dominant emotion

    return output_string, 200 # Return the formatted string

@app.route('/', methods=['GET']) # Serve index.html
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) # Host set to 0.0.0.0 to make it accessible in the labs
