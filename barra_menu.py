#proyecto tkinter para crear ventana con barra menu estilo cascada


import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x400")
ventana.title("BARRA MENU")
ventana.resizable(False, False)
#__________________________________________________________
#FUNCIONES 
def saludo ():
    print("HELLO USER ACTIVE")


#__________________________________________________________

barra_menu = tk.Menu()
menu_archivo = tk.Menu(barra_menu, tearoff=False)
img_menu_nuevo = tk.PhotoImage(file="logo.png")

barra_menu.add_cascade(menu=menu_archivo, label="ARCHIVO")
menu_archivo.add_command(
    label="Nuevo",
    accelerator="Ctrl+N",
    command= saludo,
    )

menu_archivo.add_separator()#sirve para poner una linea de separacion en el menu cascada

menu_archivo.add_command(label="Ayuda")

#-------------
menu_herramientas = tk.Menu(barra_menu, tearoff=False)
barra_menu.add_cascade(menu=menu_herramientas, label="HERRAMIENTAS")
menu_herramientas.add_command(label="Informacion")
menu_herramientas.add_command(label="FAQ")

























#__________________________________________________________
ventana.config(menu=barra_menu)
ventana.mainloop()