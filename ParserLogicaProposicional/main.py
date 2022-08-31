# Kayo Renato Bortolan Cezario

# Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a
# linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional
# escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma
# da expressão (sintaxe).
# A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
# com a seguinte formatação:
# 1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões
# lógicas estão no arquivo.
# 2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
# A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída
# para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.
# Gramática:
# Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
# Constante="T"|"F".
# Proposicao=[a−z0−9]+
# FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
# FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
# AbreParen="("
# FechaParen=")"
# OperatorUnario="¬"
# OperatorBinario="∨"|"∧"|"→"|"↔"
#
# Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação,
# conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
# Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em
# qualquer expressão de entrada.
# Para  validar  seu  trabalho,  você  deve  incluir  no  repl.it,  no  mínimo  três  arquivos  contendo
# números  diferentes  de  expressões  proposicionais.  O  professor  irá  incluir  um  arquivo  de  testes  extra
# para validar seu trabalho. Para isso, caberá ao professor incluir o arquivo no seu repl.it e rodar o seu
# programa carregando o arquivo de testes.

constanteCaracteres = ["T", "F"]

proposicaoCaracteres = []
for i in range(48, 58):
    proposicaoCaracteres.append(chr(i))
for i in range(97, 123):
    proposicaoCaracteres.append(chr(i))

abreParen = "("
fechaParen = ")"

operadorUnarioCaracteres = [r"\neg"]
operadorBinarioCaracteres = ["\disj", "\conj", "\implic", r"\biImplic"]

# na formula binaria, em uma parte da composicao temos "formula formula". Esta funcao
# serve para detectar e separar essas duas formulas para verificarmos elas separadamente
# futuramente
def dividirFormulas(formulas): # retorna uma matriz com duas posicoes

    # exemplos de entrada:
    # string = "(a b (a b c d) (a b c d) d) (a b c d)"
    # string2 = "(a b c d) a"

    # retorno
    strings = ["", ""]

    # a variavel n serve para verificarmos os parenteses, caso o valor final for diferente
    # de zero a formula esta errada e retornara ["", ""]
    n = 0
    if(formulas[0] == abreParen):
        for i in range(0, len(formulas)):
            if formulas[i] == abreParen:
                n += 1
            elif formulas[i] == fechaParen:
                n -= 1
                if(n < 0):
                    return strings
                elif (n == 0):
                    for j in range(0, i + 1):
                        strings[0] += formulas[j]
                    for j in range(i + 2, len(formulas)):
                        strings[1] += formulas[j]
                    break
        # caso a variavel n termine positiva
        return strings
    else:
        strings = formulas.split(" ", 1)
    return strings

# verificando se uma string eh uma proposicao
def proposicao(string):
    for i in range(0, len(string)):
        caracter = str(string[i])
        if caracter not in proposicaoCaracteres:
            return False
    if(string == ""):
        return False
    return True


# verificando se uma string eh uma formula unaria
def formulaUnaria(string):
    strings = string.split(" ", 2)
    if (strings[0] == abreParen and strings[2][len(strings[2]) - 1] == fechaParen):
        if (strings[1] in operadorUnarioCaracteres):
            if(formula(strings[2][:-2])):
                return True
    return False

# verificando se uma string eh uma formula binaria
def formulaBinaria(string):
    strings = string.split(" ", 2)
    if (strings[0] == abreParen and strings[2][len(strings[2]) - 1] == fechaParen):
        if (strings[1] in operadorBinarioCaracteres):
            formulas = dividirFormulas(strings[2][:-2])
            if(formula(formulas[0]) and formula(formulas[1])):
                return True
    return False

# verificando se uma string eh uma formula
def formula(string):
    if (string in constanteCaracteres or proposicao(string) or formulaUnaria(string) or formulaBinaria(string)):
        return True
    else:
        return False

# exemplo: "( \neg ( \disj ( \biImplic ( \neg T ) ( \neg T ) ) ( \neg T ) ) )"

nomeArquivo = ""

while(True):
    nomeArquivo = input("Digite o nome do arquivo (Exemplo: arquivo1.txt): ")
    try:
        with open(nomeArquivo, "r") as arquivo:
            linhas = arquivo.read().split("\n")
        break
    except:
        print("Nome de arquivo invalido! Digite novamente")

for i in range(1, int(linhas[0]) + 1):
    if(formula(linhas[i])):
        print(linhas[i] + ": valida")
    else:
        print(linhas[i] + ": invalida")