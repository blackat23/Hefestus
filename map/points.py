import numpy as np
from stl import mesh
fdg
def extraer_puntos_unicos(ruta_archivo_stl, ruta_salida='puntos_unicos.csv'):
    """
    Carga un archivo STL, extrae los vértices únicos en 3D y los guarda en un archivo CSV.

    Parámetros:
        ruta_archivo_stl (str): Ruta del archivo STL a cargar.
        ruta_salida (str): Ruta del archivo CSV donde se guardarán los puntos únicos.

    Retorna:
        np.ndarray: Array de puntos únicos en 3D.
    """
    # Cargar el archivo STL
    stl_mesh = mesh.Mesh.from_file(ruta_archivo_stl)

    # Extraer los vértices como coordenadas 3D y eliminar duplicados
    vertices = stl_mesh.vectors.reshape(-1, 3)
    puntos_unicos = np.unique(vertices, axis=0)

    # Mostrar los puntos únicos
    print("Puntos únicos en 3D:")
    print(puntos_unicos)

    # Guardar los puntos únicos en un archivo CSV
    np.savetxt(ruta_salida, puntos_unicos, delimiter=',', header='X,Y,Z', comments='')

    return puntos_unicos

puntos = extraer_puntos_unicos('C:/IBERO/TERCER SEMESTRE/Programacion Avanzada/Hefesto/test pieces/pieza estructura.stl')
