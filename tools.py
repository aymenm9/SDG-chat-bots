from typing import Literal,Union
from sdg_exceptions import FunctionCallError
from dotenv import load_dotenv
import requests
import os
load_dotenv()

API_URL = os.getenv("API_URL")



async def sll_event_registration(first_name:str, last_name:str, email:str, phone_number:str, attendance_type:Literal['online', 'on-site'], workshop:int)->Union[str, FunctionCallError]:
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
    try:
        print(f"Registering {first_name} {last_name} for workshop {workshop} with email {email} as {attendance_type}")
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
            "attendance_type": attendance_type,
            "workshop": workshop,
        }
    
        print(f"Sending registration request with payload: {payload}")
        response = requests.post(f"{API_URL}/api/registrations/", json=payload,headers={"Content-Type": "application/json", 'SSL-Chatbot-Key': os.getenv("CHATBOT_API_KEY")})
        print(f"Registration response: {response.json()}")
        response.raise_for_status()
        return response.json().get("workshop_name", "the workshop")
    except requests.RequestException as e:
        print(f"Error during event registration: {e}")
        raise FunctionCallError("Failed to register for the event.") from e


async def get_available_to_register_workshops():
    try:
        response = requests.get(f"{API_URL}/api/workshops/")
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching available workshops: {e}")
        return []

async def get_workshop_from_name(name: str)->int:
    workshops = await get_available_to_register_workshops()
    for workshop in workshops:
        print(f"Found workshop: {workshop['title']} (ID: {workshop['id']}) searching for {name}")
        if workshop["title"] == name:
            print(f"---- Workshop found: {workshop['title']} (ID: {workshop['id']})")
            return int(workshop["id"])
    return None