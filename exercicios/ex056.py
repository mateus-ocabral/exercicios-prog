sexo = str(input("Digite seu sexo: [M/F]")).strip().upper()
while sexo not in 'MmfF':
    sexo = str(input("Opcao Invalidade. Digite seu sexo: [M/F]")).strip().upper()
