from tudo_sobre__Pilhas import (
    desempilhar,
    empilhar,
    menos_o_d,
    pilha_letras,
    pilha_par_impar,
    pilha_vazia,
)


def test_01_empilhar():
    try:
        pilha_teste1 = [2, 3]
        empilhar(pilha_teste1, 4)
        assert pilha_teste1 == [2, 3, 4]
        empilhar(pilha_teste1, 5)
        assert pilha_teste1 == [2, 3, 4, 5]
        pilha_teste2 = []
        empilhar(pilha_teste2, 5)
        assert pilha_teste2 == [5]
        print("empilhar: CORRETO")
    except AssertionError:
        print("empilhar: ERRO")


def test_02_desempilhar():
    try:
        pilha_teste3 = [1, 2, 3, 4, 5, 6, 7]
        topo = desempilhar(pilha_teste3)
        assert topo == 7
        assert pilha_teste3 == [1, 2, 3, 4, 5, 6]
        topo = desempilhar(pilha_teste3)
        assert topo == 6
        assert pilha_teste3 == [1, 2, 3, 4, 5]
        topo = desempilhar(pilha_teste3)
        assert topo == 5
        assert pilha_teste3 == [1, 2, 3, 4]
        print("desempilhar: CORRETO")
    except AssertionError:
        print("desempilhar: ERRO")


def test_03_pilha_vazia():
    try:
        pilha_teste4 = [1, 2, 3]
        assert pilha_vazia(pilha_teste4) is False
        vazia = []
        assert pilha_vazia(vazia) is True
        print("pilha_vazia: CORRETO")
    except AssertionError:
        print("pilha_vazia: ERRO")


def test_04_pilha_letras():
    try:
        pilha = pilha_letras("banana")
        assert pilha == ["b", "a", "n", "a", "n", "a"]
        print("pilha_letras: CORRETO")
    except AssertionError:
        print("pilha_letras: ERRO")


def test_05_menos_o_d():
    try:
        pilha = menos_o_d("banana")
        assert pilha == ["b", "a", "n", "a", "n", "a"]
        pilha = menos_o_d("bandana")
        assert pilha == ["b", "a", "a", "n", "a"]
        pilha = menos_o_d("addd")
        assert pilha == []
        pilha = menos_o_d("dbandanaa")
        assert pilha == ["b", "a", "a", "n", "a"]
        print("menos_o_d: CORRETO")
    except AssertionError:
        print("menos_o_d: ERRO")


def test_06_pilha_par_impar():
    try:
        pilha = [1, 2, 3, 4, 5, 6, 7]
        resultado = pilha_par_impar(pilha)
        assert resultado[0] == [6, 4, 2]
        assert resultado[1] == [7, 5, 3, 1]
        pilha = [4, 6, 8, 10]
        resultado = pilha_par_impar(pilha)
        assert resultado[0] == [10, 8, 6, 4]
        assert resultado[1] == []
        pilha = []
        resultado = pilha_par_impar(pilha)
        assert resultado[0] == []
        assert resultado[1] == []
        print("pilha_par_impar: CORRETO")
    except AssertionError:
        print("pilha_par_impar: ERRO")


test_01_empilhar()
test_02_desempilhar()
test_03_pilha_vazia()
test_04_pilha_letras()
test_05_menos_o_d()
test_06_pilha_par_impar()
