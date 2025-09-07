from google import genai
from google.genai import types
from dotenv import load_dotenv
from schemas import Massage

load_dotenv()

client = genai.Client()


async def generate_summary(msg: Massage)-> Massage:
    print("Generating summary...")
    config = types.GenerateContentConfig(
    system_instruction = """
    Your task is to create a new, concise summary that combines a previous summary with the latest messages. The final summary should contain the essential information needed to maintain context.
    """
    )
    contents = [
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=f"old summary:{msg.summary if msg.summary else 'No previous summary yet.'}"),
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
        print(f"Added to summary contents: role={m.role}, content={m.content}")
    contents.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="Based on the previous summary and the new messages, generate an updated summary that captures the key points and context of the conversation so far, prioritize the last messages context."),
            ],
        ),
    )
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=contents,
        config=config,
    )
    new_summary = response.text
    msg.summary = new_summary
    msg.history = []
    print(f"\n\nresponse received: {response}\n\n")
    return msg
