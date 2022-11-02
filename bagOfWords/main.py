# importando bibliotecas
from bs4 import BeautifulSoup

import requests

import re

# links para a ler os textos

links = [
        "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP",
         "https://aws.amazon.com/en/what-is/nlp/",
         "https://stagezero.ai/blog/what-is-natural-language-processing/",
         "https://www.algolia.com/blog/product/what-is-natural-language-processing-and-how-is-it-leveraged-by-search-tools-software/",
         "https://www.encora.com/insights/natural-language-processing-and-machine-learning"
        ]

# lista para armazenar os resultados
lista = []

for link in links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

    # obtendo paragrafos
    paragrafos = soup.find_all(['p'])

    # regex para separar as sentencas
    regex = re.compile(r'''([A-Z][ ]?([("]?[\w][")]?[,]?[ ]?[-]?[']?){20,}[.])''')

    # inserindo na lista
    for i in range(0, len(paragrafos)):
        texto = paragrafos[i].get_text()
        check = regex.finditer(texto)
        for i in check:
            lista.append(i[0])

# mostrando lista
for i in range(0, len(lista)):
    print(lista[i])
    print('------------------')


# codigo para gerar a bag of words
# lista que vai armazenar as palavras da sentenca
lista2 = []

# separando as palavras da sentenca com regex
regex = re.compile(r'''([\w][']?[-]?)+''')
for i in range(0, len(lista)):
  palavras = regex.finditer(lista[i])
  for palavra in palavras:
    lista2.append(palavra[0])

# criando conjunto de palavras (retirando as repeticoes)
conjuntoPalavras = set(lista2)

# mostrando no terminal
print(conjuntoPalavras)

# lista que vai armazenar a matriz
bagOfWords = []

# toda nova linha criada vai ser uma copia de uma lista com zeros
bagZeros = []
for n in range(0, len(conjuntoPalavras)):
  bagZeros.append(0)

# inserindo a sentenca na matriz
for i in range(0, len(lista)):

  bagOfWords.append(bagZeros.copy())

  # dividindo as palavras com regex
  palavras = regex.finditer(lista[i])
  for palavra in palavras:
    p = palavra[0]
    n = 0 # posicao lista bagOfWords
    for palavraConjunto in conjuntoPalavras:
      # caso encontre na lista bagOfWords
      if(palavraConjunto == p):
        bagOfWords[i][n] += 1
        break
      n += 1

# mostrando resultado
for i in bagOfWords:
  print(i)