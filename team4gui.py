from tkinter import *
import logging


logging.basicConfig(level=logging.DEBUG)  # INFO


class PalabraitorGUI(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.start_row = 2
        self.word_labels = []

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

        self.generar_palabras_btn = Button(self, text='Generar Palabra', command=self.delete_word_labels,
                                           font=self.font)
        self.generar_palabras_btn.grid(row=2, column=0, sticky='new')

    def make_input_widgets(self):
        self.palabra_var = StringVar()
        self.input_widget = Entry(self.pedir_palabra_container, textvariable=self.palabra_var,
                                  font=self.font)
        self.input_widget.grid(row=0, column=0, sticky='new')

        self.input_widget.bind('<Return>', self.on_input_enter)

    def on_input_enter(self, event=None):
        palabra = self.palabra_var.get()
        new_label = Label(self.pedir_palabra_container, text=f"{palabra}",
                          font=self.font)
        new_label.grid(row=self.start_row, column=0, sticky='n')
        logging.info(f" Columna Número: {self.start_row}")
        # agregamos el nuevo label a la lista de instancias
        # de modo que luego podamos llamar .destroy() en todas ellas, y vaciar la lista
        self.word_labels.append(new_label)
        self.start_row += 1

        self.palabra_var.set("")  # reseteamos el contenido de la variable

    def delete_word_labels(self, event=None):
        for lbl in self.word_labels:
            lbl.destroy()
        self.word_labels.clear()
        self.start_row = 2  # volvemos el contador al punto de partida

    def make_display_widgets(self):
        pass


def main():
    root = Tk()
    root.title("Palabraitor")
    window = PalabraitorGUI(root)
    window.pack(expand=YES, fill=BOTH)
    root.mainloop()


if __name__ == '__main__':
    main()
