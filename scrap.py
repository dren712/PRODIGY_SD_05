import pandas as pd
from scrapingbee import ScrapingBeeClient

# Initialize the client with your API Key
client = ScrapingBeeClient(api_key='YOUR-API-KEY')

# Send request with specific parameters to scrape data
response = client.get(
    "https://books.toscrape.com/catalogue/category/books/classics_6/index.html",
    params={
        'extract_rules': {
            # Extract name/title of the book
            "name": {
                "selector": "div.image_container > a > img",
                "output": "@alt",
                "type": "list"
            },
            # Extract the link of the book
            "link": {
                "selector": "div.image_container > a",
                "output": "@href",
                "type": "list"
            },
            # Extract the price of the book
            "price": {
                "selector": "p.price_color",
                "type": "list"
            },
            # Extract stock availability of the book
            "availability": {
                "selector": "p.instock.availability",
                "clean": True,
                "type": "list"
            },
            # Extract the image URL of the book
            "image": {
                "selector": "img.thumbnail",
                "output": "@src",
                "type": "list"
            }
        }
    }
)

# Print the content of the response
if response.ok:
    print(response.content)
