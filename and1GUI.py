from tkinter import *


def mostrar_palabras(palabras_semilla: list, palabra_generada: str, main_window):
    """Muestra las palabras semilla, y la palabra generada."""

    font = ('Verdana', 21, 'bold')

    # Frame que muestra las palabras ingresadas
    frame_mostrar_palabras = LabelFrame(
        main_window, 
        text = 'MOSTRAR LAS PALABRAS CARGADAS:',
        font = font
    )

    frame_mostrar_palabras.grid(row = 0, column = 0, sticky = 'WENS')

    label_palabras_mostradas = Label(
        frame_mostrar_palabras, 
        text = (', '.join(palabras_semilla)).upper(),
        font = font
    )

    label_palabras_mostradas.grid(row = 0, column = 0, sticky = 'WENS')

    # Frame que muestra la palabra creada.
    frame_palabra_creada = LabelFrame(
        main_window, 
        text = 'MOSTRAR LA PALABRA CREADA:',
        font = font
    )

    frame_palabra_creada.grid(row = 1, column = 0, sticky = 'WENS')

    label_palabras_mostradas = Label(
        frame_palabra_creada, 
        text = palabra_generada.upper(),
        font = font
    )

    label_palabras_mostradas.grid(row = 0, column = 0, sticky = 'WENS')

    # Botón para cerrar la ventana
    boton_cerrar = Button(
        main_window, 
        text = 'Cerrar',
        command = main_window.destroy,
        font = font
    )

    boton_cerrar.grid(row = 2, column = 0, sticky = 'NS')
 

def main(main_window):
    # Logica principal del programa
    palabras_semilla = ['ñandu', 'rio', 'bicicleta']
    palabra_generada = 'ñaocleta'
    mostrar_palabras(palabras_semilla, palabra_generada, main_window)
    
if __name__ == '__main__':
    main_window = Tk()
    main_window.title("Palabreitor")
    main(main_window)
    main_window.mainloop()