from random import randint
pont = 0


while True:
    pcn = randint(0,10)
    seun = int(input("Diga um valor"))
    opc = str(input("Par ou Impar?")).upper()
    soma = seun + pcn
    if soma % 2 == 0:
        print("Voce escolheu {} e o computador {}. A soma deu {} que e PAR ".format(seun, pcn, soma))
        if opc == 'P':
            print("Voce Venceu!")
            pont += 1
        else:
            print("Voce Perdeu")
            break
    else:
        print("Voce escolheu {} e o computador {}. A soma deu {} que e IMPAR ".format(seun, pcn, soma))
        if opc == 'I':
            print("Voce Venceu!")
            pont += 1
        else:
            print("Voce Perdeu")
            break

print('Game Over')
print('Voce venceu {} vezes'.format(pont))

