frase = str(input("Digite uma frase:")).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso =''
for inv in range(len(junto)-1,-1,-1):
   inverso += junto[inv]
if junto == inverso:
    print("POLIANDRO")
else:
    print("A palavra {} nao e poliandra da {}".format(junto,inverso))

