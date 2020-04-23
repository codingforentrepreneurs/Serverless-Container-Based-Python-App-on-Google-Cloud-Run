from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_index():
    return {"Hello": "World"}

@app.post("/scrape")
def trigger_scraping():
    return {"scraping": "yes"}