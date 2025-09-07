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