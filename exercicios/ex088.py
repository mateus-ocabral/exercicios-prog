from random import randint
mega = list()
jogo = list()

qt = int(input("Numero de Jogos: "))
tot = 1
while tot <= qt:
    cc =0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cc += 1
        if cc >= 6:
            break
    mega.append(jogo[:])
    jogo.clear()
    tot += 1

for jogo in mega:
    print(f'{jogo}')


