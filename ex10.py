print("Digite dois números inteiros: ")
a = int(input())
b = int(input())

if a % b == 0 or b % a == 0:
    print("São multiplos")
else:
    print("Não são multiplos")