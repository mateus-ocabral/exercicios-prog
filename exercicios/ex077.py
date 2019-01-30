tupla =('aprender', 'programar','curso','python','mercado')

for i in tupla:
    print(f" \nNa palavra {i.upper()} temos vogais",end=" ")
    for v in i:
        if v in 'aeiou':
            print(v,end=' ')
