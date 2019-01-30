from random import randint
print(" Sou seu computador...")
print("Pensei em um numero entre 0 e 10, Tente advinhar")

comp = randint(1,10)
seun = int(input("Seu palpite: "))

while seun != comp:
    print("Voce Errou!")
    seun = int(input("Digite seu palpite: "))
print("Parabens! Voce acertou.")