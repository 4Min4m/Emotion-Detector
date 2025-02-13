# emotion_detection.py
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

      try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()
        json_response = response.json()

        emotion_predictions = json_response.get('emotionPredictions', [])
        if emotion_predictions:
            first_prediction = emotion_predictions[0]
            emotions = first_prediction.get('emotion', {})

            # Extract the required emotions and scores:
            anger = emotions.get('anger', 0.0)
            disgust = emotions.get('disgust', 0.0)
            fear = emotions.get('fear', 0.0)
            joy = emotions.get('joy', 0.0)
            sadness = emotions.get('sadness', 0.0)

            # Find the dominant emotion:
            dominant_emotion = max(emotions, key=emotions.get) if emotions else "Unknown" # Handle empty emotions

            formatted_output = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
            return formatted_output
        else:
            return None  # No emotion predictions found

    except requests.exceptions.RequestException as e:
        print(f"Error during API call: {e}")
        return None
    except (KeyError, TypeError) as e:
        print(f"Error parsing JSON response: {e}. Response was: {response.text}")
        return None


if __name__ == '__main__':  # This block will only execute if the script is run directly
    test_text = "I love this new technology."
    emotion = emotion_detector(test_text)
    if emotion:
        print(f"The detected emotion for '{test_text}' is: {emotion}")
