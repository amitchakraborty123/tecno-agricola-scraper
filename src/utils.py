import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import HEADERS


# ---------- HTTP Session Configuration ----------
def build_session() -> requests.Session:
    """Return a Session with automatic retries on transient errors."""
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update(HEADERS)
    return session


# ---------- Items Extraction ----------
def text(tag, selector: str, default: str = "") -> str:
    """Return text from the element"""
    el = tag.select_one(selector)
    return el.get_text(strip=True) if el else default


def attr(tag, selector: str, attribute: str, default: str = "") -> str:
    """Return attribute from the element"""
    el = tag.select_one(selector)
    return el.get(attribute, default) if el else default
