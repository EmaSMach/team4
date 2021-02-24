from tkinter import *
import logging
from tkinter.messagebox import showwarning

from team4 import es_palabra_valida, generar_palabra, separar_silabas


logging.basicConfig(level=logging.ERROR)  # INFO


class MostrarPalabrasGUI(Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_grab_and_wait(self):
        self.grab_set()
        self.wait_window()


class PalabraitorGUI(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.start_row = 2
        self.word_labels = []
        self.palabras = []

        self.make_widgets()
        self.make_input_widgets()

    def make_widgets(self):
        self.font = ('Verdana', 21, 'bold')
        self.top_widget = Label(self, text="Palabraitor", font=self.font)
        self.top_widget.grid(row=0, column=0, sticky='ew')

        self.pedir_palabra_container = Frame(self, bg='grey')
        self.pedir_palabra_container.grid(row=1, column=0, sticky='nsew')
        # configuramos las columnas y filas de este contenedor
        self.pedir_palabra_container.rowconfigure(ALL, weight=1)
        self.pedir_palabra_container.columnconfigure(0, weight=1)

        self.generar_palabras_btn = Button(self, text='Generar Palabra', command=self.on_generar_palabra_btn,
                                           font=self.font)
        self.generar_palabras_btn.grid(row=2, column=0, sticky='new')

    def make_input_widgets(self):
        self.palabra_var = StringVar()
        vcmd = (self.register(self.on_validate), "%P")
        self.input_widget = Entry(self.pedir_palabra_container, textvariable=self.palabra_var,
                                  font=self.font, validatecommand=vcmd, validate='key')
        self.input_widget.grid(row=0, column=0, sticky='new')

        self.input_widget.bind('<Return>', self.on_input_enter)

    def on_input_enter(self, event=None):
        palabra = self.palabra_var.get()
        if not es_palabra_valida(palabra, 2):
            showwarning("Aviso", "La palabra debe tener al menos dos letras!!!")
            return
        new_label = Label(self.pedir_palabra_container, text=f"{palabra}",
                          font=self.font)
        new_label.grid(row=self.start_row, column=0, sticky='n')
        logging.info(f" Columna Número: {self.start_row}")
        # agregamos el nuevo label a la lista de instancias
        # de modo que luego podamos llamar .destroy() en todas ellas, y vaciar la lista
        self.word_labels.append(new_label)
        self.palabras.append(palabra)
        self.start_row += 1

        # self.palabra_var.set("")  # reseteamos el contenido de la variable
        # AVISO: borramos el contenido del widget en lugar de setear el contenido del StringVar
        # por causar problemas con las funciones de validación
        self.input_widget.delete(0, END)
        # self.input_widget.update()

    def delete_word_labels(self, event=None):
        for lbl in self.word_labels:
            lbl.destroy()
        self.word_labels.clear()
        # self.palabras.clear()
        self.start_row = 2  # volvemos el contador al punto de partida

    def make_display_widgets(self):
        pass

    def on_generar_palabra_btn(self):
        palabras_semilla = self.palabras.copy()
        if not palabras_semilla:
            showwarning("Aviso", "No hay palabras igresadas!!!")
            return

        logging.info("Palabras semilla: ", palabras_semilla)
        result_window = MostrarPalabrasGUI()

        silabas = []
        for palabra in palabras_semilla:
            logging.info("P: ", palabra)
            temp = separar_silabas(palabra)
            logging.info("SILABAS:", palabra, temp)
            silabas.append(temp)

        logging.info("Silabas: ", silabas)
        palabra_generada = generar_palabra(silabas)
        mostrar_palabras(palabras_semilla, palabra_generada, result_window)

        self.palabras.clear()
        # limpiamos la ventana anterior
        self.delete_word_labels()
        result_window.set_grab_and_wait()

    def on_validate(self, P):
        """Validación simple, se aceptan solo letras, o dejar el campo vacío"""
        if len(P) == 0 or P.isalpha():
            return True
        else:
            return False


# esta parte es de and1
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


def main():
    root = Tk()
    root.title("Palabraitor")
    window = PalabraitorGUI(root)
    window.pack(expand=YES, fill=BOTH)
    root.mainloop()


if __name__ == '__main__':
    main()
