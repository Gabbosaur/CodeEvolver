import shutil
import os

from pydantic import BaseModel
from code_translator import main as translater
from code_enhancer import main as enhancer
from move_project_to_pipeline import main as move_to_pipeline
from call_pipeline import main as call_pipeline
from check_pipeline import main as check_pipeline
from fastapi.responses import FileResponse
from fastapi import FastAPI, Response


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
    translater(body.url) 
    return {"Hello": "World"}

@app.post("/enhance/")
def enhance():
    enhancer()
    # enhancer("./evolved") 
    return {"Hello": "World"}

@app.post("/call_pipeline/")
def call_pipeline_endpoint():
    call_pipeline() 
    return {"Hello": "World"}

@app.get("/check_pipeline/")
def check_pipeline_endpoint():
    check_pipeline() 
    return {"Hello": "World"}

@app.post("/evolve/")
def evolve(body: Body):
    translate(body)
    enhance()
    # move_to_pipeline()       
    # call_pipeline()
    return "OK"
    #return check_pipeline()

@app.get("/download_folder")
async def download_folder():
    zip_file_name = "source_code.zip"
    folder_to_zip = "evolved"
    # Create zip file
    shutil.make_archive("source_code", 'zip', folder_to_zip)

    # Check if the file was created and exists
    if os.path.exists(zip_file_name):
        # Return the zip file for download
        return FileResponse(zip_file_name, media_type="application/x-zip-compressed", filename=zip_file_name)
    else:
        return Response(content="Error: Zip file not found", status_code=404)