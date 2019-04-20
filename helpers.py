import random
import statistics

# Toma una lista "f" fitness, y devuelve un índice de un elemento de esa
# lista usando el método de la ruleta.
def ruleta(f):
    numero = random.uniform(0,1)
    fitness_coincidente = 0.0
    for i in range(10):
        if i >= 9:
            return i
        if numero > fitness_coincidente:
            fitness_coincidente += f[i]
        else:
            return i

# Muestra tablas de valores, sumas, promedios, máximos
def mostrar_tablas(pob_actual, pob_bin, poblacion, f_obj, fitness):
    print("______________________________________________________________________________________")
    print("POBLACIÓN", pob_actual, "\t\t\tX\t FUNCIÓN OBJETIVO\tFUNCIÓN FITNESS")
    for i in range(10):
        print(''.join(pob_bin[i]), poblacion[i], f_obj[i], "\t", fitness[i])
    print("SUMA:\t\t\t\t\t", sum(f_obj), "\t", sum(fitness))
    print("PROMEDIO:\t\t\t\t", statistics.mean(f_obj) / 10, "\t", statistics.mean(fitness))
    print("MÁXIMO:\t\t\t\t\t", max(f_obj), "\t", max(fitness))
    print("______________________________________________________________________________________")
    print()

# Completa los ceros por delante de una lista argumento para que tenga 30 dígitos
def completar_ceros(b):
    for i in range(30 - len(b)):
        b.insert(0, '0')
    return b