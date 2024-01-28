from openai import OpenAI
from settings import settings

open_ai_clent: OpenAI = OpenAI(
    api_key=settings["open_ai_key"],
)
