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


def separar_silabas(palabra: str) -> list:
    """Separa la palabra dada en sílabas, retorna la lista de sílabas."""
    return


def generar_palabra(silabas_semilla: list) -> str:
    """Genera una palabra a partir de la lista de sílabas."""
    return


def mostrar_palabras(palabras_generadas: list, palabras_semilla: list):
    """Muestra las palabras base, y las generadas."""
    return


def main():
    # Logica principal del programa
    pedir_palabra()
    return


if __name__ == '__main__':
    main()
