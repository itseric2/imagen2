import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def abrir_ventana_programa1():
    ventana_programa1 = tk.Toplevel(ventana)
    ventana_programa1.title("Programa 1")
    
    # Agrega aquí los elementos y la lógica para el Programa 1

def abrir_ventana_programa2():
    ventana_programa2 = tk.Toplevel(ventana)
    ventana_programa2.title("Programa 2")
    
    # Agrega aquí los elementos y la lógica para el Programa 2

def abrir_ventana_programa3():
    ventana_programa3 = tk.Toplevel(ventana)
    ventana_programa3.title("Programa 3")
    
    # Agrega aquí los elementos y la lógica para el Programa 3

def opcion(event):
    seleccion = combo_var.get()
    
    if seleccion == "Opción 1":
        abrir_ventana_programa1()
    elif seleccion == "Opción 2":
        abrir_ventana_programa2()
    elif seleccion == "Opción 3":
        abrir_ventana_programa3()

ventana = tk.Tk()
ventana.title("Programas según la selección")

combo_var = tk.StringVar()
opciones = ["Opción 1", "Opción 2", "Opción 3"]

combo = ttk.Combobox(ventana, values=opciones)
combo.bind("<<ComboboxSelected>>", opcion)
combo.pack()

ventana.mainloop()

