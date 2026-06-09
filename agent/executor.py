import json
from agent.context import context

from agent.router import execute_tool


def execute_plan(plan_json):

    plan = json.loads(
        plan_json
    )

    results = []

    for step in plan:

        tool_name = step.get(
            "tool"
        )

        parameters = step.get(
            "parameters",
            {}
        )

        tool_call = {
            "tool": tool_name,
            "parameters": parameters
        }

        result = execute_tool(
            json.dumps(tool_call)
        )
        print(
            "\nEXECUTOR RESULT:"
        )
        print(result)
        context.set(
            tool_name,
            result
        )

        results.append({
            "tool": tool_name,
            "result": result
        })

    return results