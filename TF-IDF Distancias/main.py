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

# codigo TF-IDF

TF = []
# percorrendo cada linha do bagOfWords
for documento in bagOfWords:
  # lista nova (linha)
  lista = []

  # quantidade de palavras na frase (linha)
  quantidadeDePalavrasNaFrase = sum(documento)

  # percorrendo cada coluna da linha (que ja possui a quantidade de vezes que a palavra aparece na frase)
  for palavra in documento:
    # calculado TF
    calculo = palavra/quantidadeDePalavrasNaFrase
    # colocando na lista
    lista.append(calculo)
  # colocando na TF
  TF.append(lista)

for n in TF:
  print(n)

import math

IDF = []

for n in range(0, len(TF[0])): # o len de TF[0] é igual a quantidade de palavras do dicionario
  # contando a quantidade de documentos que aparece o termo
  quantidadeOcorrencias = 0
  for documento in bagOfWords:
    if documento[n] > 0:
      quantidadeOcorrencias += 1
  # calculando IDF
  calculo = math.log(len(TF)/quantidadeOcorrencias)
  IDF.append(calculo)

print(IDF)

# Sua tarefa será gerar a matriz termo-documento usando TF-IDF por meio da aplicação das
# fórmulas  TF-IDF  na  matriz  termo-documento  criada  com  a  utilização  do  algoritmo  Bag of
# Words. Sobre o Corpus que recuperamos anteriormente. O entregável desta tarefa é uma
# matriz termo-documento onde a primeira linha são os termos e as linhas subsequentes são
# os vetores calculados com o TF-IDF.

TFIDF = []

for documentoTF in TF:
  lista = []
  for n in range(0, len(documentoTF)):
    calculo = documentoTF[n] * IDF[n]
    lista.append(calculo)
  TFIDF.append(lista)

# for n in TFIDF:
#  print(n)

resposta = []
resposta.append(conjuntoPalavras)
for n in TFIDF:
  resposta.append(n)

# mostrando resposta
for n in resposta:
  print(n)

# Sua tarefa será gerar uma matriz de distância, computando o cosseno do ângulo entre todos
# os vetores que encontramos usando o tf-idf.

import numpy as np

# matriz de distancias
distancias = []

# calculando a distancia entre cada par
for n1 in range(1, len(TFIDF)):
    distanciasN1 = []
    for n2 in range(1, len(TFIDF)):
        a = TFIDF[n1]
        b = TFIDF[n2]

        cos_sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
        distanciasN1.append(cos_sim)
    distancias.append(distanciasN1)

for n in distancias:
    print(n)