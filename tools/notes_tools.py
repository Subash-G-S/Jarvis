from services.memory_service import (
    save_memory,
    get_all_memories
)

import uuid


def add_note(note):

    note_id = str(
        uuid.uuid4()
    )[:8]

    save_memory(
        category="note",
        key=f"note_{note_id}",
        value=note
    )

    return "Note saved."


def show_notes():

    memories = get_all_memories()

    notes = []

    for memory in memories:

        if memory["category"] == "note":

            notes.append(
                memory["value"]
            )

    if not notes:

        return "No notes found."

    result = ""

    for i, note in enumerate(
        notes,
        start=1
    ):

        result += (
            f"{i}. {note}\n"
        )

    return result