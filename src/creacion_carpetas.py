from app import leer_informacion 
from app import crear_archivo
import os 

contenido = leer_informacion()
sedes = ""
facultad = ""
programa_academico = ""

for diccionario in contenido:
    sedes += diccionario["SEDE"] + "\n"   
    facultad += diccionario["FACULTAD"] + "\n"
    programa_academico += diccionario["PROGRAMA"] + "\n"
     

crear_archivo("Sedes.txt", sedes)
crear_archivo("Facultades.txt", facultad)
crear_archivo("Programas_académicos.txt", programa_academico)

