# Calcular o tempo de viagem v.0.1
# Por Dorcival Leite 202003362174
import time
print("CALCULAR O TEMPO DE VIAGEM\n")
dist = float(input("Digite a distância percorrida (km): "))
velm = float(input("Digite a Velocidade Média: "))
t = float(dist / velm)
min = t * 60
print("\nO tempo de viagem foi de", t, "hora(s) ou", min, "minutos")
time.sleep(20)