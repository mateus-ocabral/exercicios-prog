matriz = [[0,0,0], [0,0,0], [0,0,0]]

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f"Digite valores [{l}][{c}]"))


for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]}]',end=' ')
    print()

soma2 = 0
soma1 = 0
soma0 = 0

for l in range (0,3):
    soma2 += matriz[l][2]
    soma1 += matriz[l][1]
    soma0 += matriz[l][0]

print(soma0,soma1,soma2)
