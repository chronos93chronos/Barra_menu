#proyecto tkinter para crear ventana con barra menu estilo cascada


import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x400")
ventana.title("BARRA MENU")
ventana.resizable(False, False)
#__________________________________________________________

barra_menu = tk.Menu()
menu_archivo = tk.Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(menu=menu_archivo, label="Archivo")




























#__________________________________________________________
ventana.config(menu=barra_menu)
ventana.mainloop()