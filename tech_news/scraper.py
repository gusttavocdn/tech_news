import time
import requests
from requests.exceptions import ReadTimeout, MissingSchema


# Requisito 1
def fetch(url: str) -> (str | None):
    """Seu código deve vir aqui"""
    time.sleep(1)
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
    except (ReadTimeout, MissingSchema):
        return None
    else:
        if response.status_code != 200:
            return None
        return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
