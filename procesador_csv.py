
import os # Para trabajar con archivos y rutas
import csv # biblioteca csv 
import matplotlib.pyplot as plt # Para crear gráficos como histogramas

def mostrar_primeras_filas(nombre_archivo, num_filas=15):
    """
    Muestra las primeras filas de un archivo CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV a procesar.
        num_filas (int): Número de filas a mostrar (por defecto, 15).
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(nombre_archivo):           #verifica si existe en el sistema
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
            input("\nPresione Enter para continuar...")
            return
        
        # Verificar si el archivo tiene extensión .csv
        if not nombre_archivo.lower().endswith('.csv'): # verifica si termina con .csv
            print(f"Error: El archivo '{nombre_archivo}' no es un archivo CSV.")
            input("\nPresione Enter para continuar...")
            return
        
        # Leer y mostrar las primeras filas
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            
            # Obtener encabezados
            encabezados = next(lector_csv)
            
            print("\n=== Primeras filas del archivo CSV ===")
            print(f"Encabezados: {', '.join(encabezados)}")
            print("\nDatos:")
            
            # Mostrar las 15 primeras filas
            contador = 0
            for fila in lector_csv:
                if contador < num_filas:
                    print(f"{contador + 1}: {', '.join(fila)}")
                    contador += 1
                else:
                    break
        
        input("\nPresione Enter para continuar...")
    
    except Exception as e:

        input("\nPresione Enter para continuar...")

def calcular_estadisticas(nombre_archivo):
    """
    Calcula estadísticas de una columna seleccionada por el usuario.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV a procesar.
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(nombre_archivo):
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
            input("\nPresione Enter para continuar...")
            return
        
        # Verificar si el archivo tiene extensión .csv
        if not nombre_archivo.lower().endswith('.csv'):
            print(f"Error: El archivo '{nombre_archivo}' no es un archivo CSV.")
            input("\nPresione Enter para continuar...")
            return
        
        # Leer el archivo y obtener encabezados
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            encabezados = next(lector_csv)
            
            # Mostrar opciones de columnas
            print("\n=== Columnas disponibles ===")
            for i, encabezado in enumerate(encabezados):
                print(f"{i+1}. {encabezado}")
            
            # Solicitar selección de columna
            opcion = input("\nSeleccione el número de columna para calcular estadísticas: ")
            try:
                indice_columna = int(opcion) - 1
                if indice_columna < 0 or indice_columna >= len(encabezados):
                    print("Selección de columna no válida.")
                    input("\nPresione Enter para continuar...")
                    return
            except ValueError:
                print("Entrada no válida. Debe ingresar un número.")
                input("\nPresione Enter para continuar...")
                return
            
            # Recolectar datos de la columna seleccionada
            archivo.seek(0)  # Volver al inicio del archivo
            next(lector_csv)  # Saltar encabezados
            
            datos_columna = []
            for fila in lector_csv:
                if indice_columna < len(fila):
                    try:
                        valor = float(fila[indice_columna])
                        datos_columna.append(valor)
                    except ValueError:
                        # Si no se puede convertir a número, ignorar la fila
                        continue
            
            # Verificar si se obtuvieron datos numéricos
            if not datos_columna:
                print(f"No se encontraron datos numéricos en la columna '{encabezados[indice_columna]}'.")
                input("\nPresione Enter para continuar...")
                return
            
            # Calcular estadísticas
            num_datos = len(datos_columna)
            promedio = sum(datos_columna) / num_datos
            valor_minimo = min(datos_columna)
            valor_maximo = max(datos_columna)
            
            # Mostrar resultados
            print(f"\n=== Estadísticas para la columna '{encabezados[indice_columna]}' ===")
            print(f"Número de datos: {num_datos}")
            print(f"Promedio: {promedio:.2f}")
            print(f"Valor mínimo: {valor_minimo:.2f}")
            print(f"Valor máximo: {valor_maximo:.2f}")
            
            input("\nPresione Enter para continuar...")
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        input("\nPresione Enter para continuar...")

def graficar_columna(nombre_archivo):
    """
    Genera una gráfica de los datos de una columna del archivo CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV a procesar.
    """

        # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo):
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
            input("\nPresione Enter para continuar...")
            return
        
        # Verificar si el archivo tiene extensión .csv
    if not nombre_archivo.lower().endswith('.csv'):
            print(f"Error: El archivo '{nombre_archivo}' no es un archivo CSV.")
            input("\nPresione Enter para continuar...")
            return
        
        # Leer el archivo y obtener encabezados
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            encabezados = next(lector_csv)
            
            # Mostrar opciones de columnas
            print("\n=== Columnas disponibles ===")
            for i, encabezado in enumerate(encabezados):
                print(f"{i+1}. {encabezado}")
            
            # Solicitar selección de columna
            opcion = input("\nSeleccione el número de columna para graficar: ")
            try:
                indice_columna = int(opcion) - 1
                if indice_columna < 0 or indice_columna >= len(encabezados):
                    print("Selección de columna no válida.")
                    input("\nPresione Enter para continuar...")
                    return
            except ValueError:
                print("Entrada no válida. Debe ingresar un número.")
                input("\nPresione Enter para continuar...")
                return
            
            # Solicitar gráfica
            print("\n=== Gráfica ===")
            print("1. Histograma")
            tipo_grafica = input("\nSeleccione la gráfica: ")
            
            # Recolectar datos de la columna seleccionada
            archivo.seek(0)  # Volver al inicio del archivo
            next(lector_csv)  # Saltar encabezados
            
            datos_columna = []
            for fila in lector_csv:
                if indice_columna < len(fila):
                    try:
                        valor = float(fila[indice_columna])
                        datos_columna.append(valor)
                    except ValueError:
                        # Si no se puede convertir a número, ignorar la fila
                        continue
            
            # Verificar si se obtuvieron datos numéricos
            if not datos_columna:
                print(f"No se encontraron datos numéricos en la columna '{encabezados[indice_columna]}'.")
                input("\nPresione Enter para continuar...")
                return
            
            # Generar la gráfica según el tipo seleccionado
            plt.figure(figsize=(10, 6))
            
            if tipo_grafica == '1':  # Histograma
                plt.hist(datos_columna, bins=min(20, len(set(datos_columna))), color='skyblue', edgecolor='black')
                plt.title(f'Histograma - {encabezados[indice_columna]}')
                plt.xlabel(encabezados[indice_columna])
                plt.ylabel('Frecuencia')
                plt.grid(axis='y')
            
            else:
                print("Tipo de gráfica no válido.")
                input("\nPresione Enter para continuar...")
                return
            
            # Guardar y mostrar la gráfica
            nombre_grafica = f"grafica_{encabezados[indice_columna].replace(' ', '_')}.png"
            plt.tight_layout()
            plt.savefig(nombre_grafica) # graficar
            plt.show()
            
            print(f"\nLa gráfica se ha guardado como '{nombre_grafica}'")
            input("\nPresione Enter para continuar...")
    
  
