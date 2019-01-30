algo = input("digite algo:")
print("O tipo primitivo desse valor e {}".format(type(algo)))
print("So tem espacos? {} ".format(algo.isspace()))
print("Numero? {}".format(algo.isnumeric()))
print("Alfabetico? {}".format(algo.isalpha()))
print("Esta em caixa alta? {}".format(algo.isupper()))
print("Esta em caixa baixa? {}".format(algo.islower()))
print("Esta capitalizado? {} ".format(algo.istitle()))

