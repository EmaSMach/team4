def es_palabra_válida(palabra: str, min_length: int) -> bool:
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


def pedir_palabra(min_length=1) -> str:
    """
    Pide una palabra, y la retorna.
    Sigue pidiendo hasta que se ingrese una palabra válida.
    """
    while True:
        # esto puede agregarse como un parámetro
        err_msg = "Ingrese una palabra válida"
        palabra = input("Ingrese palabra: ").strip()
        if es_palabra_válida(palabra, min_length):
            return palabra
        else:
            print(err_msg)


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
    pass


if __name__ == '__main__':
    main()
