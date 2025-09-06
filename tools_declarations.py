get_infos_declarations = {
    "name": "get_infos",
    "description": "Retrieve information about a list of tools.",
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
