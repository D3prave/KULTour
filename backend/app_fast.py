from fastapi import FastAPI
from flask import jsonify, request
from collab_filt_svd import CollaborativeFiltering

app = FastAPI()

collab_filtering = CollaborativeFiltering('prepared_data.csv')

@app.get("/data")
def get_data():
    data_frame = collab_filtering.data
    data_json = data_frame.to_json(orient='records')
    return {"Here": data_json}

@app.post('/recommendation')
def get_recommendation(text: str):
    #user_data = request.get_json()
    recommendations_df = collab_filtering.get_recommendations()
    recommendations_json = recommendations_df.to_json(orient='records')
    return {'recommendations': recommendations_json}

