'''
# the ai should sent a valid list of info to loock for so tool_names should be in the tools dict keys
get_sdg_infos_declarations = {
    "name": "get_infos",
    "description": "Retrieve information about a list of info topics related to the Setif Development Group (SDG), with include only  [about_SDG, SDG_activities, SDG_methodology, SDG_mission, how_to_join_SDG, SDG_membership_benefits, SDG_team_members, SDG_upcoming_events, SDG_location, SDG_operating_time, SDG_membership_requirements, SDG_member_required_capacities, SDG_member_responsibilities].",
    "parameters": {
        "type": "object",
        "properties": {
            "tool_names": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        },
        "required": ["tool_names"],
    },
}
'''

registration_declarations = {
    "name": "sll_event_registration",
    "description": "Register a user for a workshop at the SDG Skills Lab (SSL) Event. The user must provide their first name, last name, email, attendance type (either 'online' or 'on-site'), and the workshop they wish to attend (identified by its ID).",
    "parameters": {
        "type": "object",
        "properties": {
            "first_name": {
                "type": "string",
                "description": "The first name of the participant."
            },
            "last_name": {
                "type": "string",
                "description": "The last name of the participant."
            },
            "email": {
                "type": "string",
                "description": "The email address of the participant."
            },
            "phone_number": {
                "type": "string",
                "description": "The phone number of the participant."
            },
            "attendance_type": {
                "type": "string",
                "enum": ["online", "on-site"],
                "description": "The type of attendance for the participant, either 'online' or 'on-site'."
            },
            "workshop": {
                "type": "integer",
                "description": "The ID of the workshop the participant wishes to attend."
            }
        },
        "required": ["first_name", "last_name", "email", "attendance_type", "workshop"],
    },
}


