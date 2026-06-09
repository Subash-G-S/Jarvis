from services.memory_service import (
    save_memory,
    get_memory,
    delete_memory
)


def set_preference(
    key,
    value
):

    save_memory(
        category="preference",
        key=key,
        value=value
    )

    return "Preference saved."


def get_preference(key):

    value = get_memory(key)

    if value:

        return value

    return "Preference not found."


def delete_preference(key):

    return delete_memory(key)