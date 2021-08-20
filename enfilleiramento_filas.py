from tudo_sobre_Filas import (
    desenfileirar,
    enfileirar,
    fila_inicial,
    fila_vazia,
    primeiro,
    tamanho,
    vira_1,
)


def test_01_enfileirar():
    try:
        fila = [1, 2]
        enfileirar(fila, 5)
        assert fila == [1, 2, 5]
        enfileirar(fila, 10)
        assert fila == [1, 2, 5, 10]
        fila = [1, 2]
        enfileirar(fila, 10)
        assert fila == [1, 2, 10]
        print("enfileirar: CORRETO")
    except AssertionError:
        print("enfileirar: ERRO")


def test_02_desenfileirar():
    try:
        fila = [10, 4, 5]
        primeiro = desenfileirar(fila)
        assert primeiro == 10
        assert fila == [4, 5]
        primeiro = desenfileirar(fila)
        assert primeiro == 4
        assert fila == [5]
        primeiro = desenfileirar(fila)
        assert primeiro == 5
        assert fila == []
        fila = [11, 12, 13]
        primeiro = desenfileirar(fila)
        assert primeiro == 11
        assert fila == [12, 13]
        print("desenfileirar: CORRETO")
    except AssertionError:
        print("desenfileirar: ERRO")


def test_03_tamanho():
    try:
        fila = [10, 4, 5]
        assert tamanho(fila) == 3
        desenfileirar(fila)
        assert tamanho(fila) == 2
        desenfileirar(fila)
        assert tamanho(fila) == 1
        desenfileirar(fila)
        assert tamanho(fila) == 0
        print("tamanho: CORRETO")
    except AssertionError:
        print("tamanho: ERRO")


def test_04_fila_vazia():
    try:
        fila = [4, 50, 2]
        assert fila_vazia(fila) is False
        desenfileirar(fila)
        assert fila_vazia(fila) is False
        desenfileirar(fila)
        assert fila_vazia(fila) is False
        desenfileirar(fila)
        assert fila_vazia(fila) is True
        enfileirar(fila, 12)
        assert fila_vazia(fila) is False
        print("fila_vazia: CORRETO")
    except AssertionError:
        print("fila_vazia: ERRO")


def test_05_primeiro():
    try:
        fila = [4, 3, 2]
        primeiro_numero = primeiro(fila)
        assert primeiro_numero == 4
        if fila != [4, 3, 2]:
            print("fila_vazia: ERRO - nao deve retirar da fila")
            raise AssertionError
        print("primeiro: CORRETO")
    except AssertionError:
        print("primeiro: ERRO")


def test_06_vira_1():
    try:
        fila = [1, 2, 3, 4]
        vira_1(fila)
        assert fila == [2, 3, 4, 1]
        vira_1(fila)
        assert fila == [3, 4, 1, 2]
        print("vira_1: CORRETO")
    except AssertionError:
        print("vira_1: ERRO")


def test_07_fila_inicial():
    try:
        assert fila_inicial(4) == [1, 2, 3, 4]
        assert fila_inicial(8) == [1, 2, 3, 4, 5, 6, 7, 8]
        print("fila_inicial: CORRETO")
    except AssertionError:
        print("fila_inicial: ERRO")


test_01_enfileirar()
test_02_desenfileirar()
test_03_tamanho()
test_04_fila_vazia()
test_05_primeiro()
test_06_vira_1()
test_07_fila_inicial()
