from exa_py import Exa
import os
from dotenv import load_dotenv
load_dotenv()

EXA_API_KEY = os.getenv(
    "EXA_API_KEY"
)

exa = Exa(EXA_API_KEY)


def search_web(query):

    result = exa.search_and_contents(
        query,
        num_results=10
    )

    print("\nEXA RESULT:")
    print(result)

    data = []

    print("\nRESULTS ATTRIBUTE:")
    print(result.results)

    for item in result.results:

        print(item)

        data.append({
            "title": item.title,
            "url": item.url
        })

    print("\nPARSED DATA:")
    print(data)

    return data