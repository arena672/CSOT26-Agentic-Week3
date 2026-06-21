import requests


def paper_search(query):

    try:

        url = "https://huggingface.co/api/papers/search"

        response = requests.get(
            url,
            params={"q": query}
        )

        response.raise_for_status()

        papers = response.json()

        results = []

        for paper in papers[:5]:

            results.append(
                {
                    "title": paper.get("title"),
                    "arxiv_id": paper.get("id")
                }
            )

        return {
            "papers": results
        }

    except Exception as e:

        return {
            "error": str(e)
        }

def read_paper(arxiv_id):

    try:

        url = f"https://huggingface.co/papers/{arxiv_id}.md"

        response = requests.get(url)

        response.raise_for_status()

        return {
            "content": response.text
        }

    except Exception as e:

        return {
            "error": str(e)
        }