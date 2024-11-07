import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh

def extraer_caras_por_capa(ruta_archivo_stl, altura_capa=1.0):
    """
    Carga un archivo STL y divide sus caras en capas según su coordenada Z.

    Parámetros:
        ruta_archivo_stl (str): Ruta del archivo STL a cargar.
        altura_capa (float): Altura de cada capa en la división vertical.

    Retorna:
        dict: Diccionario donde cada clave es el número de capa y el valor son las caras en esa capa.
    """
    # Cargar el archivo STL
    stl_mesh = mesh.Mesh.from_file(ruta_archivo_stl)

    capas = {}
    for i, vector in enumerate(stl_mesh.vectors):
        # Obtener el rango de Z para la cara (mínimo y máximo Z)
        z_min, z_max = np.min(vector[:, 2]), np.max(vector[:, 2])
        
        # Identificar todas las capas en las que esta cara podría estar presente
        capa_inicial = int(z_min // altura_capa)
        capa_final = int(z_max // altura_capa)

        # Agregar la cara a cada capa correspondiente en el rango
        for capa in range(capa_inicial, capa_final + 1):
            if capa not in capas:
                capas[capa] = []
            capas[capa].append(vector)

    return capas

# Paso 1: Dividir las caras en capas
capas = extraer_caras_por_capa('C:/IBERO/TERCER SEMESTRE/Programacion Avanzada/Hefesto/test pieces/pieza estructura.stl', altura_capa=1.0)

# Paso 2: Configurar la figura de la visualización
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Visualizar cada capa automáticamente
for numero_capa, caras_capa in sorted(capas.items()):
    print(f"Visualizando la capa {numero_capa} con {len(caras_capa)} caras")

    # Limpiar la figura y volver a agregar las caras de la capa actual
    ax.clear()
    ax.add_collection3d(Poly3DCollection(caras_capa, color='cyan', alpha=0.6, edgecolor='gray'))

    # Etiquetas y título
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Capa {numero_capa}")

    # Ajustar los límites de los ejes
    all_points = np.concatenate(caras_capa)
    ax.auto_scale_xyz(all_points[:, 0], all_points[:, 1], all_points[:, 2])

    plt.pause(1)  # Pausa de 1 segundo antes de mostrar la siguiente capa

plt.close()  # Cerrar la figura después de mostrar todas las capas
