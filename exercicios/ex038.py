from datetime import date
nasc = int(input("Ano de nascimento: "))
ano = date.today().year
idade = ano - nasc

if idade == 18:
    print("Quem nasceu em {} tem {} em {}".format(nasc, idade, ano))
    print("Voce precisa se alistar")
elif idade < 18:
    print("Quem nasceu em {} tem {} em {}".format(nasc, idade, ano))
    print("Ainda falta {} anos para o alistamento ".format(18-idade))
    print("Seu alistamento sera em {} ".format(ano+(18-idade)))
else:
    print("Quem nasceu em {} tem {} em {}".format(nasc, idade, ano))
    print("Ja passou {} anos para o alistamento ".format(idade - 18))
    print("Seu alistamento foi em {} ".format(ano - (idade-18)))