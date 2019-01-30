lista = []
for i in range (0,5):

    num = int(input(f"Digite um valor para a posicao {i}"))
    if i == 0:
        menor=num
        maior=num
        lista.append(num)

    else:
        if num > maior:
            maior = num
            lista.append(num)

        if menor > num:
            menor = num
            lista.append(num)


print(f"O maior valor digitado foi {maior} nas posicoes")


print(f"O menor valor digitado foi {menor} nas posicoes")

print(num)
