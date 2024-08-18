cod_prod = int(input("Código do produto comprado: "))
qtd_prod = int(input("Quantidade comprada: "))
valor = 0

match cod_prod:
    case 1:
        valor = 5 * qtd_prod
    case 2:
        valor = 3.5 * qtd_prod
    case 3:
        valor = 4.8 * qtd_prod
    case 4:
        valor = 8.9 * qtd_prod
    case 5:
        valor = 7.32 * qtd_prod
    case _:
        print("Insira um valor válido")

print(f"Valor a pagar: R${valor:.2f}")