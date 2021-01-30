# Somar a quantidade total em segundos v.0.1
# Por Dorcival Leite 202003362174
import time
print("CONVERSAO DO TEMPO EM SEGUNDOS\n")
d = int(input("Digite a quantidade de dias: "))
h = int(input("Digite a quantidade de horas: "))
min = int(input("Digite a quantidade de minutos: "))
s = int(input("Digite a quantidade de segundos: "))
totals = ((d*86400)+(h*3600)+(min*60)+s)
print("\n", d, "dias +", h, "horas +", min, "minutos +", s, "segundos =", totals, "segundos")
time.sleep(20)