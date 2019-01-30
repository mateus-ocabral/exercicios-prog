peso = float(input("Seu peso: "))
alt = float(input("Sua altura: "))

imc= peso / (alt*2)

print("O IMC E {}".format(imc))
if imc <=18.5:
    print("Esta abaixo do peso")
elif imc <= 25:
    print("Esta com o PESO NORMAL")
elif imc <= 30:
    print("Esta de sobrepeso")
else:
    print("Esta obeso")