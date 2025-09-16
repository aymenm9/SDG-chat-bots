from google.genai import types
from schemas import Massage, Msg
from summary import generate_summary
async def build_config(system_instruction:str, tools_declarations:list = None,)-> types.GenerateContentConfig:
    print('Building config...')
    config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
    system_instruction = system_instruction,
    )
    if tools_declarations:
        tools = await build_tools(tools_declarations)
        config.tools = tools
    return config

async def build_system_instructions(instructions:str, chatbot_infos:dict, chatbot_name:str):
    sys_instructions = instructions + f'the information about {chatbot_name}: \n'
    for key, info in chatbot_infos.items():
        sys_instructions += f'{key} : {info},\n'
    return sys_instructions
    

async def build_tools(tools_declarations:list)-> types.Tool:
    print('Building tools...')
    tools_list = []
    for declaration in tools_declarations:
        tools_list.append(declaration)
    tools = types.Tool(   
        function_declarations=tools_list
    )
    return tools

async def build_content(message:Massage)-> list[types.Content]:
    print('Building content...')
    if len(message.history) >= 16:
        message = await generate_summary(message)
    contents = [
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=message.summary),
            ],
        ),
    ] if message.summary else []
    for m in message.history:
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
                types.Part.from_text(text=message.message),
            ],
        ),
    )
    return contents


async def rebuild_message(message:Massage, response:str)-> Massage:
    print('Rebuilding message...')
    message.history.append(
        Msg(
            role="user",
            content=message.message,
        )
    )
    message.history.append(
        Msg(
            role="model",
            content=response,
        )
    )
    message.message = response
    return message 