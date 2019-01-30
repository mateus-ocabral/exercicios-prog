maiores = 0
hom = 0
mul = 0

while True:
    id = int(input("Idade"))
    sex = str(input("Sexo [M/F]")).upper()
    if id > 18:
        maiores += 1

    if id < 20 and sex == 'F':
        mul += 1

    if sex == 'M':
        hom += 1


    r = str(input("Deseja Continuar[S/N]")).upper()

    if r != 'S':
        break



print("{} maiores, {} homens {} mulheres".format(maiores, hom, mul))