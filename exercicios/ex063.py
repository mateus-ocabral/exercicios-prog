c = 0
soma = 0
while True:
    n = int(input("Digite um numero: "))
    if n != 999:
        soma += n
        c += 1
    else:
        break





print('Voce digitou {} e a soma entre eles e de {} '.format(c,soma))