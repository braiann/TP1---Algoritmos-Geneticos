## TRABAJO PRÁCTICO 1
## Braian Villasanti, Rafael Verde
"""Notas: -combine este tp con lo que hiciste de la clase cromosoma
          -consecuentemente, la pob_bin ahora es un string
          -la pob_bin solia guardar todos los individuos de todas las poblaciones, ya no
          -consecuentemente, no podemos obtener el mayor cromosoma final
          -y como la pob_bin guarda strings, no puedo guardar los maximos de las poblaciones (ver lineas 116 - 119)"""

import random
from helpers import ruleta, completar_ceros, crossover, mutar, mostrar_info, sort
from clases.cromosoma import Cromosoma
import statistics
import argparse

parser = argparse.ArgumentParser()
poblacion = [] # Población en números enteros
pob_bin = [] # Población en números binarios
f_obj = [] # Resultados de la función objetivo para cada cromosoma
fitness = [] # Resultados de la función fitness
prob_cross = 0.75
prob_mut = 0.05
x_minimos = []
x_promedios= []
x_maximos = []
max_crom = []
n = 10 # Tamaño de la población

# Creación de argumentos para los comandos de cmd
parser.add_argument("-c", "--crossover", help="Cambia el valor de la probabilidad de crossover", type=int)
parser.add_argument("-m", "--mutacion", help="Cambia el valor de la probabilidad de mutación", type=int)
args = parser.parse_args()

#Verfica si se llamó a la flag y si esta cumple con los requisitos; si no cumple termina el programa
if args.crossover:
	if args.crossover <= 100 and args.crossover >= 0:
		prob_cross = args.crossover/100
	else:
		print("! El nro de crossover tiene que ser entre 0 y 100")
		exit()

if args.mutacion:
	if args.mutacion <= 100 and args.mutacion >= 0:
		prob_mut = args.mutacion/100
	else:
		print("! El nro de mutacion tiene que ser entre 0 y 100")
		exit()

# Genera la población inicial.
for i in range(n):
    pob_bin.append(Cromosoma())

# Genera la poblacion en enteros
for i in range(n):
    poblacion.append(pob_bin[i].entero())

# Genera los resultados de la función objetivo.
for i in range(n):
    f_obj.append(pob_bin[i].f_obj())

# Genera los resultados de la función fitness.
for i in range(n):
    fitness.append(f_obj[i]/sum(f_obj))

# Bucle de 200 iteraciones para cada iteración del algoritmo.
for generacion in range(200):
    resultado_ruleta = [] # Lista que guarda los padres que resultarán de la selección.
    nueva_pob_bin = []
    for i in range(n):
        resultado_ruleta.append(pob_bin[ruleta(fitness)])
    print(pob_bin)
    print(fitness)
    fitness_ordenado = sort(fitness) #Generar array de fitneess ordenado
    for i in range(len(fitness)):
        if fitness_ordenado[0] == fitness[i]:
            max_cromosoma_1 = pob_bin[i]
        if fitness_ordenado[1] == fitness[i]:
            max_cromosoma_2 = pob_bin[i]
    print(max_cromosoma_1)
    print(max_cromosoma_2)
	#max_cromosoma_1 = sort(fitness)[0]
	#max_cromosoma_2 = sort(fitness)[1]

    # Crossover
    for i in range(0, 9, 2):
        padre = resultado_ruleta[i]
        madre = resultado_ruleta[i + 1]
        punto_cross = random.randint(0,28)
        crossover(nueva_pob_bin, padre, madre, punto_cross, prob_cross)

    # Mutación
    for i in range(n):
        mutar(nueva_pob_bin[i], prob_mut)

    x_maximos.append(max(f_obj))
    x_minimos.append(min(f_obj))
    x_promedios.append(statistics.mean(f_obj))

    # Resetear todos los datos
    poblacion = []
    f_obj = []
    fitness = []
    pob_bin = nueva_pob_bin

    # Generar la nueva población en números enteros
    for i in range(n):
        poblacion.append(pob_bin[i].entero())

    # Genera resultados de la función objetivo
    for i in range(n):
        f_obj.append(pob_bin[i].f_obj())

    # Genera resultados de función fitness.
    for i in range(n):
        fitness.append(f_obj[i] / sum(f_obj))

    max_crom.append(max(pob_bin.entero()).binario_lindo)
    print(max_crom)

max_crom = sort(max_crom)
# Mostrar todo en un archivo HTML
mostrar_info(''.join(max), x_maximos, x_minimos, x_promedios, prob_cross, prob_mut)
