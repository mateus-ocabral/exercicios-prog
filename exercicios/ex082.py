lista = []
listpar = []
listimpar = []
while True:
    valor = int(input("Digite um valor:"))
    lista.append(valor)
    if valor % 2 ==0:
        listpar.append(valor)
    else:
        listimpar.append(valor)
    op = str(input("Deseja Continuar?"))
    if op in 'Nn':
        break


print(f' Lista Completa: {lista}')
print(f'LIsta dos impares: {listimpar}')
print(f'Lista dos pares: {listpar}')