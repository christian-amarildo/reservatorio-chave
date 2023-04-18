#codigo que representa o circuito
b = input("Escolha o valor de b,botão do reservatório (ligado/desligado): ").lower()
n = input("Escolha o valor de n, nível da água no sensor (ligado/desligado): ").lower()

if b == 'desligado':
    print("a saida da água esta ativada e a entrada de água no reservatrio esta desativada")
elif b == 'ligado' and n == 'desligado':
    print("a entrada de água esta ativada e a saída de água esta desativada")
else:
    print("a entrada e a saida de água estão desativados")