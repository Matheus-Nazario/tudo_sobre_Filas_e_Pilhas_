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
    print(numPar, numImpar)


pilha_par_impar([4, 6, 8, 10])
