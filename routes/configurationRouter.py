from fastapi import APIRouter, File, UploadFile
import shutil
import os

UPLOAD_DIRECTORY = "./uploads/"

router = APIRouter(prefix='/configurations', tags=['Configuratinos Endpoints'])

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@router.post('/upload')
async def uploadFile(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    return {"info": f"File '{file.filename}' saved at '{file_location}'"}