import tkinter as tk
import subprocess
from tkinter import PhotoImage






# Crear la ventana principal
reserva = tk.Tk()

# Establecer el título de la ventana
reserva.title("RESERVA")

# Establecer las dimensiones de la ventana
reserva.geometry("800x600")

# Evitar que se pueda modificar el tamaño de la ventana
reserva.resizable(False, False)

# Obtener el ancho y la altura de la pantalla
ancho_pantalla = reserva.winfo_screenwidth()
altura_pantalla = reserva.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (800 // 2)  # La mitad del ancho de la pantalla menos la mitad del ancho de la ventana
y = (altura_pantalla // 2) - (600 // 2)  # La mitad de la altura de la pantalla menos la mitad de la altura de la ventana



# Establecer las dimensiones de la ventana y su posición centrada
reserva.geometry("800x600+{}+{}".format(x, y))










def opcion1():
    etiqueta.config(text="Opción 1 seleccionada")

def opcion2():
    etiqueta.config(text="Opción 2 seleccionada")

def opcion3():
    etiqueta.config(text="Opción 3 seleccionada")
    



  

# Crear la ventana principal


# Crear un marco para organizar el logo y los botones en la parte superior
marco_logo_botones = tk.Frame(reserva)
marco_logo_botones.grid(row=0, column=0, sticky="w", padx=10, pady=10)  # Organizar el marco usando grid

# Agregar un logo a la izquierda
logo = tk.PhotoImage(file="")  # Reemplaza "logo.png" con la ruta de tu archivo de imagen
label_logo = tk.Label(marco_logo_botones, image=logo)
label_logo.grid(row=0, column=0)  # Organizar el logo usando grid

# Crear botones con texto y añadirlos al marco
boton1 = tk.Button(marco_logo_botones, text="Opción 1", command=opcion1, compound=tk.LEFT, image=logo)
boton2 = tk.Button(marco_logo_botones, text="Opción 2", command=opcion2, compound=tk.LEFT, image=logo)
boton3 = tk.Button(marco_logo_botones, text="Opción 3", command=opcion3, compound=tk.LEFT, image=logo)

# Añadir botones al marco y organizarlos horizontalmente
boton1.grid(row=0, column=1, padx=10)
boton2.grid(row=0, column=2, padx=10)
boton3.grid(row=0, column=3, padx=10)

# Etiqueta para mostrar la opción seleccionada
etiqueta = tk.Label(reserva, text="")
etiqueta.grid(row=1, column=0, pady=20)  # Organizar la etiqueta usando grid

# Iniciar el bucle de la aplicación
reserva.mainloop()
