import bs4
import requests


def get_price(product_url):
    res = requests.get(product_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elements = soup.select(
        "#in-stock > div.product-item-content > div.price > span.price-new.money"
    )
    # CSS element
    return elements[0].text.strip()


price = get_price("https://inoxia-rec.com/collections/cd-1")  # URL of product
print("The price is " + price)
