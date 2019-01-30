from datetime import date

ano = int(input("Digite o ano que quer analizar. Caso quer analizar o ano atual digite 0"))
if ano == 0:
    ano = date.today().year
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print("O ano {} e bissexto.".format(ano))
else:
    print("O ano {} NAO e bissexto.".format(ano))
