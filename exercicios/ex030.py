dist = float(input("Digite a distancia da sua viagem :"))
if dist <= 200:
    print("Voce esta prestes a comecar uma viagem de {}Km".format(dist))
    print("E o preco da sua passagem sera de R${}".format(dist*0.5))
else:
    print("Voce esta prestes a comecar uma viagem de {}Km".format(dist))
    print("E o preco da sua passagem sera de R${}".format(dist*0.45))
