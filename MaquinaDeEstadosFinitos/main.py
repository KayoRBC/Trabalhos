# Kayo Renato Bortolan Cezario

# Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá
# criar  um  programa,  utilizando  a linguagem  Python, C, ou C++.  
# Este  programa,  quando  executado,  irá  determinar  se  uma  
# string de entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 
# = {𝑥 | 𝑥 ∈ {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo 
# o alfabeto  Σ={𝑎,𝑏,𝑐}. O  programa  que  você  desenvolverá  irá  
# receber  como  entrada um arquivo de texto  (.txt) contendo várias 
# strings. A primeira linha do arquivo indica quantas strings estão 
# no arquivo de texto de entrada. As linhas subsequentes contém uma 
# string por linha.  A seguir está um exemplo das linhas que podem 
# existir em um arquivo de testes para o programa que você irá 
# desenvolver: 
# 3 
# abbaba 
# abababb 
# bbabbaaab 
# Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  
# strings em  cada  arquivo  será representado  por  um  número  
# inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  
# uma, e somente uma linha de saída para cada string. Estas linhas 
# conterão a string de entrada e o resultado da validação conforme o 
# formato indicado a seguir: 
# abbaba: não pertence.   
# A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  
# para  o  terminal  padrão  e  será composta de uma linha de saída 
# por string de entrada. No caso do exemplo, teremos 3 linhas de 
# saída. Para que seu programa possa ser testado você deve criar, no 
# mínimo, três arquivos de entrada contendo um número diferente de 
# strings diferentes. Os arquivos de entrada criados para os seus 
# testes devem estar disponíveis tanto no ambiente repl.it quanto no 
# ambiente Github. Observe que o professor irá  testar  seu  programa 
# com  os  arquivos  de  testes  que  você  criar  e  com,  no  
# mínimo  um  arquivo  de testes criado pelo próprio professor.  

# verifica se uma palavra eh valida ou nao
def verificar(palavra):
  alfabeto = ['a', 'b', 'c']
  # verificando cada caracter da palavra
  for i in range(0, len(palavra)):
    letra = palavra[i]
    # caso seja 'a' e tenha pelo menos 2 caracteres seguintes
    if(letra == alfabeto[0] and i < len(palavra)-2):
      # verificando os 2 caracteres seguintes
      for j in range(i + 1, i + 3):
        letra = palavra[j]
        i = j
        if(letra != alfabeto[1]):
          return False
    # caso nao esteja no alfabeto
    elif(letra not in alfabeto):
      return False
    # caso nao tenha 2 caractes seguintes e seja 'a'
    elif(letra == alfabeto[0]):
      return False
  # se tudo certo
  return True


# ler arquivo e verificar se as strings sao validas
def ler_arquivo(nome):
  with open(nome, 'r') as arquivo:
    linhas = arquivo.read()
    strings = linhas.split()
    print(f"Arquivo: {nome}")
    print(f"Quantidade de strings: {strings[0]}")
    for n in range(1, len(strings)):
      if verificar(strings[n]):      
        print(strings[n], ": pertence")
      else:
        print(strings[n], ": nao pertence")

# testando
ler_arquivo('strings1.txt')
print('-' * 20)
ler_arquivo('strings2.txt')
print('-' * 20)
ler_arquivo('strings3.txt')