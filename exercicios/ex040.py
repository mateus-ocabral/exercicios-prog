from datetime import date
nasc = int(input("Ano de Nascimento: "))
ano = date.today().year
idade = ano - nasc

print(" O atleta tem {} anos".format(idade))

if idade <= 9:
    print("Se trata de um atleta MIRIM")
elif idade <= 14:
    print("Se trata de um atleta INFANTIL")
elif idade <= 19:
    print("Se trata de um atleta JUNIOR")
elif idade <= 25:
    print("Se trata de um atleta SENIOR")
else:
    print("Se trata de um atleta MASTER")

