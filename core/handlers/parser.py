import requests
from bs4 import BeautifulSoup as Bs

final_sp = []


def main():
    global final_sp
    url = 'https://vernost67.ru/news'
    main_class = 'post__text'

    try:
        req = requests.get(url)
        html = Bs(req.text, 'html.parser')
        t = html.find_all(class_=main_class)

    except Exception:
        print('Запрос не выполнен, проверьте подключение к интернету и корректность ссылки(((')
        t = []

    for el in t[:-2]:
        final_sp.append(' '.join(el.text.split()))
    return final_sp
