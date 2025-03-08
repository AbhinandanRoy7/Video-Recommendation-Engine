import tensorflow as tf
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("video_recommendation_model.h5")

def recommend_videos(user_embedding):
    """
        this function will accept user features and will return recommended video indices.
    """
    try:
        
        user_embedding = np.array(user_embedding).reshape(1, -1)  

        # Make predictions
        predictions = model.predict(user_embedding)

        # getting the top 5 recommended video indices
        recommended_video_ids = np.argsort(predictions[0])[-5:][::-1]

        return recommended_video_ids.tolist()  # Convert NumPy array to list for JSON response

    except Exception as e:
        return str(e)
