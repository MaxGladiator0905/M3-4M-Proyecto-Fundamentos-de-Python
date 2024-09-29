import random
import matplotlib.pyplot as plt

# Función para simular el recorrido de una canica
def simular_canica(niveles):
    posicion = 0  # Inicia en el centro (posición 0)
    for _ in range(niveles):
        # Decisión aleatoria: -1 para izquierda, +1 para derecha
        if random.choice([True, False]):
            posicion += 1  # Derecha
        else:
            posicion -= 1  # Izquierda
    return posicion

# Función para realizar la simulación de todas las canicas
def simular_maquina_galton(num_canicas, niveles):
    contenedores = [0] * (niveles * 2 + 1)  # Inicializa los contenedores
    for _ in range(num_canicas):
        posicion_final = simular_canica(niveles)
        contenedores[posicion_final + niveles] += 1  # Ajusta el índice
    return contenedores

# Función para graficar el histograma
def graficar_resultados(contenedores):
    plt.bar(range(len(contenedores)), contenedores)
    plt.xlabel('Contenedores')
    plt.ylabel('Número de Canicas')
    plt.title('Simulación de la Máquina de Galton por Máximo E. López De Nava Hernández')
    plt.show()

# Parámetros de la simulación
num_canicas = 3000
niveles = 12

# Realizar la simulación
resultados = simular_maquina_galton(num_canicas, niveles)

# Graficar los resultados
graficar_resultados(resultados)