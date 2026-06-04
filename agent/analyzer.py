from ollama import chat


def analyze_result(user_query, tool_result):

    prompt = f"""
User Question:
{user_query}

Tool Result:
{tool_result}

Answer the user's question naturally.
Do not mention tools.
Be concise and helpful.
"""

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]