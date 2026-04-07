from fastapi import APIRouter
from app.services.emotion_service import get_emotion_service
from app.services.intensity_service import IntensityService

router = APIRouter()
intensity_service = IntensityService()


@router.post("/analyze-emotion")
def analyze_emotion(text: str):
    emotion_service = get_emotion_service()

    top_emotions = emotion_service.get_top_emotions(text)

    # Add intensity to each emotion
    enriched = []
    for emo in top_emotions:
        intensity = intensity_service.calculate_intensity(text, emo["score"])

        enriched.append({
            "emotion": emo["label"],
            "confidence": round(emo["score"], 3),
            "intensity": intensity
        })

    return {
        "input_text": text,
        "analysis": enriched
    }


