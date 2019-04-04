## TRABAJO PRÁCTICO 1
## Braian Villasanti, Rafael Verde

import random
import pdb

pob_inicial = []
pob_bin = []
f_obj = []
fitness = []
suma = 0
prob_cross = 0.75
prob_mut = 0.05

# Toma una lista "f" fitness, y devuelve un índice de un elemento de esa
# lista usando el método de la ruleta.
def ruleta(f):
    numero = random.uniform(0,1)
    fitness_coincidente = 0.0
    for i in range(11):
        if numero > fitness_coincidente:
            fitness_coincidente += f[i]
        else:
            return i


# Genera población inicial y la guarda
for i in range(10):
    x = random.randint(0, (2**30) - 1)
    pob_inicial.append(x) # como números decimales
    pob_bin.append(str(bin(x))) # y como números binarios.

    f_obj.append((x/(2**30 - 1))**2) # Llena la tabla de función objetivo.

# Iteración de generaciones del algoritmo.
for i in range(200):
    suma_obj = sum(f_obj)
    promedio_obj = suma_obj/10
    max_obj = max(f_obj)
    min_obj = min(f_obj)

    # Genera resultados de función fitness.
    for i in range(10):
        fitness.append(f_obj[i] / suma_obj)

    suma_fit = sum(fitness)
    promedio_fit = suma_fit/10
    max_fit = max(fitness)

    # Muestra la tabla en los valores 20, 100, y 200.
    if i == 19 or i == 99 or i == 199:
        print("Suma: ", suma_obj)
        print("Promedio: ", promedio_obj)
        print("Máximo: ", max_obj)
        print()
        print("FITNESS")
        print(fitness)
        print()
        print("Suma: ", suma_fit)
        print("Promedio: ", promedio_fit)
        print("Máximo: ", max_fit)


    resultado_ruleta = []
    for i in range(10):
        resultado_ruleta.append(ruleta(fitness))

    # Crossover
    for i in range(1, 10, 2):
        #pdb.set_trace()
        if random.randint(0, 100) < 75:
            padre = pob_bin[resultado_ruleta[i] - 1]
            madre = pob_bin[resultado_ruleta[i - 1] - 1]
            punto_cross = random.randint(1,30)
            hijo = list("0b" + str(padre[2:punto_cross + 2]) + str(madre[punto_cross + 2:32]))
            hija = list("0b" + str(madre[2:punto_cross + 2]) + str(padre[punto_cross + 2:32]))
            # Mutación
            if random.randint(0, 100) < 5:
                punto_mutacion = random.randint(2, 32)
                hijo[punto_mutacion] = abs(int(hijo[punto_mutacion]) - 1)
            if random.randint(0, 100) < 5:
                punto_mutacion = random.randint(2, 32)
                hija[punto_mutacion] = abs(int(hija[punto_mutacion]) - 1)
            #pdb.set_trace()
            del pob_bin[resultado_ruleta[i] - 1]
            del pob_bin[resultado_ruleta[i - 1] - 1]
            #pob_bin[resultado_ruleta[i] - 1].remove()  ## = 
            #pob_bin[resultado_ruleta[i - 1] - 1].remove() ##=
            pob_bin.append(str(hija))
            pob_bin.append(str(hijo))

    suma_obj = 0
    promedio_obj = 0
    max_obj = 0
    suma_fit = 0
    promedio_fit = 0
    max_fit = 0