tab = 1
while True:
    tab = int(input("Deseja ver qual tabuada? "))
    if tab > 0:
        for i in range(1,10):
            print("{} x {} = {}".format(tab,i,(tab*i)))
    else:
        break