"""
EXPLICACAO
    Uma pilha é uma estrutura de dados que tem um "topo".

    Ela armazena quantos elementos quisermos, mas só podemos retirar
    o elemento do topo.
    Quando adicionamos um elemento, só podemos adicionar no topo.

    Em inglês, diriamos Last In First Out, ou LIFO.

    Em uma pilha a operação "colocar no topo" é chamada de "push",
    e a operação "tirar do topo" é chamada de "pop".

    Em python, podemos implementar o conceito de pilha usando uma lista,
    que têm as funções append e pop

    EXEMPLO:

    pilha = []          # começamos com uma pilha vazia
    pilha.append(5)     # pilha: [5]
    pilha.append(8)     # pilha: [5, 8]
    pilha.append(4)     # pilha: [5, 8, 4]
    pilha.append(3)     # pilha: [5, 8, 4, 3]
    item = pilha.pop()  # pilha: [5, 8, 4]          desempilhou o 3
    item = pilha.pop()  # pilha: [5, 8]             desempilhou o 4
"""

"""
EXERCICIO 1
    Crie a função empilhar, que recebe uma pilha e um elemento
    e coloca o elemento no topo da pilha
"""


def empilhar(pilha, elemento):
    pilha.append(elemento)
    return pilha


"""
EXERCICIO 2
    Crie a função desempilhar, que recebe uma pilha, tira o elemento
    que estava no topo da pilha e retorna ele

    Exemplo:
    Se a pilha era [1, 2, 3], a pilha deve ficar sendo [1, 2] e a função
    deve retornar 3
"""


def desempilhar(pilha):
    ultimoInd = len(pilha) - 1
    ultimo = pilha.pop(ultimoInd)
    return ultimo


"""
EXERCICIO 3
    Faça a função pilha_vazia que retorna verifica se a pilha está vazia.
    Deve retornar True se a pilha está vazia e False se não está
"""


def pilha_vazia(pilha):
    tamanho = len(pilha)
    if tamanho > 0:
        return False
    else:
        return True


"""
EXERCICIO 4
    Faça uma função pilha_letras, que recebe uma string e vai colocando as
    letras da string uma a uma em uma pilha.
    Sua função deve retornar a pilha pronta.
"""


def pilha_letras(texto):
    pilha = list(texto)
    return pilha


"""
EXERCICIO 5
    Fazer uma função "menos_o_d". Ela recebe uma string e vai colocando as
    letras uma a uma em uma pilha, como a funcao acima. Porém, quando ela
    vê uma letra d, ao invés de colocar o d, ela faz um pop() na pilha,
    tirando a ultima letra logo antes do d.

    Observe que se a primeira letra for d, ela talvez tente tirar uma coisa de
    uma pilha vazia.
    Outro caso ruim seria a string 'addd', que empilha um a, depois tira,
    depois tenta tirar de novo (3 vezes!)
    Nesses casos ruins, faça o seguinte: se a pilha está vazia e veio um "d",
    simplesmente não tire nada da pilha. Ela continuará vazia.

    Sua função deve retornar a ultima pilha
"""


def menos_o_d(texto):
    pilha = list(texto)
    tamText = len(pilha)
    # lista = []
    i = 0
    while i < tamText:
        elemento = pilha[i]

        if elemento == "d":
            pilha.pop(i)
            indici = i - 1
            pilha.pop(indici)
            tamText = tamText - 3
            i -= 2

        i += 1

    return pilha


"""
EXERCICIO 6
    Faça a função "pilha_par_impar" que recebe uma pilha com 10 inteiros.
    O conteúdo da pilha deve ser distribuído em outras duas pilhas:
    uma contendo os valores pares e outra contendo os valores ímpares.

    Lembre-se que você só pode aceesar os elementos do topo da pilha,
    utilizando operações de "empilhar" e "desempilhar".

    No final, retorne as duas pilhas
"""


def pilha_par_impar(pilha):
    pilha_par = []
    pilha_impar = []

    for i in pilha:
        if i % 2 == 0:
            pilha_par.append(i)
        else:
            pilha_impar.append(i)
    numPar = sorted(pilha_par, key=int, reverse=True)
    numImpar = sorted(pilha_impar, key=int, reverse=True)
    return numPar, numImpar
