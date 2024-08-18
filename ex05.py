preco = float(input("Preço unitário do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))
total_compra = preco * qtd
troco = 0

if dinheiro_recebido < total_compra:
    print(f"Dinheiro insuficiente. Faltam R${total_compra - dinheiro_recebido:.2f}.")
else:
    troco = dinheiro_recebido - total_compra
    print(f"Troco: R${troco:.2f}")