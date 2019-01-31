lista = []
temp = []

while True:
    temp.append(input("Nome"))
    temp.append(float(input("Peso:")))
    if len(lista) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp[1] < men:
            men = temp[1]
    lista.append((temp[:]))
    temp.clear()

    op = input("Deseja Continuar? [s/n]")
    if op in 'Nn':
        break

print(f'Foram adicionados: {len(lista)} usuarios')

print(f'As pessoas com o menor peso de {men} sao',end=" ")
for item in lista:
    if item[1] == men:
        print(f'{item[0]}',end=' ')

print(f'\nAs pessoas com o maior peso de {mai} sao', end=" ")
for item in lista:
    if item[1] == mai:
        print(f'{item[0]}',end=' ')

