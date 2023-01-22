from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 7
def search_by_date(date):
    try:
        formatted_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news_list = search_news({"timestamp": {"$eq": formatted_date}})
        return [(news["title"], news["url"]) for news in news_list]


# Requisito 8
def search_by_tag(tag):
    news_list = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 9
def search_by_category(category):
    news_list = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return [(news["title"], news["url"]) for news in news_list]
