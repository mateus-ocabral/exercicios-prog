num = int(input("Digite um numero: "))
cc=0
for n in range(1,num+1):
    if num % n == 0:
        print('\33[33m',end=' ')
        cc += 1
    else:
        print('\33[31m',end=' ')
    print('{}'.format(n),end=' ')




print("\n\33[mO numero {} foi divisivel {} vezes".format(num,cc))
if cc <= 2:
    print("E por isso ele e PRIMO!")
else:
    print("E por isso ele NAO E PRIMO!")


