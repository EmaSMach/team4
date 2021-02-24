#!/usr/bin/env python3
import random
from os import system
from separasilabas import silabizer
system("cls")

def pedir_palabra() -> str:
    # se puede agregar validación
    """Pide una palabra, y la retorna."""
    return


def separar_silabas(palabra: str) -> list:
    """Separa la palabra dada en sílabas, retorna la lista de sílabas."""
    return


def generar_palabra(silabas_semilla: list) -> str:
    """Genera una palabra a partir de la lista de sílabas."""
    # ejemplo [["","","",""],["",""]]
    salida =''
    
    for x in silabas_semilla:
        aux_rnd = random.randrange(2)
        # si es una sola silaba
        if len(x) == 1:
            salida += x[0]
        elif aux_rnd ==0:
            # si tiene mas de 2 silabas pero el randrage == 0 elige solo 1 silaba de la palabra
            r = random.randrange(len(x))
            salida += x[r]
        elif aux_rnd ==1:
            # si tiene mas de 2 silabas pero el randrage == 0 elige solo 2 silabas de la palabra
            r = random.randrange(len(x))
            salida += x[r]
            r = random.randrange(len(x))
            salida += x[r]
            
    return salida


def mostrar_palabras(palabras_generadas: list, palabras_semilla: list):
    """Muestra las palabras base, y las generadas."""
    return


def main():
    # Logica principal del programa
    valor =[["BI","CI","CLE","TA"],["PA","RA","GUAS"]]

    print(generar_palabra(valor))
    return


if __name__ == '__main__':
    main()
