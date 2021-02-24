from tkinter import *

from team4gui import *


def main():
    root = Tk()
    root.title("Palabraitor")
    window = PalabraitorGUI(root)
    window.pack(expand=YES, fill=BOTH)
    root.mainloop()


if __name__ == '__main__':
    main()
