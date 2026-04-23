import requests

def get_all_pages(url, headers):
    results = []

    while url:
        res = requests.get(url, headers=headers)
        res.raise_for_status()

        results.extend(res.json())

        link = res.headers.get("Link", "")

        next_url = None
        if 'rel="next"' in link:
            parts = link.split(",")
            for part in parts:
                if 'rel="next"' in part:
                    next_url = part[part.find("<")+1:part.find(">")]
                    break

        url = next_url

    return results