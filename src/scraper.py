"""
Tecno Agricola Product Scraper

A web scraping tool that extracts product data (name, price, image,
availability, and links) from https://www.tecnoagricolamodena.it/.

Features:
- Scrapes all categories or a single category
- Handles pagination automatically
- Retries failed requests
- Logs activity to logs/scraper.log
- Saves output into CSV file

Author: Amit Chakravarti
"""

import logging
import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import BASE_URL, OUTPUT_FILE, RESULTS_PER_PAGE
from utils import build_session, text, attr

# ---------- Logging Configuration ----------
os.makedirs("../logs", exist_ok=True)
logging.basicConfig(
    filename="../logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
log = logging.getLogger(__name__)


# ---------- URL Collection ----------
def collect_urls(session: requests.Session) -> list[str]:
    """Ask the user which categories to scrape and return a list of categories URLs."""
    print("What do you want to scrape?\n  1. All Categories\n  2. Single Category")
    choice = input("Enter number and press Enter: ").strip()

    if choice == "1":
        resp = session.get(BASE_URL, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "lxml")
        nav = soup.select_one("ul.cbp-hrsub-tabs-names")
        if not nav:
            log.error("Category nav not found — page structure may have changed.")
            return []
        urls = [a["href"] for a in nav.select("a.nav-link") if a.get("href")]
    elif choice == "2":
        url = input("Paste the category URL and press Enter: ").strip()
        urls = [url] if url else []
    else:
        log.error("Invalid menu choice: %s", choice)
        urls = []

    log.info("Total category URLs collected: %d", len(urls))
    print(f"---> {len(urls)} URL(s) collected.")
    return urls


# ---------- Items Extraction ----------
def extract_item(article) -> dict:
    """Extract product data & return in a dict"""
    link = attr(article, "h2.product-title a", "href")
    name = text(article, "h2.product-title")
    price = text(article, "span.product-price")
    img = attr(article, "div.thumbnail-container img", "data-src")

    if article.select_one("button[data-button-action='add-to-cart']"):
        availability = "Available"
    else:
        vedi = article.select_one("a.btn-product-list")
        availability = (
            "Not available" if vedi and vedi.get_text(strip=True) == "Vedi" else ""
        )

    return {
        "Link": link,
        "Name": name,
        "Price": price,
        "Image": img,
        "Availability": availability,
    }


# ---------- Core scraping logic ----------
def scrape(session: requests.Session, urls: list[str]) -> None:
    """Iterate over every category URL, page by page, and write results to CSV."""
    log.info("--- SCRAPING STARTED ---")
    print("--- Scraping started ---")

    first_write = not os.path.exists(OUTPUT_FILE)

    for url in urls:
        log.info("Category: %s", url)
        page = 0

        while True:
            page += 1
            page_url = f"{url}?resultsPerPage={RESULTS_PER_PAGE}&page={page}"

            try:
                resp = session.get(page_url, timeout=15)
                resp.raise_for_status()
            except requests.RequestException as exc:
                log.error("Request failed for %s: %s", page_url, exc)
                break

            soup = BeautifulSoup(resp.content, "lxml")

            product_list = soup.select_one("div#js-product-list")
            articles = (
                product_list.select("article.product-miniature") if product_list else []
            )

            log.info("Page %d | Items found: %d", page, len(articles))
            print(f"- Page {page} | {len(articles)} items")

            if not articles:
                break

            # --- Collect the whole page content & write them once ---
            rows = [extract_item(a) for a in articles]
            df = pd.DataFrame(rows)
            df.to_csv(
                OUTPUT_FILE,
                mode="a",
                header=first_write,
                encoding="utf-8-sig",
                index=False,
            )
            first_write = False

            time.sleep(0.5)

    log.info("--- SCRAPING COMPLETE ---")
    print("--- All data scraped successfully ---")


# ---------- Entry Point ----------
def main() -> None:
    session = build_session()
    urls = collect_urls(session)
    if not urls:
        print("No URLs to scrape. Exiting...")
        return
    scrape(session, urls)


if __name__ == "__main__":
    main()
