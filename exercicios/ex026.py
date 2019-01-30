nome = input("Digite seu nome completo: ").strip().title()
separado= nome.split()
print("Seu primeiro nome e {}".format(separado[0]))
print("Seu ultimo nome e {}".format(separado[len(separado)-1]))
