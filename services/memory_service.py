from database.db import SessionLocal
from database.models import Memory


def save_memory(
    category,
    key,
    value
):

    session = SessionLocal()

    memory = session.query(
        Memory
    ).filter_by(
        key=key
    ).first()

    if memory:

        memory.value = value

        memory.category = category

    else:

        memory = Memory(
            category=category,
            key=key,
            value=value
        )

        session.add(memory)

    session.commit()

    session.close()

    return "Memory saved."

def get_memory(key):

    session = SessionLocal()

    memory = session.query(
        Memory
    ).filter_by(
        key=key
    ).first()

    session.close()

    if memory:

        return memory.value

    return None


def get_all_memories():

    session = SessionLocal()

    memories = session.query(
        Memory
    ).all()

    session.close()

    return [

        {
            "category": m.category,
            "key": m.key,
            "value": m.value
        }

        for m in memories
    ]
def delete_memory(key):

    session = SessionLocal()

    memory = session.query(
        Memory
    ).filter_by(
        key=key
    ).first()

    if not memory:

        session.close()

        return "Memory not found."

    session.delete(memory)

    session.commit()

    session.close()

    return "Memory deleted."