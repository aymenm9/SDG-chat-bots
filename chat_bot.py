from google import genai
from google.genai import types
from dotenv import load_dotenv
from schemas import Massage
from infos import get_infos
from models_manager import Models_manager
from sdg_exceptions import ModelUnavailableError, FunctionCallError
from tools import sll_event_registration
load_dotenv()

client = genai.Client()

async def generate_response_ABC(contents: list[types.Content], config: types.GenerateContentConfig, model: str) -> types.GenerateContentResponse:
    print("Generating response...")
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=config,
    )
    return response

async def generate_response(contents: list[types.Content], config: types.GenerateContentConfig, model: str) -> str:
    print("Generating response...")
    response =await generate_response_ABC(contents, config, model)
    return response.text

async def generate_response_with_functions(contents: list[types.Content], config: types.GenerateContentConfig, model: str) -> str:
    print("Generating response...")
    response = await generate_response_ABC(contents, config, model)
    if response.candidates[0].content.parts[0].function_call:
        return await function_call_execution(response, contents, config)
    else:
        return response.text

async def function_call_execution(response, contents, config):
    '''
    for now we only have one function call to event registration 
    '''
    function_call = response.candidates[0].content.parts[0].function_call
    if function_call.name == "sll_event_registration":
        args = function_call.args
        print(f"Function call detected: {function_call.name} with args {args}")
        function_response = await sll_event_registration(**args)
        print(f"user was registered to {function_response}")
            
        return 'you were registered to ' + function_response + ' successfully'
    else:
        raise Exception(f"Function call not supported: {function_call.name}")