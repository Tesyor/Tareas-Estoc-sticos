import random
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns

#Pregunta 2


def crear_lambdas(n: int) -> list:        
    phi = (1 + (5**0.5))/2
    psi = (1 - (5**0.5))/2  
    lambdas = []          #Tiene que llegar hasta el n-1
    for i in range(1,n):
        lambdaact = ((phi**(n-i+1)) - (psi**(n-i+1)))/(5**0.5)
        lambdas.append(float(lambdaact))
    lambdas.append(0.5) #Ultimo lambda (n)
    return lambdas

def probabilidad_teorica(lambdas: list)-> float:
    cantlamb = len(lambdas)
    actual = 1
    for i in range(cantlamb):
        suma = np.sum(lambdas[i:])
        expresion = (lambdas[i])/(suma)
        actual *= expresion
    return actual

def probabilidad_empirica(lambdas: list, experimentos: int) -> float:
    np.random.seed(2123)
    contador = 0
    for i in range(experimentos):
        valores_lambda = np.array(lambdas, dtype=np.float64)
        tiempos = np.random.exponential(scale=1 / valores_lambda)
        if np.all(np.diff(tiempos) >= 0):
            contador += 1
    return contador/experimentos

resultados = {}
for i in range(2,13):
    lambdas = crear_lambdas(i)
    empirica = probabilidad_empirica(lambdas, 1000)
    teorica = probabilidad_teorica(lambdas)
    error_teorico = abs(teorica - empirica)/teorica
    resultados[i] = (teorica, empirica, error_teorico)
for i in resultados:
    print(f"Cantidad de máquinas ={i}: Probabilidad teórica={resultados[i][0]:.4f}, Probabilidad empírica={resultados[i][1]:.4f}, Error teórico={resultados[i][2]:.4f}")

n_values = list(resultados.keys())
prob_teorica = [resultados[i][0] for i in n_values]
prob_empirica = [resultados[i][1] for i in n_values]

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
plt.plot(n_values, prob_teorica, label="Probabilidad teórica", color='red', linestyle='dashed', linewidth=2)
plt.scatter(n_values, prob_empirica, label="Probabilidad empírica", color='blue', s=100, edgecolors='black')
plt.xlabel("Número de máquinas (n)", fontsize=12)
plt.ylabel("Probabilidad", fontsize=12)
plt.title("Comparación de Probabilidades Teórica vs. Empírica", fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

error = [resultados[i][2]*100 for i in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, error, label="Error teórico", color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)
plt.xlabel("Número de máquinas (n)", fontsize=12)
plt.ylabel("Error Absoluto", fontsize=12)
plt.title("Error Absoluto entre Probabilidad Teórica y Empírica", fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


    

