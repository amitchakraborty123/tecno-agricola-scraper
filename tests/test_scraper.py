from bs4 import BeautifulSoup
from pathlib import Path

from scraper import extract_item


def test_extract_item():
    html = Path("tests/fixtures/sample_product.html").read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")

    article = soup.select_one("article")
    result = extract_item(article)

    assert result["Name"] == "Cesar cane - Fresh Bowls chicken - carrots - green beans and pumpkin 85 gr."
    assert result["Price"] == "€1.49"
    assert result["Image"] == "https://www.tecnoagricolamodena.it/15916-home_default/cesar-cane-natural-goodness-agnello-carote-patate-spinaci-400-gr.jpg"
    assert result["Availability"] == "Available"
