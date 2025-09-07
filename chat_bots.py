import asyncio
from util import build_config, build_content, build_tools, rebuild_message
from system_instructions import SDG_SYSTEM_INSTRUCTION
from tools import get_sdg_info
from schemas import Massage
from chat_bot import generate_response

async def SDG_chatbot(msg: Massage)->Massage:
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