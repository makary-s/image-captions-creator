import os
import json
import sys
from typing import TypedDict

class Settings(TypedDict):
    images_directory: str
    open_ai_key: str
    open_ai_model: str
    query_message: str
    max_tokens: int

settings_file_name = "settings.json"

def create_default_settings():
    settings: Settings = {
        "images_directory": "",
        "open_ai_key": "",
        "open_ai_model": "gpt-4-vision-preview",
        "query_message": "Your task is to describe the person in the image and what surrounds him. The description should be in the form of a simple comma-separated enumeration, use simple language. Your description sentence should start with 'A person' (only once at the very beginning). You should start by describing what is happening in the image (for example, smiling, sitting, playing chess), then move on to details: objects, characters, their characteristics (color, size, texture), environment (time of day, weather, room/outdoors), actions and interactions, general mood (peaceful, sinister, joyful, etc.), and if any abstract elements (metaphors, themes) are available. Do not specify what is not in the image. Don't use dot. Use English.",
        "max_tokens": 300
    }
    with open(settings_file_name, "w") as file:
        json.dump(settings, file, indent=2)


if not os.path.exists("settings.json"):
    create_default_settings()
    print(f"The \"{settings_file_name}\" file was created. Fill it out and restart the script. The script will now exit.")
    sys.exit()

with open(settings_file_name, "r") as file:
    settings: Settings = json.load(file)

