from google.genai import types
from schemas import Massage
from summary import generate_summary
async def build_config(system_instruction:str, tools:types.Tool)-> types.GenerateContentConfig:
    config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
    system_instruction = system_instruction,
    tools=[tools]
    )
    return config



async def build_tools_declarations(tools_declarations:list)-> types.Tool:
    tools_list = []
    for declaration in tools_declarations:
        tools_list.append(declaration)
    tools = types.Tool(   
        function_declarations=tools_list
    )
    return tools

async def build_content(message:Massage)-> list[types.Content]:
    if len(message.history) >= 8:
        massage = await generate_summary(message)
    content = [
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=message.summary),
            ],
        ),
    ]
    for m in message.history:
        content.append(
            types.Content(
                role=m.role,
                parts=[
                    types.Part.from_text(text=m.content),
                ],
            ),
        )
    content.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=message.message),
            ],
        ),
    )
    return content
