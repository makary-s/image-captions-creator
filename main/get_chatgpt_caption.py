import base64
from settings import settings
from open_ai_client import open_ai_clent

def get_chatgpt_caption(image_path: str):
    with open(image_path, 'rb') as file:
        base64_image = base64.b64encode(file.read()).decode('utf-8')
    try:
        response = open_ai_clent.chat.completions.create(
            model=settings["open_ai_model"],
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", 
                            "text": settings["query_message"]
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}",
                                "detail": "high"
                            },
                        },
                    ],
                }
            ],
            max_tokens=settings["max_tokens"],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error in getting description from OpenAI: {e}")
        return "Description not available"

