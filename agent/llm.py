# agent/llm.py

from ollama import chat

from agent.tool_registry import generate_tool_prompt


def ask_llm(user_input):

    system_prompt = generate_tool_prompt()

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response["message"]["content"]