import sys

from tech_news.analyzer.ratings import top_5_categories, top_5_news
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


# Requisito 12
def analyzer_menu():

    option = input(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )
    try:
        option = int(option)
    except ValueError:
        print("Opção inválida", file=sys.stderr)
        return

    if option not in range(8):
        print("Opção inválida", file=sys.stderr)
        return

    menu_functions = {
        0: menu_add_news_to_db,
        1: menu_search_by_title,
        2: menu_search_by_date,
        3: menu_search_by_tag,
        4: menu_search_by_category,
        5: top_5_news,
        6: top_5_categories,
        7: menu_exit,
    }

    return menu_functions[option]()
