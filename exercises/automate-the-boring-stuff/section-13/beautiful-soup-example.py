import bs4
import requests

# Amazon blocks non-browser requests, so this does not work
res = requests.get("https://store.steampowered.com")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")  # html.parser is to avoid warning

elements = soup.select(
    "#tab_newreleases_content > a:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)"
)
elements[0].text.strip()
