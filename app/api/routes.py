from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

api_router = APIRouter()

@api_router.get("/nours-image")
async def get_nours_image():

    image_path = os.path.join("static", "images", "nours.png")