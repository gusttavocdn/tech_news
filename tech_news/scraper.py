import time
import requests
from requests.exceptions import ReadTimeout, MissingSchema
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url: str):
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
    soup = BeautifulSoup(html_content, "html.parser")
    links = [
        anchor["href"]
        for anchor in soup.find_all("a", {"class": "cs-overlay-link"})
    ]
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page_link = soup.find("a", {"class": "next page-numbers"})
    return next_page_link["href"] if next_page_link else None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    news = {
        "title": soup.find("h1", {"class": "entry-title"}).get_text(
            strip=True
        ),
        "url": soup.find("link", {"rel": "canonical"})["href"],
        "timestamp": soup.find("li", {"class": "meta-date"}).string,
        "writer": soup.find("li", {"class": "meta-author"})
        .find("span", {"class": "author"})
        .a.string,
        "summary": soup.find("div", {"class": "entry-content"}).find("p").text,
        "tags": [tag.string for tag in soup.find_all("a", {"rel": "tag"})],
        "category": soup.find("a", {"class": "category-style"})
        .find("span", {"class": "label"})
        .string,
        "comments_count": 0,
    }

    final_char = news["summary"][-1]

    if final_char not in ".?!”":
        last_dot_index = news["summary"].rfind(".")
        news["summary"] = news["summary"][: last_dot_index + 1]

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
