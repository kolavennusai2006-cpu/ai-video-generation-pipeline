import requests
from config import PEXELS_API_KEY

def fetch_image(query, output_path):
    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": 1
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if "photos" not in data or len(data["photos"]) == 0:
        print("No image found.")
        return

    image_url = data["photos"][0]["src"]["original"]

    img_data = requests.get(image_url).content
    with open(output_path, "wb") as f:
        f.write(img_data)
