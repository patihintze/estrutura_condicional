minutos = int(input("Digite a quantidade de minutos: "))
valor = 50
if minutos > 100:
    valor = valor + 2 * (minutos - 100)
    print(f"Valor a pagar: R${valor}")
else: print(f"Valor a pagar: R${valor}")