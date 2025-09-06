from google import genai
from google.genai import types
from dotenv import load_dotenv
from schemas import Massage

load_dotenv()

client = genai.Client()
config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
    system_instruction = """
        Your task is to summarize a conversation for a large language model. You will be provided with a previous summary and the latest messages.

        Create a new, concise summary that combines the old summary with the new messages. The final summary should contain only the essential information needed to maintain context for the chatbot's next response, focusing on key facts and the user's recent intent.
        """
    )

async def generate_summary(msg: Massage)-> Massage:
    print("Generating summary...")

    contents = [
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=f"masseges summary:{msg.summary}"),
            ],
        )
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
    response = client.models.generate_content(
        model='gemini-2.0-flash-lite',
        contents=contents,
        config=config,
    )
    new_summary = response.text
    msg.summary = new_summary
    msg.history = []
    return msg
