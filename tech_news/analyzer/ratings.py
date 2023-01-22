from collections import Counter
from tech_news.database import find_news

# Requisito 10


def top_5_news():
    news_list = find_news()
    sorted_news = sorted(
        news_list,
        key=lambda x: (x["comments_count"], x["title"]),
        reverse=True,
    )
    return [(new["title"], new["url"]) for new in sorted_news][:5]


# Requisito 11
def top_5_categories():
    news_list = find_news()

    categories = sorted([news["category"] for news in news_list])
    top_5_common_categories = Counter(categories).most_common()[:5]
    return [category[0] for category in top_5_common_categories]
