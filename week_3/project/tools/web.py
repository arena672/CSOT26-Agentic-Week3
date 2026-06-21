"""
Web search and fetch tools
"""

import os
import requests
import trafilatura
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")


def web_search(query: str):
    """
    Search the web using Serper API.
    Returns top search results.
    """

    try:
        url = "https://google.serper.dev/search"

        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.post(
            url,
            headers=headers,
            json={"q": query}
        )

        data = response.json()

        results = []

        for item in data.get("organic", [])[:5]:
            results.append({
                "title": item["title"],
                "link": item["link"],
                "snippet": item["snippet"]
            })

        return {"results": results}

    except Exception as e:
        return {"error": str(e)}


def web_fetch(url: str):
    """
    Fetch webpage and extract clean text.
    """

    try:
        response = requests.get(url, timeout=10)

        text = trafilatura.extract(response.text)

        return {
            "content": text
        }

    except Exception as e:
        return {"error": str(e)}
