from fastapi import FastAPI
from pydantic import BaseModel
from code_translator import main as translater
from code_enhancer import main as enhancer
from call_pipeline import main as call_pipeline
from check_pipeline import main as check_pipeline

# Define a Pydantic model for the request body
class Body(BaseModel):
    url: str


app = FastAPI()
# TODO manage all the returns

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/translate/")
def translate(body: Body):
    translater("./legacyproject") 
    return {"Hello": "World"}

@app.post("/enhance/")
def enhance(body: Body):
    enhancer("./legacyproject") 
    return {"Hello": "World"}

@app.post("/call_pipeline/")
def call_pipeline():
    call_pipeline() 
    return {"Hello": "World"}

@app.get("/check_pipeline/")
def check_pipeline():
    check_pipeline() 
    return {"Hello": "World"}