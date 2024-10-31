import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh

def visualizar_stl(ruta_archivo_stl):
    
    stl_mesh = mesh.Mesh.from_file(ruta_archivo_stl)

    # Crear la figura
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Agregar el modelo STL a la gráfica
    ax.add_collection3d(Poly3DCollection(stl_mesh.vectors, color='cyan', alpha=0.6, edgecolor='gray'))

    # Ajustar los límites de los ejes en función de los datos del modelo
    scale = stl_mesh.points.flatten()
    ax.auto_scale_xyz(scale, scale, scale)

    # Etiquetas de los ejes
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Mostrar la gráfica
    plt.show()

# Ejemplo de uso
visualizar_stl('C:/IBERO/TERCER SEMESTRE/Programacion Avanzada/Hefesto/test pieces/pieza estructura.stl')
