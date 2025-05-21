# Aplicación CLI de Análisis de Datos

Esta aplicación permite procesar y analizar archivos de texto (.txt) y archivos separados por comas (.csv) a través de una interfaz de línea de comandos.

## Requisitos

- Python 3.6 o superior
- Bibliotecas necesarias:
  - matplotlib

Para instalar las dependencias necesarias, ejecuta:
```
pip install matplotlib numpy
```

## Estructura del Proyecto

- `main.py`: Archivo principal que contiene el menú de la aplicación.
- `procesador_texto.py`: Módulo para procesar archivos de texto (.txt).
- `procesador_csv.py`: Módulo para procesar archivos CSV (.csv).

## Funcionalidades

### Menú Principal

1. **Listar archivos**: Muestra los archivos disponibles en la ruta actual o en una ruta específica.
2. **Procesar archivo de texto (.txt)**: Abre el submenú para archivos de texto.
3. **Procesar archivo CSV (.csv)**: Abre el submenú para archivos CSV.
4. **Salir**: Cierra la aplicación.

### Procesamiento de Archivos de Texto (.txt)

1. **Contar número de palabras y caracteres**: Cuenta el número de palabras, caracteres con espacios y caracteres sin espacios en el archivo.
2. **Reemplazar una palabra por otra**: Permite al usuario reemplazar todas las ocurrencias de una palabra por otra y guardar el resultado en un nuevo archivo.
3. **Histograma de ocurrencia de las vocales**: Genera un histograma que muestra la frecuencia de cada vocal en el archivo.

### Procesamiento de Archivos CSV (.csv)

1. **Mostrar las primeras 15 filas**: Muestra las primeras 15 filas del archivo CSV para una vista previa rápida.
2. **Calcular estadísticas de una columna**: Permite al usuario seleccionar una columna y calcula estadísticas como número de datos, promedio, mediana, valor mínimo y valor máximo.
3. **Graficar una columna**: Permite al usuario seleccionar una columna y generar diferentes tipos de gráficas (líneas, barras, histograma).

## Cómo Usar

1. Ejecuta el programa principal:
```
python main.py
```

2. Sigue las instrucciones en pantalla para navegar por los menús y seleccionar las opciones deseadas.

3. Para procesar archivos, asegúrate de tener los archivos en la misma carpeta que el programa o especifica la ruta correcta cuando se te solicite.

## Ejemplos de Archivos

### Archivos de Texto (.txt)
Puedes usar cualquier archivo de texto plano para las funcionalidades de procesamiento de texto.

### Archivos CSV (.csv)
Para las funcionalidades de procesamiento CSV, utiliza archivos de datos reales de fuentes como:
- Registros de calidad del aire
- Estadísticas de salud pública
- Datos de eficiencia de motores
- Registros de consumo de combustible

## Notas Adicionales

- Las gráficas generadas se guardan automáticamente en la carpeta de trabajo.
- Los archivos modificados por la función de reemplazo se guardan con el prefijo "modificado_" seguido del nombre original.
