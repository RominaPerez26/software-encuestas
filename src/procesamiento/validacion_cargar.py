from nuevos_registros import validar_archivo_csv
from nuevos_registros import limpiar_datos
import pandas as pd
import os

### LLAMAMOS LAS FUNCIONES CREADAS EN nuevos_registros.py para ver que funcionen



nombre_archivo = input("Ingrese el nombre del archivo a cargar  ---->  ")

# Creo la ruta absoluta usando la librería nativa OS con el nombre del archivo ingresado.
ruta = os.path.join(os.getcwd(), "data", nombre_archivo)
df = pd.read_csv(ruta, nrows=6550)
print(validar_archivo_csv(ruta))
print(limpiar_datos(df))