salario = float(input("Digite o salário: "))
novo_salario = 0
aumento = 0
porcentagem = ""

match salario:
    case _ if salario <= 1000:
        aumento = salario * 0.20
        novo_salario = salario + aumento
        porcentagem = "20%"
    case _ if salario <= 3000:
        aumento = salario * 0.15
        novo_salario = salario + aumento
        porcentagem = "15%"
    case _ if salario <= 8000:
        aumento = salario * 0.10
        novo_salario = salario + aumento
        porcentagem = "10%"
    case _:
        aumento = salario * 0.05
        novo_salario = salario + aumento
        porcentagem = "5%"

print(f"Novo salário: {novo_salario:.2f}")
print(f"Aumento: {aumento:.2f}")
print(f"Porcentagem: {porcentagem}")