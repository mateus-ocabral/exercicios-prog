tab = int(input("Digite um numero para ver sua tabuada: "))

for i in range(1,11):
    print("{} x {} = {} ".format(tab,i,(tab*i)))
    i+=1
print('='*20)