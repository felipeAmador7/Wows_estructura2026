cubo_inicio = [
[' ',' ',' ','W','W','W',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','W','W','W',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','W','W','W',' ',' ',' ',' ',' ',' '],

['O','O','O','G','G','G','R','R','R','B','B','B'],
['O','O','O','G','G','G','R','R','R','B','B','B'],
['O','O','O','G','G','G','R','R','R','B','B','B'],

[' ',' ',' ','Y','Y','Y',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','Y','Y','Y',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','Y','Y','Y',' ',' ',' ',' ',' ',' ']
]

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def dibujar_cubo(cubo):
    colores = {
        'W': 'white',
        'O': 'orange',
        'G': 'green',
        'R': 'red',
        'B': 'blue',
        'Y': 'yellow',
        ' ': 'lightgray'
    }

    fig, ax = plt.subplots(figsize=(8,6))

    for fila in range(9):
        for col in range(12):
            color = colores[cubo[fila][col]]
            rect = patches.Rectangle((col, 8-fila), 1, 1,
                                     edgecolor='black',
                                     facecolor=color)
            ax.add_patch(rect)

    ax.set_xlim(0,12)
    ax.set_ylim(0,9)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

dibujar_cubo(cubo_inicio)

def copiar_cubo(cubo):
    return [fila[:] for fila in cubo]

def cubo_a_texto(cubo):
    return ''.join(''.join(fila) for fila in cubo)

def es_objetivo(cubo):
    return cubo_a_texto(cubo) == cubo_a_texto(cubo_inicio)


def mover_X3R(cubo):  # arriba
    nuevo = copiar_cubo(cubo)

    for i in range(3):
        for j in range(3):
            nuevo[i][j+3] = cubo[2-j][i+3]

    temp = cubo[3][3:6]
    nuevo[3][3:6] = cubo[3][0:3]
    nuevo[3][0:3] = cubo[3][9:12]
    nuevo[3][9:12] = cubo[3][6:9]
    nuevo[3][6:9] = temp

    return nuevo


def mover_X3L(cubo):
    nuevo = copiar_cubo(cubo)

    for i in range(3):
        for j in range(3):
            nuevo[i][j+3] = cubo[j][5-i]

    temp = cubo[3][3:6]
    nuevo[3][3:6] = cubo[3][6:9]
    nuevo[3][6:9] = cubo[3][9:12]
    nuevo[3][9:12] = cubo[3][0:3]
    nuevo[3][0:3] = temp

    return nuevo


def mover_X1R(cubo):  # abajo
    nuevo = copiar_cubo(cubo)

    for i in range(3):
        for j in range(3):
            nuevo[i+6][j+3] = cubo[8-j][i+3]

    temp = cubo[5][3:6]
    nuevo[5][3:6] = cubo[5][6:9]
    nuevo[5][6:9] = cubo[5][9:12]
    nuevo[5][9:12] = cubo[5][0:3]
    nuevo[5][0:3] = temp

    return nuevo


def mover_X1L(cubo):
    nuevo = copiar_cubo(cubo)

    for i in range(3):
        for j in range(3):
            nuevo[i+6][j+3] = cubo[j+6][5-i]

    temp = cubo[5][3:6]
    nuevo[5][3:6] = cubo[5][0:3]
    nuevo[5][0:3] = cubo[5][9:12]
    nuevo[5][9:12] = cubo[5][6:9]
    nuevo[5][6:9] = temp

    return nuevo


def mover_X2R(cubo):  # mitad horizontal
    nuevo = copiar_cubo(cubo)

    temp = cubo[4][3:6]
    nuevo[4][3:6] = cubo[4][0:3]
    nuevo[4][0:3] = cubo[4][9:12]
    nuevo[4][9:12] = cubo[4][6:9]
    nuevo[4][6:9] = temp

    return nuevo


def mover_X2L(cubo):
    nuevo = copiar_cubo(cubo)

    temp = cubo[4][3:6]
    nuevo[4][3:6] = cubo[4][6:9]
    nuevo[4][6:9] = cubo[4][9:12]
    nuevo[4][9:12] = cubo[4][0:3]
    nuevo[4][0:3] = temp

    return nuevo

def mover_Y1U(cubo): return cubo
def mover_Y1D(cubo): return cubo
def mover_Y2U(cubo): return cubo
def mover_Y2D(cubo): return cubo
def mover_Y3U(cubo): return cubo
def mover_Y3D(cubo): return cubo

def mover_Z1R(cubo): return cubo
def mover_Z1L(cubo): return cubo
def mover_Z2R(cubo): return cubo
def mover_Z2L(cubo): return cubo
def mover_Z3R(cubo): return cubo
def mover_Z3L(cubo): return cubo


from collections import deque

def aplicar_movimiento(cubo, movimiento):

    if movimiento == "X1R": return mover_X1R(cubo)
    if movimiento == "X1L": return mover_X1L(cubo)
    if movimiento == "X2R": return mover_X2R(cubo)
    if movimiento == "X2L": return mover_X2L(cubo)
    if movimiento == "X3R": return mover_X3R(cubo)
    if movimiento == "X3L": return mover_X3L(cubo)

    if movimiento == "Y1U": return mover_Y1U(cubo)
    if movimiento == "Y1D": return mover_Y1D(cubo)
    if movimiento == "Y2U": return mover_Y2U(cubo)
    if movimiento == "Y2D": return mover_Y2D(cubo)
    if movimiento == "Y3U": return mover_Y3U(cubo)
    if movimiento == "Y3D": return mover_Y3D(cubo)

    if movimiento == "Z1R": return mover_Z1R(cubo)
    if movimiento == "Z1L": return mover_Z1L(cubo)
    if movimiento == "Z2R": return mover_Z2R(cubo)
    if movimiento == "Z2L": return mover_Z2L(cubo)
    if movimiento == "Z3R": return mover_Z3R(cubo)
    if movimiento == "Z3L": return mover_Z3L(cubo)

    return cubo


def obtener_movimientos(cubo):
    movimientos = [
        "X1R", "X1L",
        "X2R", "X2L",
        "X3R", "X3L",

        "Y1U", "Y1D",
        "Y2U", "Y2D",
        "Y3U", "Y3D",

        "Z1R", "Z1L",
        "Z2R", "Z2L",
        "Z3R", "Z3L"
    ]

    resultado = []

    for mov in movimientos:
        resultado.append((mov, aplicar_movimiento(cubo, mov)))

    return resultado


def bfs(cubo_inicial, limite=6):
    cola = deque()
    visitados = set()

    cola.append((cubo_inicial, []))
    visitados.add(cubo_a_texto(cubo_inicial))

    while cola:
        estado_actual, camino = cola.popleft()

        if es_objetivo(estado_actual):
            return camino

        if len(camino) >= limite:
            continue

        for nombre, nuevo in obtener_movimientos(estado_actual):
            texto = cubo_a_texto(nuevo)

            if texto not in visitados:
                visitados.add(texto)
                cola.append((nuevo, camino + [nombre]))

    return None


def inverso_mov(mov):
    inversos = {
        "X1R":"X1L", "X1L":"X1R",
        "X2R":"X2L", "X2L":"X2R",
        "X3R":"X3L", "X3L":"X3R",
        "Y1U":"Y1D", "Y1D":"Y1U",
        "Y2U":"Y2D", "Y2D":"Y2U",
        "Y3U":"Y3D", "Y3D":"Y3U",
        "Z1R":"Z1L", "Z1L":"Z1R",
        "Z2R":"Z2L", "Z2L":"Z2R",
        "Z3R":"Z3L", "Z3L":"Z3R"
    }
    return inversos[mov]


def bfs_bidireccional(inicio, objetivo, limite=14):
    frente_inicio = {cubo_a_texto(inicio): (inicio, [])}
    frente_objetivo = {cubo_a_texto(objetivo): (objetivo, [])}

    visitados_inicio = dict(frente_inicio)
    visitados_objetivo = dict(frente_objetivo)

    for _ in range(limite):
        nuevo_frente = {}

        for texto, (estado, camino) in frente_inicio.items():
            for mov, nuevo_estado in obtener_movimientos(estado):
                nuevo_texto = cubo_a_texto(nuevo_estado)

                if nuevo_texto not in visitados_inicio:
                    nuevo_camino = camino + [mov]
                    visitados_inicio[nuevo_texto] = (nuevo_estado, nuevo_camino)
                    nuevo_frente[nuevo_texto] = (nuevo_estado, nuevo_camino)

                    if nuevo_texto in visitados_objetivo:
                        camino_obj = visitados_objetivo[nuevo_texto][1]
                        return nuevo_camino + [inverso_mov(m) for m in camino_obj[::-1]]

        frente_inicio = nuevo_frente

        nuevo_frente = {}

        for texto, (estado, camino) in frente_objetivo.items():
            for mov, nuevo_estado in obtener_movimientos(estado):
                nuevo_texto = cubo_a_texto(nuevo_estado)

                if nuevo_texto not in visitados_objetivo:
                    nuevo_camino = camino + [mov]
                    visitados_objetivo[nuevo_texto] = (nuevo_estado, nuevo_camino)
                    nuevo_frente[nuevo_texto] = (nuevo_estado, nuevo_camino)

                    if nuevo_texto in visitados_inicio:
                        camino_ini = visitados_inicio[nuevo_texto][1]
                        return camino_ini + [inverso_mov(m) for m in nuevo_camino[::-1]]

        frente_objetivo = nuevo_frente

    return None



cubo_mezclado = cubo_inicio

mezcla = [
    "X3R",
    "X1R",
    "X2R",
    "X3L"
]

print("CUBO INICIAL:")
dibujar_cubo(cubo_inicio)

for mov in mezcla:
    print("Mezclando con:", mov)
    cubo_mezclado = aplicar_movimiento(cubo_mezclado, mov)
    dibujar_cubo(cubo_mezclado)

print("CUBO MEZCLADO:")
dibujar_cubo(cubo_mezclado)

solucion = bfs(cubo_mezclado, limite=8)

print("SOLUCIÓN BFS:")
print(solucion)

cubo_actual = cubo_mezclado

if solucion is not None:
    for mov in solucion:
        print("Aplicar:", mov)
        cubo_actual = aplicar_movimiento(cubo_actual, mov)
        dibujar_cubo(cubo_actual)
else:
    print("No se encontró solución con ese límite.")


def traducir_solucion(solucion):
    nombres = {
        "U": "gira la cara de ARRIBA una vez hacia la derecha",
        "U'": "gira la cara de ARRIBA una vez hacia la izquierda",
        "U2": "gira la cara de ARRIBA dos veces",

        "D": "gira la cara de ABAJO una vez hacia la derecha",
        "D'": "gira la cara de ABAJO una vez hacia la izquierda",
        "D2": "gira la cara de ABAJO dos veces",

        "L": "gira la cara IZQUIERDA una vez hacia la derecha",
        "L'": "gira la cara IZQUIERDA una vez hacia la izquierda",
        "L2": "gira la cara IZQUIERDA dos veces",

        "R": "gira la cara DERECHA una vez hacia la derecha",
        "R'": "gira la cara DERECHA una vez hacia la izquierda",
        "R2": "gira la cara DERECHA dos veces",

        "F": "gira la cara FRONTAL una vez hacia la derecha",
        "F'": "gira la cara FRONTAL una vez hacia la izquierda",
        "F2": "gira la cara FRONTAL dos veces",

        "B": "gira la cara TRASERA una vez hacia la derecha",
        "B'": "gira la cara TRASERA una vez hacia la izquierda",
        "B2": "gira la cara TRASERA dos veces"
    }

    pasos = solucion.split()

    print("SOLUCIÓN PASO A PASO:\n")

    for i, paso in enumerate(pasos, start=1):
        print(f"Paso {i}: {paso} → {nombres[paso]}")


cubo_profesor = [
[' ',' ',' ','W','W','W',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','W','W','W',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','W','W','W',' ',' ',' ',' ',' ',' '],

['B','B','B','O','O','O','G','G','G','R','R','R'],
['O','O','O','G','G','G','R','R','R','B','B','B'],
['G','G','G','R','R','R','B','B','B','O','O','O'],

[' ',' ',' ','Y','Y','Y',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','Y','Y','Y',' ',' ',' ',' ',' ',' '],
[' ',' ',' ','Y','Y','Y',' ',' ',' ',' ',' ',' ']
]

dibujar_cubo(cubo_profesor)

solucion = bfs_bidireccional(cubo_profesor, cubo_inicio, limite=10)

print("\nSOLUCIÓN BFS:")
print(solucion)

if solucion is not None:

    print("\nPASOS PARA RESOLVER:\n")

    for paso in solucion:

        if paso == "X3L":
            print("Girar la cara superior hacia la IZQUIERDA")

        elif paso == "X3R":
            print("Girar la cara superior hacia la DERECHA")

        elif paso == "X2L":
            print("Girar la capa media horizontal hacia la IZQUIERDA")

        elif paso == "X2R":
            print("Girar la capa media horizontal hacia la DERECHA")

        elif paso == "X1R":
            print("Girar la cara inferior hacia la IZQUIERDA")

        elif paso == "X1L":
            print("Girar la cara inferior hacia la DERECHA")

        elif paso == "Y1U":
            print("Girar la cara izquierda hacia ARRIBA")

        elif paso == "Y1D":
            print("Girar la cara izquierda hacia ABAJO")

        elif paso == "Y2U":
            print("Girar la capa media vertical hacia ARRIBA")

        elif paso == "Y2D":
            print("Girar la capa media vertical hacia ABAJO")

        elif paso == "Y3U":
            print("Girar la cara derecha hacia ARRIBA")

        elif paso == "Y3D":
            print("Girar la cara derecha hacia ABAJO")

        elif paso == "Z1R":
            print("Girar la cara frontal hacia la DERECHA")

        elif paso == "Z1L":
            print("Girar la cara frontal hacia la IZQUIERDA")

        elif paso == "Z2R":
            print("Girar la capa media de profundidad hacia la DERECHA")

        elif paso == "Z2L":
            print("Girar la capa media de profundidad hacia la IZQUIERDA")

        elif paso == "Z3R":
            print("Girar la cara trasera hacia la DERECHA")

        elif paso == "Z3L":
            print("Girar la cara trasera hacia la IZQUIERDA")

else:
    print("\nNo se encontró solución con ese límite.")
    print("Prueba aumentando el límite o revisa que la matriz esté bien escrita.")
