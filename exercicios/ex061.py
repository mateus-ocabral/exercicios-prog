prim = int(input("Primeiro Termo: "))
rza = int(input("Razao da PA:"))

termo = prim
cont = 1
op = 1

while cont <= 10:
    print('{} -> '.format(termo),end=' ')
    termo += rza
    cont +=1

while op != 0:
    op = int(input("\nQuantos a mais voce deseja?"))
    qt = op
    cont+=qt
    while qt > 0:
        print('{} -> '.format(termo), end=' ')
        termo += rza
        qt -= 1

print('FIM')
print(cont-1)