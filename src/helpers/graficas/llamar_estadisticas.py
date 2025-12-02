from estadisticas import contar_sedes
from estadisticas import contar_programas
from estadisticas import contar_estudiantes
from estadisticas import distribucion_genero
from estadisticas import estudiantes_por_region
from estadisticas import estudiantes_por_municipio
from estadisticas import mostrar_datos_generales
import os 
import pandas as pd

nombre_archivo = input("Ingrese el nombre del archivo a cargar  ---->  ")

# Creo la ruta absoluta usando la librería nativa OS con el nombre del archivo ingresado.
ruta = os.path.join(os.getcwd(), "data", nombre_archivo)
df = pd.read_csv(ruta)

contar_sedes(df)
contar_programas(df)
contar_estudiantes(df)
distribucion_genero(df)
estudiantes_por_region(df)
estudiantes_por_municipio(df)
mostrar_datos_generales(df)

print("estudiantes por region------>")
print(f"{estudiantes_por_region(df)}")
print("estudiantes por municipio------>")
print(f"{estudiantes_por_municipio(df)}")
