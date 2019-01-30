sala = float(input("Qual e o salario do funcionario? R$ "))

if sala <= 1250:
    print(" Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(sala, (sala*0.15)+sala))
else:
    print(" Quem ganhava R${:.2f} passa a ganhar R${:.2f}".format(sala, (sala*0.1)+sala))
