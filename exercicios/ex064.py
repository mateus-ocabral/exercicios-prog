media = 0
r=''
c=0
nu = int(input("Digite um numero: "))
soma = nu
menor = nu
maior = nu

while r != "N":
    r = str(input("Deseja continuar? ")).upper().strip()
    nu = int(input("Digite um numero: "))
    soma += nu
    c += 1
    if nu > maior:
        maior = nu
    elif nu < menor:
        menor = nu
    r = str(input("Deseja continuar? ")).upper().strip()


media = float (soma/c)
print(media,maior,menor)



