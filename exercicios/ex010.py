lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = lar * alt
print("Sua parede tem a dimensao de {:.2f}x{:.2f} e sua area e de {}m2".format(lar,alt,area))
print("Para pintar essa parede, voce precisara de {:.2f}l de tinta".format(area/2))