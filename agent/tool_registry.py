# agent/tool_registry.py
from tools.file_search_tools import search_files
from tools.file_open_tools import open_file
from tools.file_tools import (
    create_folder,
    create_file,
    delete_file,
    rename_file
)
from tools.screenshot_tools import (
    take_screenshot,
    open_latest_screenshot,
    timed_screenshot
)
from tools.system_tools import get_system_info
from tools.memory_tools import open_last_file
from tools.system_tools import (
    get_ram_usage,
    get_disk_space
)
from tools.process_tools import close_app
from tools.system_tools import get_battery_status
from tools.system_tools import (get_cpu_usage, list_running_apps)

from tools.app_tools import (
    open_app
)


TOOLS = {

    "create_folder": {
        "function": create_folder,
        "description": "Create a folder",
        "parameters": ["folder_name"]
    },

    "create_file": {
        "function": create_file,
        "description": "Create a file",
        "parameters": ["file_name"]
    },

    "delete_file": {
        "function": delete_file,
        "description": "Delete a file",
        "parameters": ["file_name"]
    },

    "get_ram_usage": {
        "function": get_ram_usage,
        "description": "Get RAM usage",
        "parameters": []
    },

    "get_disk_space": {
        "function": get_disk_space,
        "description": "Get disk space",
        "parameters": []
    },

    "open_app": {
        "function": open_app,
        "description": "Open an application",
        "parameters": ["app_name"]
    },
    "search_files": {
        "function": search_files,
        "description": "Search files by keyword",
        "parameters": ["keyword"]
    },
    "open_file": {
        "function": open_file,
        "description": "Open a file",
        "parameters": ["file_name"]
    },
    "rename_file": {
    "function": rename_file,
    "description": "Rename a file",
    "parameters": ["old_name", "new_name"]
},
"get_system_info": {
    "function": get_system_info,
    "description": "Get complete system information",
    "parameters": []
},
"open_last_file": {
    "function": open_last_file,
    "description": "Open the most recently referenced file",
    "parameters": []
},
"get_battery_status": {
    "function": get_battery_status,
    "description": "Get battery percentage and charging status",
    "parameters": []
},
"get_cpu_usage": {
    "function": get_cpu_usage,
    "description": "Get current CPU usage",
    "parameters": []
},
"list_running_apps": {
    "function": list_running_apps,
    "description": "List currently running applications",
    "parameters": []
},
"close_app": {
    "function": close_app,
    "description": "Close a running application",
    "parameters": ["app_name"]
},
"take_screenshot": {
    "function": take_screenshot,
    "description": "Take a screenshot",
    "parameters": []
},

"open_latest_screenshot": {
    "function": open_latest_screenshot,
    "description": "Open the latest screenshot",
    "parameters": []
},

"timed_screenshot": {
    "function": timed_screenshot,
    "description": "Take a screenshot after delay",
    "parameters": ["seconds"]
},

}


def generate_tool_prompt():

    prompt = """
You are Jarvis.

IMPORTANT:

Return ONLY valid JSON.

Always use this format:

{
    "tool": "tool_name",
    "parameters": {}
}

Examples:

{
    "tool":"get_ram_usage",
    "parameters":{}
}

{
    "tool":"get_disk_space",
    "parameters":{}
}

{
    "tool":"open_app",
    "parameters":{
        "app_name":"chrome"
    }
}

{
    "tool":"create_folder",
    "parameters":{
        "folder_name":"AI Projects"
    }
}
{
  "tool":"search_files",
  "parameters":{
    "keyword":"resume"
  }
}
{
  "tool":"open_file",
  "parameters":{
    "file_name":"resume.pdf"
  }
}
{
  "tool":"rename_file",
  "parameters":{
    "old_name":"report.pdf",
    "new_name":"final_report.pdf"
  }
}
{
  "tool":"get_system_info",
  "parameters":{}
}
{
  "tool":"open_last_file",
  "parameters":{}
}
{
  "tool":"get_battery_status",
  "parameters":{}
}
{
  "tool":"get_cpu_usage",
  "parameters":{}
}
{
  "tool":"list_running_apps",
  "parameters":{}
}
{
  "tool":"close_app",
  "parameters":{}
}
{
  "tool":"take_screenshot",
  "parameters":{}
}
Available tools:

"""

    for tool_name, tool_info in TOOLS.items():

        prompt += f"""

Tool Name: {tool_name}
Description: {tool_info['description']}
Parameters: {tool_info['parameters']}
"""

    return prompt