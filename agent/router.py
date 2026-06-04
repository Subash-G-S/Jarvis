# agent/router.py

import json

from agent.tool_registry import TOOLS


def execute_tool(llm_response):

    data = json.loads(llm_response)

    tool_name = data.get("tool")

    if tool_name not in TOOLS:
        return f"Unknown tool: {tool_name}"

    tool = TOOLS[tool_name]["function"]

    params = data.get("parameters", {})

    if params:
        return tool(**params)

    return tool()