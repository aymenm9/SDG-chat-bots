# SDG Tools
sdg_info_tools = {

# about_SDG
"about_SDG":"we are a student scientific and development group at the University of Setif",

# SDG_activities
"SDG_activities":"not availbel for now",
# SDG_methodology
"SDG_methodology":"not availbel for now",
# SDG_mission
"SDG_mission":"not availbel for now",
# how_to_join_SDG
"how_to_join_SDG":"not availbel for now",
# SDG_membership_benefits
"SDG_membership_benefits":"not availbel for now",
# SDG_team_members
"SDG_team_members":"not availbel for now",
# SDG_upcoming_events
"SDG_upcoming_events":"not availbel for now",
# SDG_location
"SDG_location":"not availbel for now",
# SDG_operating_time
"SDG_operating_time":"not availbel for now",
# SDG_membership_requirements
"SDG_membership_requirements":"not availbel for now",
# SDG_member_required_capacities
"SDG_member_required_capacities":"not availbel for now",
# SDG_member_responsibilities
"SDG_member_responsibilities":"not availbel for now",

# Event Tools:

# Event SDG focus
"Event_SDG_focus":"not availbel for now",
# about the event
"about_the_event":"not availbel for now",
# Event target audience
"Event_target_audience":"not availbel for now",
# Event objectives
"Event_objectives":"not availbel for now",
# Event registration information
"Event_registration_information":"not availbel for now",
# Event location
"Event_location":"not availbel for now",
# Event time
"Event_time":"not availbel for now",
# Event schedule
"Event_schedule":"not availbel for now",
# Event speakers
"Event_speakers":"not availbel for now",
# Event partners
"Event_partners":"not availbel for now",

# Podcast Tools:

# Podcast SDG focus
"Podcast_SDG_focus":"not availbel for now",
# Podcast description
"Podcast_description":"not availbel for now",
# Podcast platforms
"Podcast_platforms":"not availbel for now",
# Podcast release schedule
"Podcast_release_schedule":"not availbel for now",
# Podcast guests
"Podcast_guests":"not availbel for now",
# Podcast partners
"Podcast_partners":"not availbel for now",
}

def get_infos(tool_names: list) -> str:
    """
    Retrieves information about a list of tools.

    This function takes a list of tool names as input and returns a list of strings,
    where each string contains the information associated with the corresponding tool name
    from the `sdg_info_tools` dictionary.

    Args:
        tool_names: A list of strings, where each string is a valid tool name
                    present in the `sdg_info_tools` dictionary.

    Returns:
        A string containing the information for each requested tool, formatted as:
        "tool_name: tool_info\n" for each tool in the input list.
    """
    print(f"Retrieving infos for tools: {tool_names}")
    infos = ''
    for tool_name in tool_names:
        infos +=  tool_name + ': ' + sdg_info_tools[tool_name] + '\n'
    return infos