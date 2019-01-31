
lista = []
menorl = []
maiorl = []
for i in range (0,5):

    num = int(input(f"Digite um valor para a posicao {i}"))
    lista.append(num)
    if i == 0:
        menor=num
        maior=num


    else:
        if num > maior:
            maior = num
            maior =


        if menor > num:
            menor = num



print(f"O maior valor digitado foi {maior} nas posicoes")
print(lista.index(maior))


print(f"O menor valor digitado foi {menor} nas posicoes")

for i in range(0, lista.count(menor)):
    print(lista.index(menor))

print(lista)