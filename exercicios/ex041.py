seg1 = float(input("Primeiro Segmento: "))
seg2 = float(input("Segundo Segmento: "))
seg3 = float(input("Terceiro Segmento: "))

if seg1+seg2>seg3 and seg1+seg3>seg2 and seg2+seg3>seg1:
    if seg1 == seg2 and seg2 == seg3:
        print("Triangulo Retangulo")
    elif seg1 != seg2 and seg2 != seg3 and seg1 != seg3:
        print("Trinagulo Escaleno ")
    else:
        print("Triangulo Isoceles")
else:
    print("Nao forma triangulo")