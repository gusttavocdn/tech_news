from requests.exceptions import ReadTimeout, MissingSchema
from tech_news.database import create_news
from bs4 import BeautifulSoup
from math import ceil

import requests
import time

BASE_URL = "https://blog.betrybe.com/"


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
        "summary": remove_html_tags(
            soup.find("div", {"class": "entry-content"}).find("p").text
        ).strip(),
        "tags": [tag.string for tag in soup.find_all("a", {"rel": "tag"})],
        "category": soup.find("a", {"class": "category-style"})
        .find("span", {"class": "label"})
        .string,
        "comments_count": 0,
    }

    return news


# https://medium.com/@jorlugaqui/how-to-strip-html-tags-from-a-string-in-python-7cb81a2bbf44
def remove_html_tags(text):
    """Remove html tags from a string"""
    import re

    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


# Requisito 5
def get_tech_news(amount):
    necessary_pages = ceil(amount / 12)
    pages_links = get_pages_links(necessary_pages)
    tech_news_list = fetch_tech_news(pages_links, amount)

    create_news(tech_news_list)

    return tech_news_list


def fetch_tech_news(pages_links, amount):
    list = []
    for page in pages_links:
        html_content = fetch(page)
        news_links = scrape_updates(html_content)

        for link in news_links:
            if len(list) == amount:
                return list
            html_content = fetch(link)
            list.append(scrape_news(html_content))
    return list


def get_pages_links(amount):
    next_page = scrape_next_page_link(fetch(BASE_URL))

    pages_links = [BASE_URL]

    for _ in range(1, amount):
        pages_links.append(next_page)
        next_page = scrape_next_page_link(fetch(next_page))

    return pages_links
