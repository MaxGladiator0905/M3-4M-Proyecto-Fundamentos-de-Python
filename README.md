Hasta este momento, me ha encantado este UCamp, y lo que he aprendido este mes me ha ayudado a mejorar mi comprensión de código, \
y todo el proyecto se basa en la idea de que, al caer, cada canica tiene dos opciones en cada nivel: moverse a la izquierda o a la derecha. 

Para simular este comportamiento, utilicé la función random.choice() para generar decisiones aleatorias en cada nivel. Cada canica comienza su recorrido desde el centro y, según las decisiones aleatorias, termina en un contenedor específico al final de los 12 niveles.

Función simular_canica(niveles)

Esta función simula el trayecto de una canica que cae a través de los niveles.

    Entrada: El número de niveles que debe atravesar la canica (en este caso, 12).
    Proceso: En cada nivel, se toma una decisión aleatoria entre moverse a la izquierda o a la derecha. Esto se hace mediante random.choice([True, False]). Dependiendo de la decisión, se suma o se resta 1 a la posición de la canica.
    Salida: La función devuelve la posición final de la canica, que puede ser negativa (izquierda del centro) o positiva (derecha del centro).

Función de: simular_maquina_galton(num_canicas, niveles)
Esta es la función principal que simula la caída de las 3000 canicas.

    Entrada: El número de canicas y la cantidad de niveles.
    Proceso:
        Se crea una lista de contenedores para contar cuántas canicas caen en cada uno.
        Para cada canica, se llama a la función simular_canica(), que determina su posición final.
        La posición final se ajusta al índice correcto en la lista de contenedores y se incrementa el contador correspondiente.
    Salida: La función devuelve la lista con los resultados finales, es decir, cuántas canicas cayeron en cada contenedor.

Función de: graficar_resultados(contenedores)

Una vez que se tienen los resultados de la simulación, esta función genera un histograma utilizando la librería matplotlib.

    Entrada: La lista de contenedores con los resultados de la simulación.
    Proceso: Se utiliza plt.bar() para graficar la cantidad de canicas en cada contenedor. Además, se configuran los nombres de los ejes y el título del gráfico para hacerlo más descriptivo.
    Salida: Un histograma que muestra la distribución de las canicas en los contenedores.


Este proyecto me permitió aplicar conocimientos importantes sobre simulación, estructuras de control y visualización de datos en Python. 
Uno de los aspectos más desafiantes fue entender cómo las decisiones aleatorias individuales pueden generar un comportamiento general que sigue un patrón definido, como lo observamos en la distribución final de las canicas.

Además, el uso de funciones como random.choice() y la librería matplotlib me ayudaron a reforzar el manejo de bibliotecas externas en Python, algo que es fundamental para proyectos más avanzados.\
Este reto me permitió mejorar mi lógica de programación y comprender cómo aplicar simulaciones para representar fenómenos reales de manera simplificada.
