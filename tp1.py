## TRABAJO PRÁCTICO 1
## Braian Villasanti, Rafael Verde

import random
from helpers import ruleta, completar_ceros, crossover, mutar, mostrar_info
import statistics
import argparse

parser = argparse.ArgumentParser()
poblacion = [] # Población en números enteros
pob_bin = [] # Población en números binarios
f_obj = [] # Resultados de la función objetivo para cada cromosoma
fitness = [] # Resultados de la función fitness
prob_cross = 0.75
prob_mut = 0.05
x = []
x_minimos = []
x_promedios= []
x_maximos = []
n = 10 # Tamaño de la población

# Creación de argumentos para los comandos de cmd
parser.add_argument("-c", "--crossover", help="Cambia el valor de la probabilidad de crossover", type=int)
parser.add_argument("-m", "--mutacion", help="Cambia el valor de la probabilidad de mutación", type=int)
args = parser.parse_args()

if args.crossover:
	prob_cross = args.crossover

if args.mutacion:
	prob_mut = args.mutacion

# Genera población inicial y la guarda
for i in range(n):
    x = random.randint(0, (2**30) - 1)
    poblacion.append(x) # como números decimales
    pob_bin.append(completar_ceros((list(str(bin(x))))[2:])) # y como números binarios de 30 dígitos.
    f_obj.append((x/(2**30 - 1))**2) # Llena la tabla de función objetivo.

# Genera resultados de función fitness.
for i in range(n):
    fitness.append(f_obj[i] / sum(f_obj))

# Bucle de 200 iteraciones para cada iteración del algoritmo.
for generacion in range(200):
    resultado_ruleta = [] # Lista que guarda los padres que resultarán de la selección.
    for i in range(n):
        resultado_ruleta.append(pob_bin[ruleta(fitness)])
 
    # Crossover
    for i in range(0, 9, 2):
        padre = resultado_ruleta[i]
        madre = resultado_ruleta[i + 1]
        punto_cross = random.randint(0,28)
        crossover(pob_bin, padre, madre, punto_cross, prob_cross)

    # Mutación
    for i in range(n):
        mutar(pob_bin[i], prob_mut)
    
    x_maximos.append(max(f_obj))
    x_minimos.append(min(f_obj))
    x_promedios.append(statistics.mean(f_obj))

    # Resetear todos los datos menos los de la población binaria
    poblacion = []
    f_obj = []
    fitness = []
    
    # Generar la nueva población en números enteros
    for i in range(n):
        poblacion.append(int(''.join(pob_bin[i]), 2))

    # Genera resultados de la función objetivo
    for i in range(n):
        f_obj.append((poblacion[i]/(2**30 - 1))**2)

    # Genera resultados de función fitness.
    for i in range(n):
        fitness.append(f_obj[i] / sum(f_obj))

# Mostrar todo en un archivo HTML
mostrar_info(''.join(max(pob_bin)), x_maximos, x_minimos, x_promedios, prob_cross, prob_mut)
