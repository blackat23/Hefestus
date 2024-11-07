import numpy as np

def dividir_en_capas(puntos, altura_capa=1.0):
    """
    Divide los puntos en capas según su coordenada Z.

    Parámetros:
        puntos (np.ndarray): Array de puntos únicos en 3D (X, Y, Z).
        altura_capa (float): Altura de cada capa en la división vertical.

    Retorna:
        dict: Diccionario donde cada clave es el número de capa y el valor son los puntos en esa capa.
    """
    capas = {}
    # Ordena los puntos por la coordenada Z
    puntos_ordenados = puntos[np.argsort(puntos[:, 2])]

    # Agrupa los puntos en capas según la altura de la capa
    for punto in puntos_ordenados:
        capa = int(punto[2] // altura_capa)  # Determina la capa correspondiente al punto
        if capa not in capas:
            capas[capa] = []
        capas[capa].append(punto)

    # Convierte las listas de puntos en arrays para cada capa
    for capa in capas:
        capas[capa] = np.array(capas[capa])

    return capas

# Ejemplo de uso
capas = dividir_en_capas(puntos, altura_capa=1.0)

# Imprimir los puntos de la primera capa como ejemplo
print("Puntos en la primera capa:")
print(capas[0])
