# agent/tool_registry.py
from tools.file_search_tools import search_files
from tools.file_open_tools import open_file
from tools.file_tools import (
    create_folder,
    create_file,
    delete_file,
    rename_file,
    get_last_generated_file
)
from tools.email_tools import email_last_file
from tools.search_tools import (
    web_search
)
from tools.excel_tools import (
    create_excel
)

from tools.browser_tools import (
    search_web
)
from tools.preferences_tools import (
    set_preference,
    get_preference,
    delete_preference
)
from tools.notes_tools import (
    add_note,
    show_notes
)
from tools.memory_db_tools import (
    remember,
    recall_memory,
    show_memories
)
from tools.brightness_tools import (
    get_brightness,
    set_brightness,
    increase_brightness,
    decrease_brightness
)
from tools.volume_tools import (
    volume_up,
    volume_down,
    mute_volume,
    unmute_volume
)
from tools.clipboard_tools import (
    read_clipboard,
    copy_to_clipboard,
    clear_clipboard,
    get_clipboard_history
)
from tools.task_tools import (
    create_task,
    show_tasks,
    mark_task_complete
)
from tools.window_tools import (
    minimize_window,
    maximize_window,
    activate_window,
    close_active_window
)
from tools.media_tools import (
    play_pause,
    next_track,
    previous_track
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
"minimize_window": {
    "function": minimize_window,
    "description": "Minimize a window",
    "parameters": ["window_name"]
},

"maximize_window": {
    "function": maximize_window,
    "description": "Maximize a window",
    "parameters": ["window_name"]
},

"activate_window": {
    "function": activate_window,
    "description": "Switch focus to an already open window",
    "parameters": ["window_name"]
},

"close_active_window": {
    "function": close_active_window,
    "description": "Close current active window",
    "parameters": []
},
"read_clipboard": {
    "function": read_clipboard,
    "description": "Read current clipboard text",
    "parameters": []
},

"copy_to_clipboard": {
    "function": copy_to_clipboard,
    "description": "Copy text to clipboard",
    "parameters": ["text"]
},

"clear_clipboard": {
    "function": clear_clipboard,
    "description": "Clear clipboard",
    "parameters": []
},

"get_clipboard_history": {
    "function": get_clipboard_history,
    "description": "Show clipboard history",
    "parameters": []
},

"volume_up": {
    "function": volume_up,
    "description": "Increase volume",
    "parameters": []
},

"volume_down": {
    "function": volume_down,
    "description": "Decrease volume",
    "parameters": []
},

"mute_volume": {
    "function": mute_volume,
    "description": "Mute system volume",
    "parameters": []
},

"unmute_volume": {
    "function": unmute_volume,
    "description": "Unmute system volume",
    "parameters": []
},
"get_brightness": {
    "function": get_brightness,
    "description": "Get current screen brightness",
    "parameters": []
},

"set_brightness": {
    "function": set_brightness,
    "description": "Set brightness percentage",
    "parameters": ["percent"]
},

"increase_brightness": {
    "function": increase_brightness,
    "description": "Increase screen brightness",
    "parameters": []
},

"decrease_brightness": {
    "function": decrease_brightness,
    "description": "Decrease screen brightness",
    "parameters": []
},
"play_pause": {
    "function": play_pause,
    "description": "Play or pause media",
    "parameters": []
},

"next_track": {
    "function": next_track,
    "description": "Play next song",
    "parameters": []
},

"previous_track": {
    "function": previous_track,
    "description": "Play previous song",
    "parameters": []
},
"remember": {
    "function": remember,
    "description": "Store information in long term memory",
    "parameters": ["key", "value"]
},

"recall_memory": {
    "function": recall_memory,
    "description": "Recall information from memory",
    "parameters": ["key"]
},

"show_memories": {
    "function": show_memories,
    "description": "Show all stored memories",
    "parameters": []
},
"add_note": {
    "function": add_note,
    "description": "Save a note to the notes database",
    "parameters": ["note"]
},

"show_notes": {
    "function": show_notes,
    "description": "Show all saved notes",
    "parameters": []
},
"create_task": {
    "function": create_task,
    "description": "Create a new task",
    "parameters": ["task"]
},

"show_tasks": {
    "function": show_tasks,
    "description": "Show all tasks",
    "parameters": []
},

"mark_task_complete": {
    "function": mark_task_complete,
    "description": "Mark a task as completed",
    "parameters": ["task"]
},
"set_preference": {
    "function": set_preference,
    "description": "Save a user preference",
    "parameters": ["key", "value"]
},

"get_preference": {
    "function": get_preference,
    "description": "Get a user preference",
    "parameters": ["key"]
},

"delete_preference": {
    "function": delete_preference,
    "description": "Delete a user preference",
    "parameters": ["key"]
},
"web_search": {
    "function": web_search,
    "description": "Search the web using Exa AI",
    "parameters": ["query"]
},
"create_excel": {
    "function": create_excel,
    "description": "Create Excel file from context results",
    "parameters": ["filename"]
},
"get_last_generated_file": {
    "function": get_last_generated_file,
    "description": "Get last generated file path",
    "parameters": []
},
"email_last_file": {
    "function": email_last_file,
    "description": "Email the last generated file",
    "parameters": ["recipient"]
}


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
{
    "tool":"search_web",
    "parameters":{
      "query":"machine learning internships"
    }
  },
  {
    "tool":"create_excel",
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