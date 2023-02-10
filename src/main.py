import os
from fastapi import FastAPI
from src.env import config

MODE=config("MODE", cast=str, default="test")

app = FastAPI() 

@app.get("/") # GET -> HTTP METHOD
def home_page():
    # for API services
    # JSON-ready dict -> json.dumps({'hello': 'world'})
    return {"Hello": "World", "mode": MODE}

# @app.post("/") # POST -> HTTP METHOD
# def home_handle_data_page():
#     # for API services
#     # JSON-ready dict -> json.dumps({'hello': 'world'})
#     return {"Hello": "World"}