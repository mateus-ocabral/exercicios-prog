lista = [[],[]]
lisp=[]
lisi=[]

for i in range(1,8):
  valor = int(input(f"Digite o valor da posicao {i}:"))
  if valor % 2 == 0:
      lista[0].append(valor)
  else:
      lista[1].append(valor)

lista[1].sort()

print(f'A lista dos pares {lista[0]}')
print(f'A lista dos impares {lista[1]}')