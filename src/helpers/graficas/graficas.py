# 5. GRAFICOS.PY - Generación de visualizaciones
#Funciones para generar gráficos con matplotlib

import os
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd


def crear_carpeta_graficos(ruta_base):
    """
    Crea carpeta 'graficos' dentro de ruta_base.
    
    Args:
        ruta_base (str): Ruta base
        
    Returns:
        str: Ruta a la carpeta de gráficos
    """
    try:
        ruta_graficos = os.path.join(ruta_base, 'graficos')
        os.makedirs(ruta_graficos, exist_ok=True)
        print(f"✓ Carpeta de gráficos: {ruta_graficos}")
        return ruta_graficos
    except Exception as e:
        print(f"❌ Error al crear carpeta: {str(e)}")
        return None


def guardar_grafico_png(fig, nombre_archivo, ruta_graficos):
    """
    Guarda gráfico matplotlib como PNG.
    
    Args:
        fig: Objeto figure de matplotlib
        nombre_archivo: Nombre sin extensión
        ruta_graficos: Ruta donde guardar
        
    Returns:
        str: Ruta del archivo guardado
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_completo = f"{nombre_archivo}_{timestamp}.png"
        ruta_completa = os.path.join(ruta_graficos, nombre_completo)
        
        fig.savefig(ruta_completa, dpi=300, bbox_inches='tight')
        print(f"✓ Gráfico guardado: {ruta_completa}")
        
        plt.close(fig)
        return ruta_completa
        
    except Exception as e:
        print(f"❌ Error al guardar gráfico: {str(e)}")
        return None


def grafico_barras_genero_sede(df, ruta_graficos):
    """
    Genera gráfico de barras: Hombres vs Mujeres por sede.
    """
    try:
        print("\\n📊 Generando gráfico: Barras Género por Sede...")
        
        fig, c
        
        # Datos de ejemplo
        sedes = ['Sede A', 'Sede B', 'Sede C']
        hombres = [150, 120, 180]
        mujeres = [140, 130, 160]
        
        x = range(len(sedes))
        width = 0.35
        
        ax.bar([i - width/2 for i in x], hombres, width, label='Hombres', color='#2180CF')
        ax.bar([i + width/2 for i in x], mujeres, width, label='Mujeres', color='#E6A060')
        
        ax.set_xlabel('Sede', fontsize=12, fontweight='bold')
        ax.set_ylabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
        ax.set_title('Distribución de Estudiantes por Género y Sede', fontsize=14, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(sedes)
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
        
        guardar_grafico_png(fig, "01_barras_genero_sede", ruta_graficos)
        plt.show()
        
    except Exception as e:
        print(f"❌ Error en gráfico barras: {str(e)}")


def grafico_torta_region(df, ruta_graficos):
    """
    Genera gráfico de torta: Porcentaje de estudiantes por región.
    """
    try:
        print("\\n📊 Generando gráfico: Torta Regiones...")
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Datos de ejemplo
        regiones = ['Región Central', 'Región Oriental', 'Región Occidental', 'Región Atlántica']
        porcentajes = [35, 25, 20, 20]
        colores = ['#208074', '#32B8C6', '#E68164', '#D4B76A']
        
        ax.pie(porcentajes, labels=regiones, autopct='%1.1f%%', colors=colores, startangle=90)
        ax.set_title('Distribución de Estudiantes por Región', fontsize=14, fontweight='bold')
        
        guardar_grafico_png(fig, "02_torta_region", ruta_graficos)
        plt.show()
        
    except Exception as e:
        print(f"❌ Error en gráfico torta región: {str(e)}")


def grafico_torta_municipio(df, ruta_graficos):
    """
    Genera gráfico de torta: Porcentaje de estudiantes por municipio.
    """
    try:
        print("\\n📊 Generando gráfico: Torta Municipios...")
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Datos de ejemplo - Top 10
        municipios = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 
                     'Bucaramanga', 'Cúcuta', 'Manizales', 'Ibagué', 'Otros']
        porcentajes = [20, 15, 10, 8, 7, 6, 5, 4, 3, 22]
        colores = plt.cm.Set3(range(len(municipios)))
        
        ax.pie(porcentajes, labels=municipios, autopct='%1.1f%%', colors=colores, startangle=90)
        ax.set_title('Distribución de Estudiantes por Municipio', fontsize=14, fontweight='bold')
        
        guardar_grafico_png(fig, "03_torta_municipio", ruta_graficos)
        plt.show()
        
    except Exception as e:
        print(f"❌ Error en gráfico torta municipio: {str(e)}")


def grafico_gapminder_inspirado(df, ruta_graficos):
    """
    Genera gráfico inspirado en Gapminder (scatter plot múltiples variables).
    """
    try:
        print("\\n📊 Generando gráfico: Gapminder Inspirado...")
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Datos de ejemplo
        sedes = ['Sede A', 'Sede B', 'Sede C', 'Sede D', 'Sede E']
        estudiantes = [400, 350, 520, 480, 420]
        promedio = [3.5, 3.8, 3.2, 3.6, 3.4]
        tamaño = [s*2 for s in estudiantes]
        colores = ['#208074', '#32B8C6', '#E68164', '#D4B76A', '#A67C52']
        
        for i, sede in enumerate(sedes):
            ax.scatter(estudiantes[i], promedio[i], s=tamaño[i], alpha=0.6, 
                      c=colores[i], label=sede, edgecolors='black', linewidth=1)
        
        ax.set_xlabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
        ax.set_ylabel('Promedio Académico', fontsize=12, fontweight='bold')
        ax.set_title('Análisis Multivariable: Estudiantes vs Desempeño Académico', 
                    fontsize=14, fontweight='bold')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)
        
        guardar_grafico_png(fig, "04_gapminder_inspirado", ruta_graficos)
        plt.show()
        
    except Exception as e:
        print(f"❌ Error en gráfico Gapminder: {str(e)}")


def generar_todos_graficos(df, ruta_graficos):
    """
    Genera todos los gráficos requeridos.
    """
    print("\\n📈 === GENERANDO GRÁFICOS ===\\n")
    
    if not ruta_graficos:
        print("❌ No hay ruta de gráficos válida")
        return
    
    try:
        grafico_barras_genero_sede(df, ruta_graficos)
        grafico_torta_region(df, ruta_graficos)
        grafico_torta_municipio(df, ruta_graficos)
        grafico_gapminder_inspirado(df, ruta_graficos)
        
        print("\\n✅ Todos los gráficos generados exitosamente")
        print(f"📁 Gráficos guardados en: {ruta_graficos}")
        
    except Exception as e:
        print(f"❌ Error general al generar gráficos: {str(e)}")

