#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt #importa la libreria para hacer graficos

# 1. Contar el numero de plabras

def contar_palabras_caracteres(nombre_archivo):
    """
    Cuenta el número de palabras y caracteres en un archivo de texto.
    
    Args:
        nombre_archivo (str): Nombre del archivo de texto a procesar.
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(nombre_archivo):
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
            input("\nPresione Enter para continuar...")
            return
        
        # Leer el contenido del archivo
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        # Contar palabras
        palabras = contenido.split()
        num_palabras = len(palabras)
        
        # Contar caracteres con espacios
        num_caracteres_con_espacios = len(contenido)
        
        # Contar caracteres sin espacios
        num_caracteres_sin_espacios = len(contenido.replace(" ", "").replace("\n", "").replace("\t", ""))
        
        # Mostrar resultados
        print("\n=== Resultados ===")
        print(f"Número de palabras: {num_palabras}")
        print(f"Número de caracteres (con espacios): {num_caracteres_con_espacios}")
        print(f"Número de caracteres (sin espacios): {num_caracteres_sin_espacios}")
        
        input("\nPresione Enter para continuar...")
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        input("\nPresione Enter para continuar...")

# 2. Reemplazar una palabra por otra

def reemplazar_palabra(nombre_archivo, palabra_buscar, palabra_reemplazar):
    """
    Reemplaza una palabra por otra en un archivo de texto.
    
    Args:
        nombre_archivo (str): Nombre del archivo de texto a procesar.
        palabra_buscar (str): Palabra a buscar en el archivo.
        palabra_reemplazar (str): Palabra con la que se reemplazará.
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(nombre_archivo):
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
            input("\nPresione Enter para continuar...")
            return
        
        # Leer el contenido del archivo
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        
        # Realizar el reemplazo
        contenido_nuevo = contenido.replace(palabra_buscar, palabra_reemplazar)
        
        # Contar el número de reemplazos
        num_reemplazos = contenido.count(palabra_buscar)
        
        # Guardar el contenido modificado en un nuevo archivo
        nombre_archivo_nuevo = f"modificado_{nombre_archivo}"
        with open(nombre_archivo_nuevo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_nuevo)
        
        # Mostrar resultados
        print("\n=== Reemplazo completado ===")
        print(f"Se reemplazaron {num_reemplazos} ocurrencias de '{palabra_buscar}' por '{palabra_reemplazar}'")
        print(f"El resultado se guardó en el archivo '{nombre_archivo_nuevo}'")
        
        input("\nPresione Enter para continuar...")
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        input("\nPresione Enter para continuar...")

# 3. Histograma de vocales
def histograma_vocales(nombre_archivo):
    """
    Genera un histograma de la ocurrencia de vocales en un archivo de texto.
    
    Args:
        nombre_archivo (str): Nombre del archivo de texto a procesar.
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(nombre_archivo):
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
            input("\nPresione Enter para continuar...")
            return
        
        # Leer el contenido del archivo
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().lower()
        
        # Contar ocurrencias de cada vocal
        vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        
        for caracter in contenido:
            if caracter in vocales:
                vocales[caracter] += 1
        
        # Crear el histograma
        plt.figure(figsize=(10, 6))
        plt.bar(vocales.keys(), vocales.values(), color='skyblue')
        plt.title('Histograma de Ocurrencia de Vocales')
        plt.xlabel('Vocales')
        plt.ylabel('Número de Ocurrencias')
        
        # Añadir las cantidades encima de las barras
        for vocal, cantidad in vocales.items():
            plt.text(vocal, cantidad + 5, str(cantidad), ha='center')
        
        # Mostrar el histograma
        plt.tight_layout()
        plt.savefig('histograma_vocales.png')
        plt.show()
        
        # Mostrar resultados
        print("\n=== Histograma generado ===")
        print("El histograma se ha guardado como 'histograma_vocales.png'")
        print("Ocurrencias de vocales:")
        for vocal, cantidad in vocales.items():
            print(f"{vocal}: {cantidad}")
        
        input("\nPresione Enter para continuar...")
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        input("\nPresione Enter para continuar...")
