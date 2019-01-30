lista = []
maior = 0
menor = 0

for i in range(1,6):
    peso = float(input(" Peso da {} pessoa: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior =peso
        if peso < menor:
            menor = peso

    lista.append(peso)

print("O maior peso lido foi {}".format(max(lista)))
print("O menor peso lido foi {}".format(min(lista)))
print("="*20)
print("O maior peso lido foi {}".format(maior))
print("O menor peso lido foi {}".format(menor))