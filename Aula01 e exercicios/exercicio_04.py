# Calcular desconto mercadoria v.0.1
# Por Dorcival Leite 202003362174
import time
print("APLICACAO DE DESCONTO MERCADORIA\n")
merc = float(input("Digite o valor da mercadoria: "))
perc = float(input("Digite o percentual de desconto (0-100): "))
desc = float(merc * perc / 100)
vfinal = float(merc - desc)
print("\nA mercadoria de R$", merc, "com o desconto de R$", desc, "é igual a R$", vfinal)
time.sleep(20)