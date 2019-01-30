print("="*30 + '\n 10 TERMOS DE UMA PA \n' + '='*30)
termo = int(input("Primeiro Termo :"))
rzao = int(input("Razao: "))
dec = termo + (10-1) * rzao
for i in range(termo,dec,rzao):
    print(" {} ".format(i),'->',end=" ")
print('ACABOU')

