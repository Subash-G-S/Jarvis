from services.memory_service import (
    save_memory,
    get_memory,
    get_all_memories
)

save_memory(
    "preferred_browser",
    "chrome"
)

print(
    get_memory(
        "preferred_browser"
    )
)

print(
    get_all_memories()
)