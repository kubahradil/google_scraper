import requests

API_KEY = "08ef0af29d735a7cb98339fbe50b2f3dc45194ebdaaf0596152f9954345603d4"

def get_google_results(query):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "hl": "cs",
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()

    results = []
    for result in data.get("organic_results", []):
        results.append({
            "title": result.get("title"),
            "link": result.get("link")
        })
    return results
