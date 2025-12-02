# 2. PROCESAMIENTO.PY - Manejo de datos CSV
import os
import pandas as pd
import csv
from pathlib import Path


def validar_archivo_csv(ruta_archivo):
    """
    Valida que el archivo CSV exista y tenga formato correcto.
    
    Args:
        ruta_archivo (str): Ruta del archivo CSV
        
    Returns:
        bool: True si es válido, False en caso contrario
    """
    try:
        # Verificar existencia
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"❌ Archivo no encontrado: {ruta_archivo}")
        
        # Verificar extensión
        if not ruta_archivo.lower().endswith('.csv'):
            raise ValueError(f"❌ Archivo no es CSV: {ruta_archivo}")
        
        # Intentar leer primeras líneas
        df = pd.read_csv(ruta_archivo, nrows=5)
        
        if df.empty:
            raise ValueError("❌ Archivo CSV está vacío")
        
        print(f"✓ CSV válido. Columnas encontradas: {len(df.columns)}")
        return True
        
    except pd.errors.EmptyDataError:
        print("❌ Archivo CSV está vacío")
        return False
    except pd.errors.ParserError as e:
        print(f"❌ Error al parsear CSV: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False


def cargar_csv_seguro(ruta_archivo):
    """
    Carga CSV con manejo robusto de errores y encoding múltiple.
    
    Args:
        ruta_archivo (str): Ruta del archivo CSV
        
    Returns:
        pd.DataFrame: DataFrame con los datos, o None si hay error
    """
    try:
        if not validar_archivo_csv(ruta_archivo):
            return None
        
        # Intentar con UTF-8
        try:
            df = pd.read_csv(ruta_archivo, encoding='utf-8')
            print(f"✓ Cargado: {len(df)} registros (encoding UTF-8)")
            return df
        except UnicodeDecodeError:
            print("⚠️  Probando encoding latin-1...")
            df = pd.read_csv(ruta_archivo, encoding='latin-1')
            print(f"✓ Cargado: {len(df)} registros (encoding latin-1)")
            return df
            
    except Exception as e:
        print(f"❌ Error al cargar CSV: {str(e)}")
        return None


def appendear_registros(df_principal, df_nueva):
    """
    Appendea (agrega) nuevos registros al DataFrame principal.
    
    Args:
        df_principal (pd.DataFrame): DataFrame principal
        df_nueva (pd.DataFrame): DataFrame con nuevos registros
        
    Returns:
        pd.DataFrame: DataFrame combinado
    """
    try:
        # Verificar que tengan las mismas columnas
        if list(df_principal.columns) != list(df_nueva.columns):
            print("⚠️  Las columnas no coinciden exactamente")
            print(f"Principal: {list(df_principal.columns)}")
            print(f"Nueva: {list(df_nueva.columns)}")
        
        # Appendear
        df_combinado = pd.concat([df_principal, df_nueva], ignore_index=True)
        
        # Eliminar duplicados si existen
        filas_antes = len(df_combinado)
        df_combinado = df_combinado.drop_duplicates()
        filas_despues = len(df_combinado)
        
        duplicados = filas_antes - filas_despues
        if duplicados > 0:
            print(f"⚠️  Se removieron {duplicados} registros duplicados")
        
        print(f"✓ Registros appendeados: {len(df_nueva)}")
        print(f"✓ Total en base de datos: {len(df_combinado)}")
        
        return df_combinado
        
    except Exception as e:
        print(f"❌ Error al appendear: {str(e)}")
        return df_principal


def guardar_csv(df, ruta_destino):
    """
    Guarda DataFrame como archivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame a guardar
        ruta_destino (str): Ruta donde guardar
        
    Returns:
        bool: True si se guardó correctamente
    """
    try:
        # Crear directorio si no existe
        directorio = os.path.dirname(ruta_destino)
        os.makedirs(directorio, exist_ok=True)
        
        # Guardar
        df.to_csv(ruta_destino, index=False, encoding='utf-8')
        print(f"✓ Guardado: {ruta_destino}")
        print(f"✓ Registros guardados: {len(df)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al guardar CSV: {str(e)}")
        return False


def limpiar_datos(df):
    """
    Limpia y normaliza datos del DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame a limpiar
        
    Returns:
        pd.DataFrame: DataFrame limpiado
    """
    try:
        # Eliminar espacios en blanco en columnas de texto
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()
        
        # Eliminar filas completamente vacías
        df = df.dropna(how='all')
        
        print(f"✓ Datos limpiados. Registros resultantes: {len(df)}")
        return df
        
    except Exception as e:
        print(f"❌ Error al limpiar datos: {str(e)}")
        return df


with open(f"{proyecto_dir}/procesamiento.py", "w", encoding="utf-8") as f:
    f.write(procesamiento_py)

print("✓ procesamiento.py creado")