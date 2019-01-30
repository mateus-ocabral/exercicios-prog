n = int(input("Quantos termos voce quer?"))

x=0
y=1

print(x,y,end=" ")

cont = 3
while cont <= n:
    z=x+y
    print(z,end=' ')
    x = y
    y = z
    cont += 1
print("Fim")
