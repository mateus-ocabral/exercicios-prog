extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze')

num = int(input("Digite um numero de 0 - 12"))
while True:
    if num <=12:
        print(extenso[num])
        num = int(input("Digite um numero de 0 - 12"))
        if num == 999:
            break
    else:
        num = int(input("OPCAO ERRADA! Digite um numero de 0 - 12"))
        if num == 999:
            break



