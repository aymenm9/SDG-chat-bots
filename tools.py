from typing import Literal,Union
from sdg_exceptions import FunctionCallError

async def sdg_event_registration(first_name:str, last_name:str, email:str, attendance_type:Literal['online', 'onsite'], workshop:int)->Union[str, FunctionCallError]:
    '''
    {
        "first_name": "string",
        "last_name": "string",
        "email": "user@example.com",
        "phone": "string",
        "attendance_type": "string",
        "workshop": 0
    }
    '''
    ...