#En esta carpeta vamos a realizar el 2do punto del proyecto de aula de algoritmos y programación
# -------------------------------------------------------------
# IMPORTAR LA LIBRERÍA PANDAS
# -------------------------------------------------------------
# Esta línea permite usar todas las herramientas de pandas,
# que se utilizan para leer archivos, analizar datos y hacer conteos.
import pandas as pd
from pathlib import Path 
from app import leer_informacion
import os 

# -------------------------------------------------------------
# DEFINICIÓN DE LA FUNCIÓN PRINCIPAL
# -------------------------------------------------------------
# Se crea una función para que todo el proceso quede organizado,
# reutilizable y fácil de ejecutar cuando se necesite.
def datos_generales_registro():

    # ---------------------------------------------------------
    # LECTURA DEL ARCHIVO CSV
    # ---------------------------------------------------------
    # pd.read_csv() sirve para leer el archivo de la base de datos.
    # "DataBase.csv" es el archivo donde están almacenados los estudiantes.
    # Todo el contenido se guarda dentro de la variable df como una tabla.
    
    # LECTURA DEL ARCHIVO CSV
    # ---------------------------------------------------------
    # Usamos la variable 'file_path' que contiene la ruta correcta.
    with open("Sedes.txt","r", encoding= "UTF-8") as archivo:
        for lineas in archivo:
            df = archivo.readlines()
            # ---------------------------------------------------------
            # CÁLCULO DE LA CANTIDAD TOTAL DE ESTUDIANTES
            # ---------------------------------------------------------
            # len(df) cuenta cuántas filas tiene la tabla.
            # Como cada fila representa un estudiante, este valor
            # corresponde al total de estudiantes registrados.
            total_estudiantes = len(df)

            # ---------------------------------------------------------
            # CÁLCULO DEL NÚMERO DE SEDES
            # ---------------------------------------------------------
            # df['SEDE'] selecciona únicamente la columna donde están las sedes.
            # nunique() cuenta cuántos valores diferentes hay en esa columna.git
            # Esto permite saber cuántas sedes existen sin contar las repetidas.
            numero_sedes = df['SEDE'].nunique()

            # ---------------------------------------------------------
            # CÁLCULO DEL NÚMERO DE PROGRAMAS ACADÉMICOS
            # ---------------------------------------------------------
            # df['PROGRAMA'] selecciona la columna donde están los programas.
            # nunique() cuenta cuántos programas diferentes existen.
            numero_programas = df['PROGRAMA'].nunique()

            # ---------------------------------------------------------
            # NORMALIZACIÓN DE LA COLUMNA DE GÉNERO
            # ---------------------------------------------------------
            # Se convierte toda la columna de género a texto para evitar errores.
            df['SEXO'] = df['SEXO'].astype(str)

            # Se pasan todos los textos a minúscula para evitar diferencias
            # entre palabras como "Hombre", "hombre", "HOMBRE".
            df['SEXO'] = df['SEXO'].str.lower()

            # Se eliminan los espacios en blanco antes o después de los textos.
            df['SEXO'] = df['SEXO'].str.strip()

            # Se reemplazan diferentes formas de escribir el género
            # para que todo quede estandarizado.
            df['SEXO'] = df['SEXO'].replace({
                'm': 'hombres',
                'masculino': 'hombres',
                'f': 'mujeres',
                'femenino': 'mujeres'
            })

            # Todo valor que NO sea "hombres" o "mujeres" se clasifica como "otro".
            df.loc[~df['SEXO'].isin(['hombres', 'mujeres']), 'SEXO'] = 'otro'

            # ---------------------------------------------------------
            # CONTEO DE ESTUDIANTES POR GÉNERO
            # ---------------------------------------------------------
            # value_counts() cuenta cuántas veces aparece cada género.
            conteo_genero = df['SEXO'].value_counts()

            # ---------------------------------------------------------
            # PRESENTACIÓN DE RESULTADOS EN PANTALLA
            # ---------------------------------------------------------
            print("==============================================")
            print("      DATOS GENERALES DE REGISTRO")
            print("==============================================")

            # Se imprimen los valores calculados anteriormente.
            print(f"Cantidad total de estudiantes: {total_estudiantes}")
            print(f"Número de sedes: {numero_sedes}")
            print(f"Número de programas académicos: {numero_programas}")

            print("\nCantidad de registros por género:")

            # Se recorre el conteo de géneros para mostrar cada uno con su cantidad.
            for genero, cantidad in conteo_genero.items():
                print(f"{genero.capitalize()}: {cantidad}")

        # -------------------------------------------------------------
        # LLAMADO A LA FUNCIÓN
        # -------------------------------------------------------------
        # Esta línea ejecuta la función para que todo el proceso se realice.

print(datos_generales_registro())
