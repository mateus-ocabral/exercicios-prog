valorc = float(input("Valor da casa: "))
sala = float(input("Salario do comprador: "))
anos = int(input("Quantidade de anos: "))


print("Para pagar uma casa de R${} em {} anos a prestacao sera R${}".format(valorc,anos,(valorc/(anos * 12))))
if (valorc/(anos * 12)) <= (sala*0.3):
    print("Emprestimo pode ser CONCEDIDO")
else:
    print("Emprestimo NEGADO!")