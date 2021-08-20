"""
EXPLICAÇÃO

    Uma fila é uma estrutura de dados que suporta 2 operações
    basicas: enfileirar e desenfileirar.

    A idéia é que novos elementos são enfileirados "no fim" da fila,
    e os elementos removidos são desenfileirados do finaç da fila.

    Basicamente é uma fila de supermercado. Quem entra, entra
    "no fim" da fila. Quem sai, sai "da frente" da fila.

    Ou seja: quem entrou primeiro sai primeiro. Em inglês,
    diriamos First In First Out, ou FIFO.

    Para implementar a idéia de filas em python, usamos uma lista.
    Para criar uma lista vazia, fazemos: lista = []
    Para a operação "retirar" um elemento, fazemos: elemento = lista.pop(0)
    Para adicionar um elemento, fazemos: lista.append(elemento)
    Para verificar quantos elementos tem na fila, é só fazer: len(fila).
    Para ver qual é o primeiro elemento sem retirá-lo, usamos elemento=fila[0]

    EXEMPLO: Veja o exemplo a seguir

    fila = []           # Começamos com uma fila vazia
    fila.append(1)      # fila = [1]
    fila.append(2)      # fila = [1, 2]
    fila.append(3)      # fila = [1, 2, 3]
    fila.pop(0)         # fila = [2, 3]         saiu o 1
    fila.append(4)      # fila = [2, 3, 4]
    fila.pop(0)         # fila = [3, 4]         saiu o 3
"""

"""
EXERCICIO 1
    Considere que a função abaixo recebe como entrada uma fila
    e um elemento que será inserido na fila.
    Implemente a funcao enfileirar(fila, elemento)
    que adiciona o elemento ao final da fila
"""


def enfileirar(fila, elemento):
    fila.append(elemento)
    return fila


"""
EXERCICIO 2
    Faca a funcao 'desenfileirar(fila)' que tira o elemento do inicio
    da fila e retorna esse elemento.

    Ou seja:
    fila = [10, 2, 3]
    desenfileirar(fila)    # retorna 10, e a fila fica com os elementos [2, 3]
"""


def desenfileirar(fila):
    elemento = fila.pop(0)
    return elemento


"""
EXERCICIO 3
    Implemente a função 'tamanho(fila)', que recebe uma fila e retorna a
    quantidade de elementos contidos nessa fila.
"""


def tamanho(fila):
    tamanho = len(fila)
    return tamanho


"""
EXERCICIO 4
    Usando o tamanho, podemos definir uma funcao 'fila_vazia'
    que diz se a fila está vazia ou não.
    Ela retorna True se a fila estiver vazia, False caso contrário
"""


def fila_vazia(fila):
    tamanho = len(fila)
    if tamanho > 0:
        return False
    else:
        return True


"""
EXERCICIO 5
    Implemente a função 'primeiro(fila)', que retorna o primeiro elemento
    da fila sem retirá-lo da fila.
"""


def primeiro(fila):
    primeiro = fila[0]
    return primeiro


"""
EXERCICIO 6
    faça uma funcao vira_1(fila) que recebe uma fila, retira o primeiro
    elemento do começo da fila e coloca ele de volta, no fim da fila

    Ex:
    fila = [1, 2, 3, 4, 5]
    se fizermos vira_1(fila), a fila passa a ser [2, 3, 4, 5, 1]

    DICA: Utilize as funçoes enfileirar e desenfileirar já implementadas
"""


def vira_1(fila):
    primeiro = fila[0]
    fila.append(primeiro)
    fila.pop(0)
    return fila


"""
EXERCÍCIO 7

    Faça uma funcao fila_inicial(n) que recebe um numero n
    e retorna uma fila [1, 2, 3, ..., n] (ou seja, uma fila
    dos numeros de 1 até n.
"""


def fila_inicial(n):
    fila = []
    i = 1
    while i <= n:
        fila.append(i)
        i = i + 1
    return fila
