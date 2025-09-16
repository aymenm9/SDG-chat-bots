import asyncio
from util import build_config, build_content, build_tools, rebuild_message, build_system_instructions
from system_instructions import SDG_SYSTEM_INSTRUCTION
from infos import get_sdg_info, sdg_info, sdg_static_replay
from schemas import Massage
from chat_bot import generate_response
from sdg_exceptions import ModelUnavailableError, FunctionCallError
from static_bot import msg_static_replay
from google.genai import types
from models_manager import Models_manager

'''
async def SDG_chatbot(msg: Massage)->Massage:
    try:
        if sdg_info.get(msg.message):
            response = sdg_info.get(msg.message)
        else:
            #tools_task = asyncio.create_task(build_tools([get_sdg_infos_declarations]))
            content_task = asyncio.create_task(build_content(msg))
            #tools = await tools_task
            config_task = asyncio.create_task(
                build_config(system_instruction=SDG_SYSTEM_INSTRUCTION + 'the information about SDG: \n' + get_sdg_info(), tools=None)
            )
            config, content = await asyncio.gather(config_task, content_task)
            response = await generate_response(content, config)

        new_msg = await rebuild_message(msg, response)
        return new_msg
    except ModelUnavailableError as e:
        response = "Sorry, the model is currently unavailable. Please try again later."
        new_msg = await rebuild_message(msg, response)
        return new_msg
    except FunctionCallError as e:
        response = "Sorry, there was an error processing your request. Please try again later."
        new_msg = await rebuild_message(msg, response)
        return new_msg
'''

async def SDG_chatbot(msg: Massage)->Massage:
    return await chatbot(msg, SDG_SYSTEM_INSTRUCTION, 'SDG', sdg_info,sdg_static_replay,None)

async def chatbot(msg: Massage,system_instructions:str,name:str, infos:dict, static_replay:dict, tools:list = None)->Massage:
    try:
        if rep := msg_static_replay(msg.message,infos, static_replay):
            response = rep
        else:
            #tools_task = asyncio.create_task(build_tools([get_sdg_infos_declarations]))
            content_task = asyncio.create_task(build_content(msg))
            #tools = await tools_task
            config_task = asyncio.create_task(
                build_config(system_instruction= await build_system_instructions(system_instructions, infos, name), tools_declarations=tools)
            )
            config, content = await asyncio.gather(config_task, content_task)
            response = await generate_response(content, config,Models_manager.get_model())

        new_msg = await rebuild_message(msg, response)
        return new_msg
    except ModelUnavailableError as e:
        response = "Sorry, the model is currently unavailable. Please try again later."
        new_msg = await rebuild_message(msg, response)
        return new_msg
    except FunctionCallError as e:
        response = "Sorry, there was an error processing your request. Please try again later."
        new_msg = await rebuild_message(msg, response)
        return new_msg
    except Exception as e:
        print(e)
        response = "Sorry, there was an error processing your request. Please try again later."
        new_msg = await rebuild_message(msg, response)
        return new_msg