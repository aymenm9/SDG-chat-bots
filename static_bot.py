from typing import Union


def msg_static_replay(msg:str, msg_static:dict, infos: dict)-> Union[str,None]:
    return msg_static.get(msg) or infos.get(msg)