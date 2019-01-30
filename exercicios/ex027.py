import random
seun = int(input("Em qual numero eu pensei? "))
pcn = random.randint(0,5)
print(seun)
print(pcn)
if seun == pcn:
    print("Acertou")
else:
    print("Errou")