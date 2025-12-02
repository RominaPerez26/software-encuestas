# 4. ESTADISTICAS.PY - Cálculo de indicadores

"Funciones para calcular indicadores y mostrar datos generales"


import pandas as pd
import os


def contar_sedes(df):
    """Cuenta número de sedes únicas."""
    try:
        # Buscar la columna que contiene 'sede'
        columnas = [col.lower() for col in df.columns]

        for col in df.columns:
            if "sede" in col.lower():
                return df[col].nunique()

        return 1  # Si no encuentra columna con 'sede'
    
    except:
        return 0



def contar_programas(df):
    """Cuenta número de programas únicos."""
    try:
        # Buscar columna de programa
        cols_lower = [col.lower() for col in df.columns]
        if 'programa' in cols_lower:
            idx = cols_lower.index('programa')
            return df.iloc[:, idx].nunique()
        return 1
    except:
        return 0


def contar_estudiantes(df):
    """Cuenta total de estudiantes."""
    return len(df)

def distribucion_genero(df):
    """
    Calcula distribución por género.
    Returns: dict con Hombres, Mujeres y Otro
    """
    try:
        cols_lower = [col.lower() for col in df.columns]

        # Buscar columna que contenga 'sexo', 'genero', o 'gender'
        if 'sexo' in cols_lower:
            idx = cols_lower.index('sexo')
        elif 'genero' in cols_lower:
            idx = cols_lower.index('genero')
        elif 'gender' in cols_lower:
            idx = cols_lower.index('gender')
        else:
            return {'Hombres': 0, 'Mujeres': 0, 'Otro': 0}

        col_genero = df.iloc[:, idx].astype(str).str.upper().str.strip()

        col_genero = col_genero.replace({
            'MASC': 'H',
            'FEME': 'M',
            'M': 'H',
            'F': 'M',
            'MASCULINO': 'H',
            'FEMENINO': 'M'
        })

        conteo = col_genero.value_counts()

        return {
            'Hombres': conteo.get('H', 0),
            'Mujeres': conteo.get('M', 0),
            'Otro': conteo.sum() - conteo.get('H', 0) - conteo.get('M', 0)
        }

    except:
        return {'Hombres': 0, 'Mujeres': 0, 'Otro': 0}

def estudiantes_por_region(df):
    """Cuenta el número de estudiantes por departamento de residencia."""
    df['DEPARTAMENTO_VIVE'] = df['DEPARTAMENTO_VIVE'].astype(str).str.strip().str.upper()
    return df.groupby('DEPARTAMENTO_VIVE').size().sort_values(ascending=False)


def estudiantes_por_municipio(df):
    """Cuenta el número de estudiantes por municipio de residencia."""
    df['NOMBRE_MUNI_VIVE'] = df['NOMBRE_MUNI_VIVE'].astype(str).str.strip().str.upper()
    return df.groupby('NOMBRE_MUNI_VIVE').size().sort_values(ascending=False)



def mostrar_datos_generales(df):
    """
    Muestra todos los datos generales de registro.
    """
    print("\\n" + "="*60)
    print("📊 DATOS GENERALES DE REGISTRO")
    print("="*60)
    
    def estudiantes_por_region(df):
        """Cuenta el número de estudiantes por departamento de residencia."""
        df['DEPARTAMENTO_VIVE'] = df['DEPARTAMENTO_VIVE'].astype(str).str.strip().str.upper()
        return df.groupby('DEPARTAMENTO_VIVE').size().sort_values(ascending=False)
    def estudiantes_por_municipio(df):
        """Cuenta el número de estudiantes por municipio de residencia."""
        df['NOMBRE_MUNI_VIVE'] = df['NOMBRE_MUNI_VIVE'].astype(str).str.strip().str.upper()
        return df.groupby('NOMBRE_MUNI_VIVE').size().sort_values(ascending=False)
    
    # Sección 1: Resumen General
    print("\\n📈 RESUMEN GENERAL")
    print("-" * 60)
    sedes = contar_sedes(df)
    programas = contar_programas(df)
    total_estudiantes = contar_estudiantes(df)
    
    print(f"  • Número de Sedes: {sedes}")
    print(f"  • Número de Programas Académicos: {programas}")
    print(f"  • Cantidad Total de Estudiantes: {total_estudiantes}")
    
    # Sección 2: Distribución por Género
    print("\\n👥 DISTRIBUCIÓN POR GÉNERO")
    print("-" * 60)
    genero = distribucion_genero(df)
    
    for clave, valor in genero.items():
        porcentaje = (valor / total_estudiantes * 100) if total_estudiantes > 0 else 0
        print(f"  • {clave}: {valor} ({porcentaje:.1f}%)")
    
    import pandas as pd
    import os

    # --- 1. CARGA DE DATOS ---
    ruta = os.path.join(os.getcwd(), "data", "database.csv")
    df = pd.read_csv(ruta)

    # --- 2. LIMPIEZA INICIAL DE NOMBRES DE COLUMNA (Importante contra espacios) ---
    df.columns = df.columns.str.strip()

    # --- 3. LISTA CORRECTA DE COLUMNAS A LIMPIAR (Con comas) ---
    columnas_ubicacion = [
        'SEDE', 
        'DEPARTAMENTO_NACE', 
        'NOMBRE_MUNI_NACE', 
        'DEPARTAMENTO_VIVE', 
        'NOMBRE_MUNI_VIVE'
    ]

    # --- 4. LIMPIEZA GLOBAL DE LOS DATOS DE UBICACIÓN ---
    for col in columnas_ubicacion:
        # Asegurarse de que la columna exista antes de intentar limpiarla
        if col in df.columns:
            # 1. Manejar valores nulos (NaN)
            df[col] = df[col].fillna('')
            
            # 2. Aplicar limpieza (quitar espacios y poner en mayúsculas)
            df[col] = df[col].astype(str).str.strip().str.upper()
        else:
            print(f"Advertencia: La columna '{col}' no se encontró en el DataFrame. Saltando.")


    # --- 5. FUNCIONES PARA CONTEO (Ahora deberían funcionar) ---

    def estudiantes_por_municipio(df):
        """Cuenta el número de estudiantes por municipio de residencia (ya limpios)."""
        # Usamos NOMBRE_MUNI_VIVE
        conteo = df.groupby('NOMBRE_MUNI_VIVE').size().sort_values(ascending=False)
        # Filtramos la cadena vacía que usamos para rellenar nulos
        return conteo[conteo.index != ''] 

    def estudiantes_por_region(df):
        """Cuenta el número de estudiantes por departamento de residencia (ya limpios)."""
        # Usamos DEPARTAMENTO_VIVE
        conteo = df.groupby('DEPARTAMENTO_VIVE').size().sort_values(ascending=False)
        # Filtramos la cadena vacía que usamos para rellenar nulos
        return conteo[conteo.index != '']

    # --- 6. PRUEBA FINAL ---
    print("\n--- Resultados de Conteo ---\n")
    print("Top 5 Municipios de Residencia:")
    print(estudiantes_por_municipio(df).head())

    print("\nTop 3 Departamentos de Residencia:")
    print(estudiantes_por_region(df).head(3))
    
    