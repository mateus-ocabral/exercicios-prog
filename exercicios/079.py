lista = []
num = int(input("Digite um numero"))
print("Valor adicionado...")
lista.append(num)
while True:
    op = str(input("Deseja Continuar?[S/N]"))
    if op in 'Nn':
        break
    else:
        num = int(input("Digite um numero"))
        if num not in lista:
            lista.append(num)
        else:
            print("Numero Ja esta na lista")




print(lista)