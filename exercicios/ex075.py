
tupla = ( int(input("Digite um numero")), int(input("Digite um numero")),int(input("Digite um numero")),int(input("Digite um numero")))

print(f"{tupla.count(9)} repeticoes do 9 ")
print(f"3 apareceu na posicao {tupla.index(3)}")
print("Numeros pares: ",end=" ")
for i in tupla:
    if i % 2 == 0:
        print(i,end=' ')

