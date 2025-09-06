from google import genai
from google.genai import types
from dotenv import load_dotenv
from schemas import Massage
from tools import get_infos
load_dotenv()

client = genai.Client()

async def generate_response(contents: list[types.Content], config: types.GenerateContentConfig) -> str:
    print("Generating response...")
    response = client.models.generate_content(
        model='gemini-2.0-flash-lite',
        contents=contents,
        config=config,
    )
    if response.candidates[0].content.parts[0].function_call:
        function_call = response.candidates[0].content.parts[0].function_call
        if function_call.name == "get_infos":
            args = function_call.args
            print(f"Function call detected: {function_call.name} with args {args}, tool_names: {args['tool_names']}")
            function_response = get_infos(args['tool_names'])
            fn_response_part = types.Part.from_function_response(name=function_call.name, response={"function_response": function_response})
            contents.append(
                response.candidates[0].content
            )
            contents.append(
                fn_response_part
            )
            print(f"Contents after function call: {function_response}")
            response = client.models.generate_content(
                model='gemini-2.0-flash-lite',
                contents=contents,
                config=config,
            )
    return response.text
