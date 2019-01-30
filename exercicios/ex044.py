from random import randint
itens = ['pedra','papel','tesoura']
comp = randint(0,2)
print(" Suas Opcoes \n [0] Pedra \n [1] Papel \n [2] Tesoura")
op = int(input("Sua Jogada: "))

print("JO")
print("KEN")
print("PO!!!")
print("Computador: {}".format(itens[comp]))
print("Voce: {}".format(itens[op]))

if comp == 0:
    if op == 0:
        print("EMPATADOS")
    elif op == 1:
        print("Voce Ganhou")
    elif op ==2:
        print("Voce Perdeu")
elif comp == 1:
    if op == 0:
        print("Voce Perdeu")
    elif op == 1:
        print("Empatados")
    elif op == 2:
        print("Voce Ganhou")
elif comp == 2:
    if op == 0:
        print("Voce Ganhou")
    elif op == 1:
        print("Voce Perdeu")
    elif op == 2:
        print("Empatados")