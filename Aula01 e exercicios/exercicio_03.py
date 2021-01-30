# Calcular aumento salarial v.0.1
# Por Dorcival Leite 202003362174
import time
print("APLICACAO DE AUMENTO SALARIAL\n")
sal = float(input("Digite o valor do Salário: "))
perc = float(input("Digite o percentual de aumento (0-100): "))
aum = float(sal * perc / 100)
sfinal = float(sal + aum)
print("\nO Salário de R$", sal, "com o aumento de R$", aum, "é igual a R$", sfinal)
time.sleep(20)