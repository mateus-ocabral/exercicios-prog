op=0
while op != 5:
    op = int(input("[1] somar \n [2] Multiplicar \n [3] maior \n [4] novos numeros \n [5] sair \n Sua opcao:"))

    if op == 1:
        pvalor = int(input("Primeiro valor: "))
        svalor = int(input("Segundo valor: "))
        print(" A soma de {} com {} resulta em {}".format(pvalor, svalor, pvalor + svalor))
    elif op == 2:
        pvalor = int(input("Primeiro valor: "))
        svalor = int(input("Segundo valor: "))
        print(" O produto de {} com {} resulta em {}".format(pvalor, svalor, pvalor * svalor))
    elif op == 3:
        pvalor = int(input("Primeiro valor: "))
        svalor = int(input("Segundo valor: "))
        if pvalor > svalor:
            print('O maior valor e {}'.format(pvalor))
        else:
            print('O maior valor e {}'.format(svalor))
    elif op == 4:
        pvalor = int(input("Primeiro valor: "))
        svalor = int(input("Segundo valor: "))
    elif op == 5:
        print("finalizando...")
    else:
        print("Opcao Invalida.tente novamente")
print("Finalizado")