from services.memory_service import (
    save_memory,
    get_memory,
    get_all_memories
)


def remember(key, value):

    save_memory(
        key,
        value
    )

    return f"Remembered {key}"


def recall_memory(key):

    value = get_memory(key)

    if value:

        return value

    return "I don't know that yet."


def show_memories():

    memories = get_all_memories()

    if not memories:

        return "No memories stored."

    result = ""

    for memory in memories:

        result += (
            f"{memory['key']} : "
            f"{memory['value']}\n"
        )

    return result