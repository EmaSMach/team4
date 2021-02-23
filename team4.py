#!/usr/bin/env python3
import random
from os import system
from separasilabas import silabizer


system("cls")


def es_palabra_valida(palabra: str, min_length: int) -> bool:
    """
    Verifica que la palabra dada sea válida, y que tenga el largo mínimo indicado.
    """
    if isinstance(palabra, str):
        if len(palabra) < min_length or not palabra.isalpha():
            return False
        else:
            return True
    else:
        raise TypeError("'palabra' debe ser un string")


def pedir_palabra(min_length: int = 2) -> str:
    """
    Pide una palabra, y la retorna.
    Sigue pidiendo hasta que se ingrese una palabra válida.
    """
    while True:
        palabra = input("Ingrese palabra: ").strip()
        if es_palabra_valida(palabra, min_length):
            return palabra
        else:
            print("Ingrese una palabra válida")


def generar_palabra(silabas_semilla: list) -> str:
    """Genera una palabra a partir de la lista de sílabas."""
    # ejemplo [["","","",""],["",""]]
    salida =''
    aux_rnd = random.randrange(2)
    if aux_rnd == 0:
    # tomando una sola silaba por cada palabra
        for x in silabas_semilla:
            r = random.randrange(len(x)-1)
            salida += x[r]
    elif aux_rnd ==1:
        # toma 2 silabas de la primera y 2 silaba de cada siguente
         
        for x in silabas_semilla:
            r = random.randrange(len(x)-1)
            salida += x[r]
            r = random.randrange(len(x)-1)
            salida += x[r]
    return salida


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
    