lista = []
for i in range (0,5):
    valor = int(input("Digite um valor para"))
    if i ==0 or valor > lista[-1]:
        lista.append(valor)
        print("Valor inserido no final da fila")
    else:
        pos = 0
        while pos < len(lista):
            if valor <=lista[pos]:
                lista.insert(pos,valor)
                break
            pos +=1


print(lista)
