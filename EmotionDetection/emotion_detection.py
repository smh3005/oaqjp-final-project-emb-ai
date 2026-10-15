
import requests


def emotion_detector(text_to_analyze):
    """Analyze text using the Watson NLP emotion detection service."""

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=30
    )

    if response.status_code != 200:
        return None

    result = response.json()
    return result["emotionPredictions"][0]["emotion"]
