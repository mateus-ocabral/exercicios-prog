import math

ang = float(input("Digite um angulo que voce deseja: "))
print("O angulo de {} tem SENO de {:.2f}".format(ang, math.sin(math.radians(ang)) ))
print("O angulo de {} tem COSS de {:.2f}".format(ang, math.cos(math.radians(ang)) ))
print("O angulo de {} tem TANGENTE de {:.2f}".format(ang, math.tan(math.radians(ang)) ))