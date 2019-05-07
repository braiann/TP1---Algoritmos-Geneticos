import random
import statistics
import webbrowser
import matplotlib.pyplot as plt
import nro
nro = nro.n #Nro de cromosomas en una poblacion

# Toma una lista "f" fitness, y devuelve un índice de un elemento de esa
# lista usando el método de la ruleta.
def ruleta(f):
    numero = random.uniform(0,1)
    fitness_coincidente = 0.0
    for i in range(nro):
        if i >= nro-1:
            return i
        if numero > fitness_coincidente:
            fitness_coincidente += f[i]
        else:
            return i

# Completa los ceros por delante de una lista argumento para que tenga 30 dígitos
def completar_ceros(b):
    for i in range(30 - len(b)):
        b.insert(0, '0')
    return b

# Hay una probabilidad "prob" de que se haga el crossover entre "a" y "b" en el punto "x" en la población "p"
def crossover(p, a, b, x, prob):
    if random.randint(0, 100) < prob*100:
        # pdb.set_trace()
        p.append(a[x:] + b[:x])
        p.append(b[x:] + a[:x])
        try:
            p.remove(a)
            p.remove(b)
        except ValueError:
            pass

# Hay una probabilidad "prob" de que exista una mutación en un bit aleatorio del cromosoma
def mutar(cromosoma, prob):
    if random.randint(0, 100) < prob*100:
        bit_cambiado = random.randint(0,29)
        cromosoma[bit_cambiado] = str(abs(int(cromosoma[bit_cambiado]) - 1))

# Crea un archivo HTML que muestra la información que se pide.
def mostrar_info(cromosoma_final, maximos, minimos, promedios, prob_cross, prob_mut):
    f = open('resultados.html', 'w')

    html_inicial = """<!DOCTYPE html>
    <html>
        <head>
            <title>Trabajo Práctico N°1</title>
            <link rel="stylesheet" type="text/css" href="styles.css">
        </head>
        <body>
            <div>
                <h1>Trabajo Práctico N°1</h1>
                <h2>Algoritmos Genéticos</h2>
                <p>Rafael Verde</p>
                <p>Braian Villasanti</p>"""

    # Muestra el cromosoma máximo final.
    cromosoma_maximo = """<p><b>Cromosoma máximo: </b><div class="monoespaciado">%s</div></p>""" % cromosoma_final

    #Muestra los valores de las probabilidades
    valores = """<p><b>Probabilidad de crossover: </b>%s <b>Probabilidad de mutacion: </b>%s</p>
    <h1>Tablas de valores</h1>""" %(prob_cross, prob_mut)

    # Muestra el valor máximo, mínimo, y promedio de cada población.
    header_tabla = """
    <table>
        <tr>
            <th>Generación</th>
            <th>Máximos</th>
            <th>Mínimos</th>
            <th>Promedios</th>
        </tr>
        """
    
    f.write(html_inicial)
    f.write(cromosoma_maximo)
    f.write(valores)
    f.write(header_tabla)

    for i in range(200):
        tabla = """<tr>
            <td>%d</td>
            <td>%f</td>
            <td>%f</td>
            <td>%f</td>
        </tr>""" %(i + 1, maximos[i], minimos[i], promedios[i])
        f.write(tabla)

    # Muestra tablas de máximos, mínimos, y promedios para 20, 100, y 200 corridas.
    tabla2 = """</table>
    <h1>Valores para las 20, 100, y 200 corridas</h1>
    <table>
        <tr>
            <th>Generación</th>
            <th>Máximos</th>
            <th>Mínimos</th>
            <th>Promedios</th>
        </tr>
        <tr>
            <td>20</td>
            <td>%f</td>
            <td>%f</td>
            <td>%f</td>
        </tr>
        <tr>
            <td>100</td>
            <td>%f</td>
            <td>%f</td>
            <td>%f</td>
        </tr>
        <tr>
            <td>200</td>
            <td>%f</td>
            <td>%f</td>
            <td>%f</td>
        </tr>
    </table>""" % (maximos[19], minimos[19], promedios[19], maximos[99], minimos[99], promedios[99], maximos[199], minimos[199], promedios[199])

    plt.plot(range(200), maximos)
    plt.xlim(0, 200)
    plt.ylim(0, 1)
    plt.autoscale(False)
    plt.savefig('graficos/maximos.svg', bbox_inches='tight')
    plt.clf()
    

    plt.plot(range(200), minimos)
    plt.xlim(0, 200)
    plt.ylim(0, 1)
    plt.autoscale(False)
    plt.savefig('graficos/minimos.svg', bbox_inches='tight')
    plt.clf()

    plt.plot(range(200), promedios)
    plt.xlim(0, 200)
    plt.ylim(0, 1)
    plt.autoscale(False)
    plt.savefig('graficos/promedios.svg', bbox_inches='tight')

    html_final = """
                <h1>Máximos<h1>
                <img src="graficos/maximos.svg">
                <h1>Mínimos<h1>
                <img src="graficos/minimos.svg">
                <h1>Promedios<h1>
                <img src="graficos/promedios.svg">
            </div>
        </body>
    </html>"""

    f.write(tabla2)
    f.write(html_final)
    f.close()

    webbrowser.open_new_tab('resultados.html')