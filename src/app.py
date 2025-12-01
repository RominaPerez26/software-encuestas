import os

nombre_archivo = input("Ingrese el nombre del archivo a cargar  ---->  ")

# Creo la ruta absoluta usando la librería nativa OS con el nombre del archivo ingresado.
ruta = os.path.join(os.getcwd(), "data", nombre_archivo)

# Obtener toda la información del archivo CSV y definir una función para cargar el archivo.

def leer_informacion():
    ruta = os.path.join(os.getcwd(), "data", nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as archivo:
        diccionario = {}
        lista = []
        for lineas in archivo:
            lineas = archivo.readlines()  # Una vez leído el archivo y guardado en lineas puedo inspeccionar información
            # por línea en el siguiente código
            for linea in lineas:
                linea = linea.strip()
                
                sexo, sede, cod_programa, programa, cod_facultad, facultad, cod_pais, pais_nace, cod_dep, departamento, cod_municipio_nace, nombre_municipio_nace,cod_pais_vive, pais_vive, cod_dep_vive, dep_vive,cod_mun_vive, mun_vive, credito_semestre_anterior, semestre_inicia_programa, cred_curso, cred_aprobados, promedio_semestre, promedio_programa = linea.split(",")
                
                diccionario = {
                    "SEXO": sexo, 
                    "SEDE": sede, 
                    "CÓDIGO DEL PROGRAMA": cod_programa,
                    "PROGRAMA": programa,
                    "CÓDIGO DE FACULTAD": cod_facultad,
                    "FACULTAD": facultad, 
                    "CÓDIGO DE PAÍS": cod_pais, 
                    "PAÍS DE NACIMIENTO": pais_nace,
                    "CÓDIGO DE DEPARTAMENTO": cod_dep, 
                    "DEPARTAMENTO": departamento, 
                    "CÓDIGO DE MUNICIPIO DONDE NACE": cod_municipio_nace,
                    "MUNICIPIO DONDE NACE": nombre_municipio_nace, 
                    "CODIGO DEL PAIS DONDE VIVE": cod_pais_vive,
                    "PAIS DONDE VIVE": pais_vive, 
                    "CÓDIGO DEL DEPARTAMENTO QUE VIVE": cod_dep_vive,
                    "DEPARTAMENTO DONDE VIVE": dep_vive,
                    "CODIGO DEL MUNICIPIO QUE VIVE":cod_mun_vive,
                    "MUNICIPIO DONDE VIVE": mun_vive,
                    "CRÉDITOS DEL SEMESTRE ANTERIOR": credito_semestre_anterior,
                    "EL SEMESTRE DE INICIO": semestre_inicia_programa,
                    "CRÉDITOS TOTALES DEL PROGRAMA": cred_curso, 
                    "CREDITOS APROBADOS": cred_aprobados,
                    "PROMEDIO DEL SEMESTRE": promedio_semestre,
                    "PROMEDIO DEL PROGRAMA": promedio_programa
                }
                
                lista.append(diccionario)
                
                
    return lista

leer_informacion()

###Crearé un archivo .txt para que compruebe que toda la información ha sido extraída con éxito, dado que no se puede
###visualizar en su totalidad en la consola llamado "estudiantes.txt"

def crear_archivo(ruta,contenido):
    with open(ruta, "w") as archivo:
        archivo.write(contenido + "\n")


estudiantes = leer_informacion()
contenido = "SEXO, SEDE, CODIGO DEL PROGRAMA, PROGRAMA, CODIGO DE LA FACULTAD FACULTAD, FACULTAD, CODIGO DEL PAIS, PAIS NACIMIENTO, COD_DEPTO_NACE, DEPARTAMENTO_NACE, COD_MUNI_NACE, NOMBRE_MUNI_NACE, COD_PAIS_VIVE, PAIS_VIVE, COD_DEPTO_VIVE, DEPARTAMENTO_VIVE, COD_MUNI_VIVE, NOMBRE_MUNI_VIVE, CREDITOS_ULTIM_SEMEST_MATRIC, SEMESTRE_INICIA_PROGRAMA, CRED_CURS_PROG , CRED_APROB_PROG, PROMEDIO_SEMESTRE, PROMEDIO_PROGRAMA"

for estudiante in estudiantes:
    contenido += f"\n{estudiante["SEXO"]}, {estudiante["SEDE"]}, {estudiante["CÓDIGO DEL PROGRAMA"]}, {estudiante["PROGRAMA"]}, {estudiante["CÓDIGO DE FACULTAD"]}, {estudiante["FACULTAD"]}, {estudiante["CÓDIGO DE PAÍS"]}, {estudiante["PAÍS DE NACIMIENTO"]}, {estudiante["CÓDIGO DE DEPARTAMENTO"]}, {estudiante["DEPARTAMENTO"]}, {estudiante["CÓDIGO DE MUNICIPIO DONDE NACE"]}, {estudiante["MUNICIPIO DONDE NACE"]}, {estudiante["CODIGO DEL PAIS DONDE VIVE"]}, {estudiante["PAIS DONDE VIVE"]}, {estudiante["CÓDIGO DEL DEPARTAMENTO QUE VIVE"]}, {estudiante["DEPARTAMENTO DONDE VIVE"]}, {estudiante["CODIGO DEL MUNICIPIO QUE VIVE"]}, {estudiante["MUNICIPIO DONDE VIVE"]}, {estudiante["CRÉDITOS DEL SEMESTRE ANTERIOR"]}, {estudiante["EL SEMESTRE DE INICIO"]}, {estudiante["CRÉDITOS TOTALES DEL PROGRAMA"]}, {estudiante["CREDITOS APROBADOS"]}, {estudiante["PROMEDIO DEL SEMESTRE"]}, {estudiante["PROMEDIO DEL PROGRAMA"]}\n"

crear_archivo("estudiantes.py", contenido)     



