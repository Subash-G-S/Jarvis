from agent.tool_registry import TOOLS


def get_available_tools():

    tools_text = ""

    for name, info in TOOLS.items():

        tools_text += (
            f"\nTool: {name}\n"
            f"Description: {info['description']}\n"
        )

    return tools_text