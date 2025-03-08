
from dotenv import load_dotenv
import os

load_dotenv()


FLIC_TOKEN = os.getenv("FLIC_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL")


print("FLIC_TOKEN:", FLIC_TOKEN)
print("API_BASE_URL:", API_BASE_URL)


from fastapi import FastAPI
import uvicorn
from app.api.recommendation import router as recommendation_router

from fastapi import FastAPI, Query
import tensorflow as tf
import numpy as np
import json

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))



model = tf.keras.models.load_model("video_recommendation_model.h5")


app = FastAPI()



# Register API routes
app.include_router(recommendation_router, prefix="/api", tags=["recommendation"])

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)









@app.get("/")
def read_root():
    return {"Welcome": "Your Server is LIVE !!! "}
