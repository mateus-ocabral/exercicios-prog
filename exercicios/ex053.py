from datetime import date

ano = date.today().year
maior=0
menor=0
for i in range(1,8):
    nasc = int(input("Em que ano a {}  pessoa nasceu?".format(i)))
    if (ano - nasc) > 18:
        maior+=1
    else:
        menor+=1
print("Ao todo foram {} maiores de idade".format(maior))
print("Ao todo foram {} menores de idade".format(menor))



