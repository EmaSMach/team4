# Imports
from tkinter import *
from separasilabas import silabizer

def pedir_palabra() -> str:
    # se puede agregar validación
    """Pide una palabra, y la retorna."""
    return


def separar_silabas(palabra: str) -> list:
    """Separa la palabra dada en sílabas, retorna la lista de sílabas."""
    return

def generar_palabra(silabas_semilla: list) -> str:
    """Genera una palabra a partir de la lista de sílabas."""
    return


def mostrar_palabras(palabras_semilla: list, palabra_generada: str):
    """Muestra las palabras semilla, y la palabra generada."""
    print(
        "Se ingresaron {} palabras semillas: {}".format(
            len(palabras_semilla), 
            (', ').join(palabras_semilla).upper())
    )

    print(
        'La palabra creada es: {}'.format(
            palabra_generada.upper()
        )
    )

def main():
    # Logica principal del programa
    pass
    
if __name__ == '__main__':
    main()
    
