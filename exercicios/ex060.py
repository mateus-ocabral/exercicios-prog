
c=11
numero = int(input("Digite um numero: "))
razao = int(input("Digite a razao: "))

while c > 1:
    print(numero,'->',end=' ')
    numero+=razao
    c -= 1
print('Acabou')
