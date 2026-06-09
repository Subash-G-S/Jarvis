from agent.llm import ask_llm
from agent.tool_manager import (
    get_available_tools
)
tools = get_available_tools()
def create_plan(user_request):

    prompt = f"""
You are an AI planning agent.

Available tools:

{tools}

Return ONLY JSON.
IMPORTANT:

Return ONLY valid JSON.

Do NOT explain.

Do NOT add markdown.

Do NOT add code fences.

Do NOT add any text before or after JSON.

Return ONLY a JSON array.

IMPORTANT:

If the user specifies:

- file names
- search queries
- dates
- locations
- limits
- filters

extract them and include them in parameters.

Examples:
User:
Find software developer internships
and send it to my email

Output:

[
  {{
    "tool":"web_search",
    "parameters":{{
      "query":"software developer internships"
    }}
  }},
  {{
    "tool":"create_excel",
    "parameters":{{}}
  }},
  {{
    "tool":"email_last_file",
    "parameters":{{}}
  }}
]
User:
Send the report to my email

Output:

[
  {{
    "tool":"email_last_file",
    "parameters":{{}}
  }}
]

User:
Find machine learning internships
and save as ml_jobs.xlsx

Output:

[
  {{
    "tool":"web_search",
    "parameters":{{
      "query":"machine learning internships"
    }}
  }},
  {{
    "tool":"create_excel",
    "parameters":{{
      "filename":"ml_jobs.xlsx"
    }}
  }}
  {{
    "tool":"email_last_file",
    "parameters":{{}}
  }}
]

User Request:
{user_request}
"""

    return ask_llm(prompt)