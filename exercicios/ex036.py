num = int(input("Digite um numero inteiro"))

op = int(input("Digite uma opcao: \n [1] Binario \n [2] OCTAL \n [3] Hexadecimal \n Sua opcao: " ))

if op == 1:
    print(" {} em binario e {}".format(num, bin(num)[2:]))
elif op == 2:
    print(" {} em octal e {}".format(num, oct(num)[2:]))
else:
    print(" {} em hexadecimal e {}".format(num,hex(num)[2:]))


