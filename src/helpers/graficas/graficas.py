import matplotlib.pyplot as plt
import numpy as np


def configurar_lienzo():
    """Crea la figura principal y los 4 sub-ejes."""
    fig, axs = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle('Tablero de Control: Estadísticas Estudiantiles', fontsize=20, fontweight='bold')
    return fig, axs

def graficar_barras_genero(ax, sedes, hombres, mujeres):
    """
    Genera un diagrama de barras agrupadas (Hombres vs Mujeres).
    Parámetros:
      ax: El eje (cuadro) donde se dibujará.
      sedes: Lista de nombres de las sedes.
      hombres: Lista de cantidades de hombres.
      mujeres: Lista de cantidades de mujeres.
    """
    x = np.arange(len(sedes))
    width = 0.35
    
    rects1 = ax.bar(x - width/2, hombres, width, label='Hombres', color='blue')
    rects2 = ax.bar(x + width/2, mujeres, width, label='Mujeres', color='red')
    
    ax.set_ylabel('Cantidad de Estudiantes')
    ax.set_title('A. Distribución de Género por Sede (Estimado)')
    ax.set_xticks(x)
    ax.set_xticklabels(sedes)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.3)

def graficar_torta_region(ax, departamentos, valores):
    """
    Genera un gráfico de torta por región/departamento.
    """
    
    explode = (0, 0.2, 0.4) 
    
    ax.pie(valores, labels=departamentos, autopct='%1.1f%%', explode=explode,
           colors=['lime', 'aqua', 'purple'], startangle=45)
    ax.set_title('B. Estudiantes por Departamento')

def graficar_torta_municipios(ax, municipios, valores):
    """
    Genera un gráfico de torta para el Top 5 de municipios.
    """
    explode = (0.1, 0, 0, 0, 0) # Destacamos el primero (Rionegro)
    
    ax.pie(valores, explode=explode, labels=municipios, autopct='%1.1f%%',
           shadow=True, startangle=140, colors=plt.cm.Paired.colors)
    ax.set_title('C. Top 5 Municipios de Residencia')

def graficar_gapminder(ax, notas, edades, poblacion):
    """
    Genera un gráfico de dispersión tipo Gapminder.
    """
    colores = np.random.rand(len(notas)) 
    
    ax.scatter(notas, edades, s=poblacion, c=colores, alpha=0.6, cmap='viridis')
    
    ax.set_xlabel('Promedio de Notas')
    ax.set_ylabel('Edad Promedio')
    ax.set_title('D. Análisis Gapminder (Simulado)')
    ax.grid(True, linestyle='--', alpha=0.5)



if __name__ == "__main__":
   #Datos Gráfica A (Simulados proporcionalmente al total real: H:2965, M:3584) 
    datos_sedes = ['Sede Oriente', 'Sede Urabá', 'Sede Bajo Cauca', 'Sede Central']
    datos_hombres = [600, 500, 400, 1465]
    datos_mujeres = [800, 600, 500, 1684]

    # Datos Gráfica B (Reales: Antioquia 6307, Córdoba 140, Boyacá 15) 
    datos_deptos = ['Antioquia', 'Córdoba', 'Boyacá']
    datos_est_depto = [6307, 140, 15]

    # Datos Gráfica C (Reales Top 5) 
    datos_muni = ['Rionegro', 'Apartadó', 'Caucasia', 'La Ceja', 'Turbo']
    datos_cant_muni = [706, 558, 509, 399, 376]

    
    np.random.seed(42)
    n = 20
    datos_notas = np.random.uniform(3.0, 4.8, n)
    datos_edades = np.random.uniform(17, 25, n)
    datos_poblacion = np.random.randint(50, 500, n)

    # --- EJECUCIÓN DE FUNCIONES ---
    
    # 1. Configurar el lienzo
    fig, axs = configurar_lienzo()
    
   
    graficar_barras_genero(axs[0, 0], datos_sedes, datos_hombres, datos_mujeres)
    graficar_torta_region(axs[0, 1], datos_deptos, datos_est_depto)
    graficar_torta_municipios(axs[1, 0], datos_muni, datos_cant_muni)
    graficar_gapminder(axs[1, 1], datos_notas, datos_edades, datos_poblacion)

   
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()