hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))
duracao = 0

if hora_inicial < hora_final:
    duracao = hora_final - hora_inicial

else: duracao = (24 - hora_inicial) + hora_final

print(f"O jogo durou {duracao} hora(s)")