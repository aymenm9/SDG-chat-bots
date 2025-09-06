from util import build_config, build_content, build_tools, rebuild_message
from system_instructions import SDG_SYSTEM_INSTRUCTION
from tools_declarations import get_sdg_infos_declarations
from schemas import Massage
from chat_bot import generate_response

async def SDG_chatbot(msg: Massage)->Massage:
    tools = await build_tools([get_sdg_infos_declarations])
    config = await build_config(
        system_instruction=SDG_SYSTEM_INSTRUCTION,
        tools=tools
    )
    content = await build_content(msg)
    response = await generate_response(content, config)
    new_msg = await rebuild_message(msg, response)
    return new_msg