import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Ejemplo de Integración de Imágenes")

imagen_pil = Image.open(r"5eeea355389655.59822ff824b72.gif")

imagen_tk = ImageTk.PhotoImage(imagen_pil)

etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
etiqueta_imagen.pack()

ventana.mainloop()