pnota = float(input("Primeira Nota: "))
snota = float(input("Segunda Nota: "))
media = (pnota+snota)/2
print("Tirando {} e {} a media do aluno e {}".format(pnota,snota,media))

if media > 7:
    print("O aluno esta aprovado.")
else:
    print("O aluno esta reprovado: ")
