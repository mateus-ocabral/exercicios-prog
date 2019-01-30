print('=-='*20)
print('Analisador de Triangulos')
print('=-='*20)
an1 = float(input("Primeiro Angulo: "))
an2 = float(input("Segundo Angulo: "))
an3 = float(input("Terceiro Angulo: "))

if an1+an2>an3 and an1+an3>an2 and an2+an3>an1:
    print("Os segmentos acima PODEM formar um tringulo")
else:
    print("Os segmentos acima NAO PODEM formar um triangulo")