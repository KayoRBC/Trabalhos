# importando bibliotecas
from bs4 import BeautifulSoup

import requests

# links para a ler os textos
links = [
        "https://en.wikipedia.org/wiki/Natural_language_processing",
        "https://www.ibm.com/cloud/learn/natural-language-processing",
        "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP",
        "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html",
        "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/"
        ]

# lista para armazenar os resultados
lista = []

for link in links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # obtendo paragrados
    paragrafos = soup.find_all(['p'])

    # inserindo na lista
    for i in range(0, len(paragrafos)):
        lista.append(paragrafos[i].get_text())

# mostrando lista
for i in range(0, len(lista)):
    print(lista[i])