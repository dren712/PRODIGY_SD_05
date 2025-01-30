import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

# URL of the e-commerce website (example: a random page from books.toscrape.com)
url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"

# Send a GET request to fetch the webpage content
response = requests.get(url)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product containers
product_containers = soup.find_all('article', class_='product_pod')

# Lists to hold scraped data
product_names = []
product_prices = []
product_links = []

# Loop through the products to extract details
for product in product_containers:
    # Extract the product name (title of the book)
    name = product.find('h3').find('a')['title']
    product_names.append(name)
    
    # Extract the price of the book
    price = product.find('p', class_='price_color').text
    product_prices.append(price)
    
    # Extract the product link
    link = product.find('h3').find('a')['href']
    product_links.append(f"https://books.toscrape.com/catalogue{link.replace('../../..', '')}")

# Create a DataFrame to store the scraped data
data = {
    "Product Name": product_names,
    "Price": product_prices,
    "Link": product_links
}

df = pd.DataFrame(data)

# Output the scraped data to a CSV file
df.to_csv(f"scraped_products_{random.randint(1, 1000)}.csv", index=False)

# Print a sample of the scraped data
print(df.head())
