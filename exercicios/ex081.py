lista=[]
inverso = []
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    op = str(input("Deseja continuar? [S/N]"))
    if op in 'Nn':
        break
print(f"Voce digitou {len(lista)} valores")

print(f'Os valores em ordem decrescente {sorted(lista,reverse=True)}')
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 NAO FAZ parte da lista!")

