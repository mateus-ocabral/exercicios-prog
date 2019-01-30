import random

lista = []
for i in range (1,6):
    lista.append(random.randint(0,10))

print(sorted(lista))
print(max(lista))
print(min(lista))