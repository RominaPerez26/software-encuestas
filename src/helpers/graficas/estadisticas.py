# 4. ESTADISTICAS.PY - Cálculo de indicadores

"Funciones para calcular indicadores y mostrar datos generales"


import pandas as pd


def contar_sedes(df):
    """Cuenta número de sedes únicas."""
    try:
        if 'sede' in [col.lower() for col in df.columns]:
            return df.iloc[:, 0].nunique()
        return 1
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
    
    Returns:
        dict: {Hombres, Mujeres, Otro}
    """
    try:
        cols_lower = [col.lower() for col in df.columns]
        
        # Buscar columna de género
        if 'genero' in cols_lower:
            idx = cols_lower.index('genero')
            col_genero = df.iloc[:, idx]
        elif 'gender' in cols_lower:
            idx = cols_lower.index('gender')
            col_genero = df.iloc[:, idx]
        else:
            return {'Hombres': 0, 'Mujeres': 0, 'Otro': 0}
        
        # Contar valores
        generos = col_genero.value_counts()
        
        return {
            'Hombres': generos.get('M', generos.get('Masculino', 0)),
            'Mujeres': generos.get('F', generos.get('Femenino', 0)),
            'Otro': generos.get('Otro', 0)
        }
    except:
        return {'Hombres': 0, 'Mujeres': 0, 'Otro': 0}


def estudiantes_por_region(df):
    """Calcula estudiantes por región."""
    try:
        cols_lower = [col.lower() for col in df.columns]
        if 'region' in cols_lower:
            idx = cols_lower.index('region')
            return df.iloc[:, idx].value_counts().to_dict()
        return {}
    except:
        return {}


def estudiantes_por_municipio(df):
    """Calcula estudiantes por municipio."""
    try:
        cols_lower = [col.lower() for col in df.columns]
        if 'municipio' in cols_lower:
            idx = cols_lower.index('municipio')
            return df.iloc[:, idx].value_counts().to_dict()
        return {}
    except:
        return {}


def mostrar_datos_generales(df):
    """
    Muestra todos los datos generales de registro.
    """
    print("\\n" + "="*60)
    print("📊 DATOS GENERALES DE REGISTRO")
    print("="*60)
    
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
    
    # Sección 3: Estudiantes por Región
    print("\\n🗺️  ESTUDIANTES POR REGIÓN")
    print("-" * 60)
    regiones = estudiantes_por_region(df)
    if regiones:
        for region, cantidad in sorted(regiones.items(), key=lambda x: x[1], reverse=True):
            porcentaje = (cantidad / total_estudiantes * 100) if total_estudiantes > 0 else 0
            print(f"  • {region}: {cantidad} ({porcentaje:.1f}%)")
    else:
        print("  • No hay datos de región disponibles")
    
    # Sección 4: Estudiantes por Municipio
    print("\\n🏙️  ESTUDIANTES POR MUNICIPIO (Top 10)")
    print("-" * 60)
    municipios = estudiantes_por_municipio(df)
    if municipios:
        # Mostrar top 10
        for municipio, cantidad in sorted(municipios.items(), key=lambda x: x[1], reverse=True)[:10]:
            porcentaje = (cantidad / total_estudiantes * 100) if total_estudiantes > 0 else 0
            print(f"  • {municipio}: {cantidad} ({porcentaje:.1f}%)")
    else:
        print("  • No hay datos de municipio disponibles")
    
    print("\\n" + "="*60)


with open(f"{proyecto_dir}/estadisticas.py", "w", encoding="utf-8") as f:
    f.write(estadisticas_py)

print("✓ estadisticas.py creado")