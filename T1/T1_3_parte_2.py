import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
from scipy.special import factorial

tasa_b = 0.1
tasa_l = 0.15
p_b = 0.3
p_l = 0.2
np.random.seed(2123)

def probabilidad_teorica_1() -> float:
    tasa_mod_b = 45 * tasa_b * p_b
    tasa_mod_l = 45 * tasa_l * p_l
    i = np.arange(2, 100)
    
    expresion = ((((tasa_mod_b**i)*(np.exp(-1*tasa_mod_b)))/factorial(i)) *
                 (((tasa_mod_l**(i-2))*np.exp(-1*tasa_mod_l))/factorial(i-2)))
    
    resultado = np.sum(expresion)
    return resultado

def probabilidad_teorica_2() -> float:
    tasa_mod_b = 30 * tasa_b * p_b
    tasa_mod_l = 30 * tasa_l * p_l
    i = np.arange(0, 100)
    
    expresion = ((((tasa_mod_b**i)*(np.exp(-1*tasa_mod_b)))/factorial(i)) *
                 (((tasa_mod_l**i)*(np.exp(-1*tasa_mod_l)))/factorial(i)))
    resultado = np.sum(expresion)
    return resultado

def probabilidad_teorica_3() -> float:
    tasa_mod_b = 90 * tasa_b * p_b
    tasa_mod_l = 90 * tasa_l * p_l
    i = np.arange(1, 100)
    
    expresion = ((((tasa_mod_l**i)*(np.exp(-1*tasa_mod_l)))/factorial(i)) * np.exp(-1*tasa_mod_b))
    
    resultado = np.sum(expresion)
    return resultado

def probabilidad_empirica_1(experimentos: int) -> float:

    tasa_mod_b = tasa_b * p_b
    tasa_mod_l = tasa_l * p_l
    contador = 0
    for i in range(experimentos):
        if np.sum(np.random.poisson(tasa_mod_b,45)) == (np.sum((np.random.poisson(tasa_mod_l,45)))+2):
            contador += 1
    return contador / experimentos


def probabilidad_empirica_2(experimentos: int) -> float:

    tasa_mod_b = tasa_b * p_b
    tasa_mod_l = tasa_l * p_l
    contador = 0
    for i in range(experimentos):
        if np.sum(np.random.poisson(tasa_mod_b,30)) == np.sum(np.random.poisson(tasa_mod_l,30)):
            contador += 1
    return contador / experimentos


def probabilidad_empirica_3(experimentos: int) -> float:

    tasa_mod_b = tasa_b * p_b
    tasa_mod_l = tasa_l * p_l
    contador = 0
    for i in range(experimentos):
        if np.sum(np.random.poisson(tasa_mod_l,90)) > 0:
            if np.sum(np.random.poisson(tasa_mod_b,90)) == 0:
                contador += 1
    return contador / experimentos

teorica_1 = round(probabilidad_teorica_1(),5)
teorica_2 = round(probabilidad_teorica_2(),5)
teorica_3 = round(probabilidad_teorica_3(),5)
empirica_1 = round(probabilidad_empirica_1(1000000),5)
empirica_2 = round(probabilidad_empirica_2(1000000),5)
empirica_3 = round(probabilidad_empirica_3(1000000),5)
error_1 = round(abs(teorica_1 - empirica_1)/teorica_1,5)
error_2 = round(abs(teorica_2 - empirica_2)/teorica_2,5)
error_3 = round(abs(teorica_3 - empirica_3)/teorica_3,5)

print("-"*50)
print(f"Que el VARcelona vaya ganando por 2 goles al final del primer tiempo:")
print(f"Probabilidad teorica: {teorica_1}")
print(f"Probabilidad empirica: {empirica_1}")
print(f"Error teorico: {error_1}")
print("-"*50)
print(f"Que el partido termine en empate si no hubo goles en los primeros 60 minutos:")
print(f"Probabilidad teorica: {teorica_2}")
print(f"Probabilidad empirica: {empirica_2}")
print(f"Error teorico: {error_2}")
print("-"*50)
print(f"Que el LiVARpool gane el partido sin recibir goles:")
print(f"Probabilidad teorica: {teorica_3}")
print(f"Probabilidad empirica: {empirica_3}")
print(f"Error teorico: {error_3}")
print("-"*50)

print("El ingreso esperado por cada apuesta (sin contar que se gastaron 10000): ")
print(f"El ingreso para la apuesta de que VARcelona vaya ganando por 2 goles en el primer tiempo: {empirica_1 * 10000 * 6}")
print(f"El ingreso para la apuesta de que el partido termine en empate si no habia goles en los primeros 60 minutos: {empirica_2 * 10000 * 2}")
print(f"El ingreso para la apuesta de que el LiVARpool gane el partido sin recibir goles: {empirica_3 * 10000 * 5}")
print(" ")
print(" ")
print("Calculamos que pasaría con las probabilidades y los ingresos si pb aumenta a 0.35:")

p_b = 0.35

teorica_1 = round(probabilidad_teorica_1(),5)
teorica_2 = round(probabilidad_teorica_2(),5)
teorica_3 = round(probabilidad_teorica_3(),5)
empirica_1 = round(probabilidad_empirica_1(1000000),5)
empirica_2 = round(probabilidad_empirica_2(1000000),5)
empirica_3 = round(probabilidad_empirica_3(1000000),5)
error_1 = round(abs(teorica_1 - empirica_1)/teorica_1,5)
error_2 = round(abs(teorica_2 - empirica_2)/teorica_2,5)
error_3 = round(abs(teorica_3 - empirica_3)/teorica_3,5)

print("-"*50)
print(f"Que el VARcelona vaya ganando por 2 goles al final del primer tiempo:")
print(f"Probabilidad teorica: {teorica_1}")
print(f"Probabilidad empirica: {empirica_1}")
print(f"Error teorico: {error_1}")
print("-"*50)
print(f"Que el partido termine en empate si no hubo goles en los primeros 60 minutos:")
print(f"Probabilidad teorica: {teorica_2}")
print(f"Probabilidad empirica: {empirica_2}")
print(f"Error teorico: {error_2}")
print("-"*50)
print(f"Que el LiVARpool gane el partido sin recibir goles:")
print(f"Probabilidad teorica: {teorica_3}")
print(f"Probabilidad empirica: {empirica_3}")
print(f"Error teorico: {error_3}")
print("-"*50)
print("El ingreso esperado por cada apuesta (sin contar que se gastaron 10000): ")
print(f"El ingreso para la apuesta de que VARcelona vaya ganando por 2 goles en el primer tiempo: {empirica_1 * 10000 * 6}")
print(f"El ingreso para la apuesta de que el partido termine en empate si no habia goles en los primeros 60 minutos: {empirica_2 * 10000 * 2}")
print(f"El ingreso para la apuesta de que el LiVARpool gane el partido sin recibir goles: {empirica_3 * 10000 * 5}")

