## TRABAJO PRÁCTICO 1
## Braian Villasanti, Rafael Verde

import random
import pdb
from helpers import *

pob_actual = 1
poblacion = []
pob_bin = []
f_obj = []
fitness = []
suma = 0
prob_cross = 0.75
prob_mut = 0.05

# Genera población inicial y la guarda
for i in range(10):
    x = random.randint(0, (2**30) - 1)
    poblacion.append(x) # como números decimales
    pob_bin.append(completar_ceros((list(str(bin(x))))[2:])) # y como números binarios de 30 dígitos.
    f_obj.append((x/(2**30 - 1))**2) # Llena la tabla de función objetivo.

suma_obj = sum(f_obj)
promedio_obj = suma_obj/10
max_obj = max(f_obj)

# Genera resultados de función fitness.
for i in range(10):
    fitness.append(f_obj[i] / suma_obj)

suma_fit = sum(fitness)
promedio_fit = suma_fit/10
max_fit = max(fitness)

mostrar_tablas(pob_actual, pob_bin, poblacion, f_obj, fitness)

resultado_ruleta = []
for i in range(10):
    resultado_ruleta.append(pob_bin[ruleta(fitness)])

# print("Ruleta:")
# print(resultado_ruleta)

# Crossover
for i in range(0, 9, 2):
    # pdb.set_trace()
    padre = resultado_ruleta[i]
    madre = resultado_ruleta[i + 1]
    punto_cross = random.randint(0,28)
    if random.randint(0, 100) < prob_cross*100:
        # pdb.set_trace()
        pob_bin.append(padre[punto_cross:] + madre[:punto_cross])
        pob_bin.append(madre[punto_cross:] + padre[:punto_cross])
        try:
            pob_bin.remove(padre)
            pob_bin.remove(madre)
        except ValueError:
            pass

# Mutación
for i in range(10):
    if random.randint(0, 100) < prob_mut*100:
        bit_cambiado = random.randint(0,29)
        pob_bin[i][bit_cambiado] = str(abs(int(pob_bin[i][bit_cambiado]) - 1))

poblacion = []
f_obj = []
fitness = []
suma_obj = 0
promedio_obj = 0
max_obj = 0
suma_fit = 0
promedio_fit = 0
max_fit = 0

for i in range(10):
    poblacion.append(int(''.join(pob_bin[i]), 2))

for i in range(10):
    f_obj.append((poblacion[i]/(2**30 - 1))**2)

suma_obj = sum(f_obj)
promedio_obj = suma_obj/10
max_obj = max(f_obj)

# Genera resultados de función fitness.
for i in range(10):
    fitness.append(f_obj[i] / suma_obj)

suma_fit = sum(fitness)
promedio_fit = suma_fit/10
max_fit = max(fitness)

mostrar_tablas(pob_actual, pob_bin, poblacion, f_obj, fitness)