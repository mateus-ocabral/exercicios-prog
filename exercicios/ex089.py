temp = list()
card = list()

while True:
    temp.append(input("Nome: "))
    temp.append(float(input("Nota 1: ")))
    temp.append(float(input("Nota 2: ")))
    card.append(temp[:])
    temp.clear()
    op = input("Gostaria de Continuar? [s/n]")
    if op in 'Nn':
        break
n = 0
for notatl in card:
    n += 1
    media = (notatl[1]+notatl[2])/2
    print(f'{n} {notatl[0]} {media}')



