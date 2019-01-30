mid = 0
vidade = 0
vnome=''
qtd = 0
for i in range (1,5):
    print("{} pessoa ".format(i))
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo[M,F]").upper()
    mid += idade
    if i == 1 and sexo == 'M':
        vidade = idade
        vnome = nome

    if sexo == 'F':
        if idade < 20:
            qtd += 1
    else:
        if idade > vidade:
            vidade = idade
            vnome = nome
print('A media de idade {} '.format(mid/4))
print('O homem mais velho tem {} e se chama {}'.format(vidade,vnome))
print('Ao todo sao {} mulheres com menos de 20 anos'.format(qtd))


