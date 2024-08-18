primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
terceiro = int(input("Terceiro valor: "))

if primeiro < segundo and primeiro < terceiro:
    print(f"Menor: {primeiro}")
if segundo < terceiro:
    print(f"Menor: {segundo}")
else:
    print(f"Menor: {terceiro}")