pilha = []

expres = str(input("Digite uma expressao :"))
esq = expres.count('(')
dire = expres.count(')')

if esq == dire:
    print('Expressao Valida!')
else:
    print('Expressao Errada!')

expres = str(input("Digite uma expressao :"))
for simb in expres:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            break
if len(pilha) > 0:
    print('Sua Expressao esta errada!')
else:
    print('Sua Expressao esta certa!')
