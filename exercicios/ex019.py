import random
aluno1 = input("Digite um nome de aluno: ")
aluno2 = input("Digite um nome de aluno: ")
aluno3 = input("Digite um nome de aluno: ")
aluno4 = input("Digite um nome de aluno: ")

lista=[aluno1, aluno2, aluno3, aluno4]

print(random.shuffle(lista))

random.shuffle(lista)
print(lista)