import tkinter as tk
import subprocess
from tkinter import PhotoImage


# Crear la ventana principal
menu = tk.Tk()

# Establecer el título de la ventana
menu.title("SUPER MENU")

# Establecer las dimensiones de la ventana
menu.geometry("800x600")

# Evitar que se pueda modificar el tamaño de la ventana
menu.resizable(False, False)

menu.configure(bg="white")  # Establecer el fondo de la ventana en blanco

# Obtener el ancho y la altura de la pantalla
ancho_pantalla = menu.winfo_screenwidth()
altura_pantalla = menu.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (900 // 2)  # La mitad del ancho de la pantalla menos la mitad del ancho de la ventana
y = (altura_pantalla // 2) - (650 // 2)  # La mitad de la altura de la pantalla menos la mitad de la altura de la ventana

# Establecer las dimensiones de la ventana y su posición centrada
menu.geometry("900x650+{}+{}".format(x, y))






##################################################PRUEBAS#############################################################################3

def opcion1():
    etiqueta.config(text="Opción 1 seleccionada")
    


def opcion2():
    etiqueta.config(text="Opción 2 seleccionada")

def opcion3():
    etiqueta.config(text="Opción 3 seleccionada")


def cambiar_color_naranja(boton):
    # Restaurar el color original de todos los botones
    for btn in [boton1, boton2, boton3, boton4]:
        btn.config(bg="#FFD700", activebackground="#FFD700", relief=tk.FLAT)
    # Cambiar el color del botón clicado a naranja fuerte
    boton.config(bg="#FFA500", activebackground="#FFA500", relief=tk.SUNKEN)



def resaltar_naranja(event):
    event.widget.config(bg="#FFA500", activebackground="#FFA500")

def restaurar_color(event):
    if event.widget.cget("relief") != tk.SUNKEN:
        event.widget.config(bg="#FFD700", activebackground="#FFD700")





##############FUNCION PARA ABRIR LA VENTANA DE RESERVA
def abrir_ventana_secundaria():
    with open("reserva.py") as f:
        
        exec(f.read())


   


# Crear un marco para organizar los botones en la parte superior
marco_botones = tk.Frame(menu, background="#FFD700")
marco_botones.pack(side=tk.TOP, fill=tk.X)



###########CARGAR LAS IMAGENES################33
boton_vuelo = tk.PhotoImage(file="/home/brama/pruebabd/imagenes/logo.png").subsample(2,2)
label_logo = tk.Label(marco_botones, image=boton_vuelo)

icono_vuelo = tk.PhotoImage(file="/home/brama/pruebabd/imagenes/iconoavion.png").subsample(9,9)
label_iconovuelo = tk.Label(marco_botones, image=boton_vuelo)

##LOGO DE LA PARTE IZQUIERDA SUPERIOR
label_logo.grid(row=0, column=0, padx=10) 





boton1 = tk.Button(
    marco_botones,
    text="VUELO",
    command=lambda: [opcion1(), cambiar_color_naranja(boton1),abrir_ventana_secundaria()],
    compound=tk.LEFT,
    image=icono_vuelo,
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=120,  # Ancho del botón
)
boton2 = tk.Button(
    marco_botones,
    text="RESERVA",
    command=lambda: [opcion2(), cambiar_color_naranja(boton2)],
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=9,  # Ancho del borde
    width=15,  # Ancho del botón
)
boton3 = tk.Button(
    marco_botones,
    text="Opción 3",
    command=lambda: [opcion3(), cambiar_color_naranja(boton3)],
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=15,  # Ancho del botón
)
boton4 = tk.Button(
    marco_botones,
    text="Opción 4",
    command=lambda: [opcion1(), cambiar_color_naranja(boton4)],
    bg="#FFD700",  # Color de fondo por defecto
    activebackground="#FFD700",  # Naranja claro cuando el mouse está sobre el botón
    bd=2,  # Borde del botón
    highlightthickness=0,  # Grosor del resaltado
    relief=tk.FLAT,  # Establecer el relieve del botón
    borderwidth=1,  # Ancho del borde
    width=15,  # Ancho del botón
)

# Configurar eventos para resaltar el color naranja cuando el mouse entra o sale del botón
boton1.bind("<Enter>", resaltar_naranja)
boton1.bind("<Leave>", restaurar_color)
boton2.bind("<Enter>", resaltar_naranja)
boton2.bind("<Leave>", restaurar_color)
boton3.bind("<Enter>", resaltar_naranja)
boton3.bind("<Leave>", restaurar_color)
boton4.bind("<Enter>", resaltar_naranja)
boton4.bind("<Leave>", restaurar_color)




# Añadir botones a la ventana
boton1.grid(row=0, column=1, padx=10)
boton2.grid(row=0, column=2, padx=10)
boton3.grid(row=0, column=3, padx=10)
boton4.grid(row=0, column=4, padx=10)

# Etiqueta para mostrar la opción seleccionada
etiqueta = tk.Label(menu, text="")
etiqueta.pack(pady=20)










################################################# FIN DE LAS PRUEBAS #############################################################




# Ejecutar el bucle principal
menu.mainloop()