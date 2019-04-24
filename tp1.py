## TRABAJO PRÁCTICO 1
## Braian Villasanti, Rafael Verde

import random
import pdb # BORRAR en versión final
from helpers import ruleta, mostrar_tablas, completar_ceros, crossover, mutar
import matplotlib.pyplot as plt

poblacion = []
pob_bin = []
f_obj = []
fitness = []
suma = 0
prob_cross = 0.75
prob_mut = 0.05 
parametro = []
x = []

# Genera población inicial y la guarda
for i in range(10):
    x = random.randint(0, (2**30) - 1)
    poblacion.append(x) # como números decimales
    pob_bin.append(completar_ceros((list(str(bin(x))))[2:])) # y como números binarios de 30 dígitos.
    f_obj.append((x/(2**30 - 1))**2) # Llena la tabla de función objetivo.

# Genera resultados de función fitness.
for i in range(10):
    fitness.append(f_obj[i] / sum(f_obj))

for generacion in range(200):
    if generacion == 19 or generacion == 99 or generacion == 199:
        mostrar_tablas(generacion + 1, pob_bin, poblacion, f_obj, fitness)

    resultado_ruleta = []
    for i in range(10):
        resultado_ruleta.append(pob_bin[ruleta(fitness)])
 
    # Crossover
    for i in range(0, 9, 2):
        padre = resultado_ruleta[i]
        madre = resultado_ruleta[i + 1]1
           punto_cross = random.randint(0,28)
        crossover(pob_bin, padre, madre, punto_cross, prob_cross)

    # Mutación
    for i in range(10):
        mutar(pob_bin[i], prob_mut)

    # Resetear todos los datos menos los de la población binaria
    poblacion = []
    f_obj = []
    fitness = []
    suma_obj = 0
    promedio_obj = 0
    max_obj = 0
    suma_fit = 0
    promedio_fit = 0
    max_fit = 0

    # Generar la nueva población en números enteros
    for i in range(10):
        poblacion.append(int(''.join(pob_bin[i]), 2))

    # Genera resultados de la función objetivo
    for i in range(10):
        f_obj.append((poblacion[i]/(2**30 - 1))**2)

    # Genera resultados de función fitness.
    for i in range(10):
        fitness.append(f_obj[i] / sum(f_obj))

    x_minimos = []
    x_promedios= []
    x_maximos = []

    plrot.