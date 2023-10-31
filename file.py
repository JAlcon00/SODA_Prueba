# Autor: Almanza Contreras José de Jesús
import geopy
from geopy.distance import geodesic

newpoert_r1 = (41.4908, -71.312796)

def readFile(namefile):
    """
    Función para leer el contenido de un archivo.

    Parámetros:
    - namefile (str): Nombre del archivo a leer.

    Retorna:
    - str: Contenido del archivo leído.
    """
    try:
        # Abre el archivo en modo de lectura ("r")
        with open(namefile, "r") as file:
            # Lee el contenido del archivo
            data = file.read()
            return data
    except Exception as e:
        # Captura y maneja cualquier excepción que pueda ocurrir al leer el archivo
        print(f"Error al leer el archivo: {e}")
        return None

# Llama a la función para leer el contenido del archivo "bd.txt"
file_content = readFile("bd.txt")

# Imprime el contenido del archivo leído
print(file_content)

def writeFile(nameFile, text):
    """
    Función para escribir en un archivo.

    Parámetros:
    - nameFile (str): Nombre del archivo en el que se va a escribir.
    - text (str): Texto que se va a escribir en el archivo.

    Retorna:
    - str or None: El texto escrito en el archivo si tiene éxito, None si hay un error.
    """
    try:
        # Abre el archivo en modo de escritura ("w")
        with open(nameFile, "w") as file:
            # Escribe el texto en el archivo
            file.write(text)
        # Retorna el texto escrito en el archivo
        return text
    except Exception as e:
        # Captura y maneja cualquier excepción que pueda ocurrir al escribir en el archivo
        print(f"Error al escribir en el archivo: {e}")
        return None

# Llama a la función para escribir en el archivo "bd.txt"
print(writeFile("bd.txt", "OHHHH MY DOG HAHAHA!"))


