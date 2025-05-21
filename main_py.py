
import os # Para trabajar con archivos y rutas
import procesador_texto
import procesador_csv


def listar_archivos():
    
    """Lista los archivos en la ruta actual o en una ruta especificada por el usuario."""
    print("\n=== Listar Archivos ===")
    print("1. Listar archivos en la ruta actual")
    print("2. Especificar una ruta para listar archivos")
    opcion = input("\nSeleccione una opción: ")
    
    if opcion == '1':
        ruta = os.getcwd()
    elif opcion == '2':
        ruta = input("Ingrese la ruta donde desea buscar archivos: ")
        if not os.path.exists(ruta):
            print(f"Error: La ruta '{ruta}' no existe.")
            return
    else:
        print("Opción no válida.")
        return
    
    try:
        archivos = os.listdir(ruta)
        print(f"\nArchivos en {ruta}:")
        for i, archivo in enumerate(archivos, 1):
            print(f"{i}. {archivo}")
        
        input("\nPresione Enter para continuar...")
    except Exception as e:
        print(f"Error al listar archivos: {e}")
        input("\nPresione Enter para continuar...")

def menu_texto():
    """Muestra el submenú para procesar archivos de texto."""
    while True:
        print("\n=== Procesamiento de Archivos de Texto (.txt) ===")
        print("1. Contar número de palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de ocurrencia de las vocales")
        print("4. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
            procesador_texto.contar_palabras_caracteres(nombre_archivo)
        elif opcion == '2':
            nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
            palabra_buscar = input("Ingrese la palabra a buscar: ")
            palabra_reemplazar = input("Ingrese la palabra de reemplazo: ")
            procesador_texto.reemplazar_palabra(nombre_archivo, palabra_buscar, palabra_reemplazar)
        elif opcion == '3':
            nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
            procesador_texto.histograma_vocales(nombre_archivo)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

def menu_csv():
    """Muestra el submenú para procesar archivos CSV."""
    while True:
        print("\n=== Procesamiento de Archivos CSV (.csv) ===")
        print("1. Mostrar las primeras 15 filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna")
        print("4. Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
            procesador_csv.mostrar_primeras_filas(nombre_archivo)
        elif opcion == '2':
            nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
            procesador_csv.calcular_estadisticas(nombre_archivo)
        elif opcion == '3':
            nombre_archivo = input("Ingrese el nombre del archivo CSV: ")
            procesador_csv.graficar_columna(nombre_archivo)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

def menu_principal():
    """Muestra el menú principal de la aplicación."""
    while True:
        print("\n=== Aplicación CLI de Análisis de Datos ===")
        print("1. Listar archivos")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo CSV (.csv)")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            listar_archivos()
        elif opcion == '2':
            menu_texto()
        elif opcion == '3':
            menu_csv()
        else:
            print("Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
