print('='*4 + 'LOJAS' + '='*5)
valor = float(input("Valor a ser pago: "))
print("Formas de Pagamento \n [1] A vista \n [2] Cartao Debito \n [3] 2x credito \n [4] 3x ou mais no credito")
op = int(input("Sua opcao : "))
parc = 0
if op == 1:
    total = valor - (valor*0.1)
    print("Sua compra de {} com desconto fica {}".format(valor, total))

elif op == 2:
    total = valor - (valor*0.05)
    print("Sua compra de {} com desconto fica {}".format(valor, total))

elif op == 4:
    parc = int(input("Quantidade de Parcelas? "))
    total = (valor/parc)+((valor/parc)*0.2)
    print("Sua compra sera parcelada em {}x de R${} com juros".format(parc, total))

print("Sua compra de {} vai custar {} no final".format(valor, total))


