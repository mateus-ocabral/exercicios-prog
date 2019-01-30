listagem=('Lapis',1.75,
          'Boracha', 2,
          'Caderno', 15.90,
          'Estojo', 25,
          'Compasso',9.99,
          'Livro', 34.90)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end="")
    else:
        print(listagem[pos])
