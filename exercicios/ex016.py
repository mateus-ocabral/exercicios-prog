from math import hypot
from math import sqrt
caop = float(input("Digite o valor do cateto oposto: "))
caad = float(input("Digite o valor do cateto ajacente: "))
print("O valor da hipotenusa {:.2f}".format(sqrt(caop**2+caad**2)))
print("O valor de hip {:.2f}".format(hypot(caop, caad)))