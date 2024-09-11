# Supermarket Sales Analysis 

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar un conjunto de datos históricos de ventas de un supermercado con el fin de identificar patrones, realizar predicciones y proporcionar recomendaciones basadas en los hallazgos. El dataset cubre un periodo de tres meses en tres sucursales diferentes, e incluye información sobre las ventas, los clientes, los productos y los métodos de pago.

## Estructura del Proyecto
La estructura del proyecto está organizada en las siguientes carpetas y archivos:

```plaintext
├── data
│   ├── processed
│   │   └── supermarket_sales_cleaned.csv  # Datos procesados y listos para análisis
│   ├── raw
│   │   └── supermarket_sales - Sheet1.csv  # Datos sin procesar originales
├── notebooks
│   ├── 1_exploracion_limpieza.ipynb  # Exploración y limpieza de datos
│   ├── 2_eda.ipynb                   # Análisis Exploratorio de Datos (EDA)
│   └── 3_visualizaciones_recomendaciones.ipynb  # Visualizaciones y recomendaciones
├── scripts
│   └── data_processing.py  # Script para cargar, limpiar y transformar los datos
├── README.md               # Archivo de documentación
└── requirements.txt        # Dependencias y paquetes necesarios
```

# Descripción del Proyecto

## 1. Exploración y Limpieza de Datos
El notebook `1_exploracion_limpieza.ipynb` se enfoca en la carga, exploración inicial y limpieza de los datos. Este paso es crucial para asegurarnos de que los datos estén libres de duplicados y valores nulos, y que las variables de tiempo estén en el formato adecuado.

**Tareas principales:**
- Eliminación de duplicados.
- Manejo de valores nulos.
- Conversión de columnas de fecha y hora a formatos adecuados.

## 2. Análisis Exploratorio de Datos (EDA)
El notebook `2_eda.ipynb` realiza un análisis exploratorio detallado. Se exploran las distribuciones de ventas por sucursal, categorías de productos y se analizan correlaciones entre las variables para identificar relaciones significativas.

**Análisis realizados:**
- Distribución de ventas por sucursal y categoría de producto.
- Análisis de correlaciones entre variables numéricas.
- Análisis temporal de ventas por hora del día.

## 3. Visualizaciones y Recomendaciones
El notebook `3_visualizaciones_recomendaciones.ipynb` presenta las visualizaciones clave que resumen los hallazgos más importantes. Además, se proporcionan recomendaciones estratégicas basadas en los resultados del análisis.

**Visualizaciones:**
- Tendencias de ventas por sucursal y por categoría de producto.
- Comparación de patrones de compra por tipo de cliente y género.
- Rendimiento de los modelos predictivos utilizados.

**Recomendaciones:**
- Optimización de personal y stock durante horas pico.
- Fomentar la conversión de clientes a miembros mediante incentivos.
- Gestión del inventario basada en categorías de productos más vendidas.

## 4. Script de Procesamiento de Datos
El script `data_processing.py` automatiza la carga, limpieza y transformación de los datos. Esto permite un flujo de trabajo más eficiente al preparar los datos para su análisis.

**Funciones principales:**
- `load_data()`: Carga los datos desde un archivo CSV.
- `clean_data()`: Elimina duplicados y valores nulos.
- `transform_data()`: Convierte las columnas de fecha y hora a formatos adecuados.
- `save_data()`: Guarda los datos procesados en un archivo CSV.

## Requerimientos
El proyecto utiliza las siguientes bibliotecas y dependencias, listadas en el archivo `requirements.txt`. Para instalar todas las dependencias, ejecuta:

pip install -r requirements.txt


**Principales dependencias:** 

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `plotly`