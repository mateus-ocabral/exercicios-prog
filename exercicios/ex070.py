
soma = 0
mil = 0
bar = 0
produ = ' '
count = 0
while True:
    prod = str(input("Nome do Produto"))
    pre = float(input("Preco"))
    soma += pre
    count += 1
    if pre > 1000:
        mil += 1

    if count == 1 or bar > pre:
        bar = pre
        produ = prod



    r = str(input("Deseja Continuar?")).upper()

    if r == 'N':
        break
print(soma,mil)
print(produ,bar)