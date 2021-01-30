# Reducao tempo de vida fumantes v.0.1
# Considerando que 1 cigarro = 10min 
# Por Dorcival Leite 202003362174
import time
print("REDUCAO TEMPO DE VIDA DOS FUMANTES\n")
cdia = int(input("Digite a quantidade de cigarros que fuma POR DIA: "))
qanos = float(input("Digite a quantidade de ANOS que já fumou: "))
dias = qanos * 365     # transf de anos para dias 
fumados = dias * cdia  # total de cigarros fumados 
tmin = fumados * 10    # tempo vida reduzido em minutos
tdias = tmin / 1440    # transf de minutos para dias
print("\nEsse fumante perderá", tdias, "DIAS do seu tempo total de vida.")
time.sleep(20)