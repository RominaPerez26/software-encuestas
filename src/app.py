import os
import pandas as pd

nombre_archivo = input("Ingrese el nombre del archivo a cargar  ---->  ")

# Creo la ruta absoluta usando la librería nativa OS con el nombre del archivo ingresado.
ruta = os.path.join(os.getcwd(), "data", nombre_archivo)

# Crear carpetas donde pueda almacenar la información del archivo CSV organizadamente.

csv = pd.read_csv(ruta)
print(csv)
