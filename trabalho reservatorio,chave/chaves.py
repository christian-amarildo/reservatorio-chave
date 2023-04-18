A=input("insira o valor da entrada A (ligado/desligado)")
B=input("insira o valor da entrada B (ligado/desligado)")
C=input("insira o valor da entrada C (ligado/desligado)")

if A and B == 'ligado':
    print("a saída S foi ligada")
elif A and C == 'ligado':
    print("a saída S foi ligada")
elif B and C == 'ligado':
    print("a saída S foi ligada")
else:
    print("a saída S está 'desligada'")