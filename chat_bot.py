from google import genai
from google.genai import types
from dotenv import load_dotenv
from schemas import Massage

load_dotenv()

client = genai.Client()
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
    system_instruction = """You are a helpful assistant that provides information about the Sustainable Development Goals (SDGs)."""
)

async def generate_response(msg: Massage)-> Massage:
    contents = [

    ]
    for m in msg.history:
        contents.append(
            types.Content(
                role=m.role,
                parts=[
                    types.Part.from_text(text=m.content),
                ],
            ),
        )
    contents.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=msg.message),
            ],
        ),
    )
    response = client.models.generate_content(
        model='gemini-2.0-flash-lite',
        contents=contents,
        config=config,
    )
    print(response.text)
    return msg
