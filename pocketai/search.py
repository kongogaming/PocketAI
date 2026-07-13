from rich.text import Text


def search_current(history, query):
    query = query.lower()

    results = []

    for index, message in enumerate(history, start=1):

        content = message["content"]

        if query in content.lower():

            results.append({
                "number": index,
                "role": message["role"].capitalize(),
                "content": content,
            })

    return results