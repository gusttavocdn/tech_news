from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)


def menu_add_news_to_db():
    try:
        amount = int(input("Digite quantas notícias serão buscadas: "))
    except ValueError:
        print("Quantidade inválida")
        return
    else:
        return get_tech_news(amount)


def menu_search_by_title():
    title = input("Digite o título:")
    return search_by_title(title)


def menu_search_by_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(date)


def menu_search_by_category():
    category = input("Digite a categoria:")
    return search_by_category(category)


def menu_search_by_tag():
    tag = input("Digite a tag:")
    return search_by_tag(tag)


def menu_exit():
    print("Encerrando script")
