MENU_LINKS = [
    {
        'url': 'mainapp:index',
        'name': 'домой'
    },
    {
        'url': 'mainapp:products',
        'name': 'продукты',
        'url_products': 'mainapp:products-by-category'
    },
    {
        'url': 'mainapp:contact',
        'name': 'контакты'
    }
]

def menu_links():
    return {
        'menu_links': MENU_LINKS
    }