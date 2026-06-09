from openpyxl import Workbook
import os
from agent.context import context
from services.file_memory import (
    set_last_file
)
from datetime import datetime


def create_excel(
    
    filename=(f"report_"
        f"{datetime.now():%Y%m%d_%H%M%S}"
        ".xlsx")
):

    results = context.get(
        "web_search"
    )
    print(
        "CONTEXT DATA:",
        results
    )
    if not results:

        return "No search results found."

    wb = Workbook()

    ws = wb.active

    ws.title = "Results"

    ws.append([
        "Title",
        "URL"
    ])

    for item in results:

        if isinstance(item, dict):

            ws.append([
                item.get(
                    "title",
                    ""
                ),
                item.get(
                    "url",
                    ""
                )
            ])

    from services.output_manager import (
        get_output_path
    )

    filepath = get_output_path(
        filename
    )

    wb.save(filepath)
    set_last_file(
    filepath
)
    print(
        "Excel saved at:",
        os.path.abspath(filename)
    )   

    return f"Excel saved as {filename}"