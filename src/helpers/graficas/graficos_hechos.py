from graficas import crear_carpeta_graficos
from graficas import grafico_torta_region
from graficas import guardar_grafico_png

import os
import matplotlib.pyplot as plt
import time

ruta_base = os.path.join(os.getcwd(), "gráficos")

crear_carpeta_graficos(ruta_base)


hombres = [2965]
mujeres = [3584]    
print("\\n📊 Generando gráfico: Barras ...")
plt.bar(hombres, height = 2965,width= 0.35,  color='#2180CF')
plt.bar(mujeres,  height = 3584, width=0.35, color='#E6A060')
plt.ylabel('Cantidad de Estudiantes en total', fontsize=12, fontweight='bold')
plt.grid()
plt.show()



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
