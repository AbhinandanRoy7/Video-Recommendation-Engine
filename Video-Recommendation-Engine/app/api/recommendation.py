from fastapi import APIRouter, HTTPException
from app.models.model_loader import recommend_videos

router = APIRouter()

@router.get("/feed")
def get_recommendations(user_features: str):
    """
    Accepts user features as a comma-separated string (e.g., "0.5,0.2,0.7")
    and returns recommended video indices.
    """
    try:
        # Convert input string into a list of floats
        user_embedding = [float(x) for x in user_features.split(",")]

        # Get recommendations
        recommended_video_ids = recommend_videos(user_embedding)

        return {"recommended_videos": recommended_video_ids}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
