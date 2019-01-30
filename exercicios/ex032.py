valor1 = int(input('Primeiro Valor'))
valor2 = int(input('Segundo Valor'))
valor3 = int(input('Terceiro Valor'))

lista = [valor1, valor2, valor3]

print('O menor valor digitado foi {}'.format(min(lista)))
print('O maior valor digitado foi {}'.format(max(lista)))

print('='*20)



menor=valor1
if valor2<valor3 and valor2<valor1:
    menor=valor2
if valor3<valor2 and valor3<valor1:
    menor=valor3

maior=valor1
if valor2>valor3 and valor2>valor1:
    maior=valor2
if valor3>valor2 and valor3>valor1:
    maior=valor3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))