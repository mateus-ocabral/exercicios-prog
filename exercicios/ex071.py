saque = float(input("Qual o valor voce deseja sacar?"))
ce50=0
ce10=0
ce1=0
if saque > 50:
   ce50 = int(saque // 50)
   saque -= (ce50*50)
   if saque > 10:
       ce10 = int(saque // 10)
       saque -= (ce10 * 10)
       if saque > 1:
           ce1 = int(saque // 1)
           saque -= (ce1 * 1)
elif saque > 10:
    ce10 = int(saque // 10)
    saque -= (ce10 * 10)
    if saque > 1:
        ce1 = int(saque // 1)
        saque -= (ce1 * 1)
else:
    ce1 = int(saque // 1)
    saque -= (ce1 * 1)

print("Total de {} cedulas de R$ 50".format(ce50))
print("Total de {} cedulas de R$ 10".format(ce10))
print("Total de {} cedulas de R$ 1".format(ce1))

