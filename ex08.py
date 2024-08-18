escala = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if escala == "F":
    temp = float(input("Digite a temperatura em Fahrenheit: "))
    convert_cel = (5 / 9) * (temp - 32)
    print(f"Temperatura equivalente em celsius: {convert_cel:.2f}")
elif escala == "C":
    temp = float(input("Digite a temperatura em celsius: "))
    convert_fah = temp * 1.8 + 32
    print(f"Temperatura equivalente em Fahrenheit: {convert_fah:.2f}")