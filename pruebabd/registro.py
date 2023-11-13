import tkinter as tk

import subprocess
from PIL import Image, ImageTk 
from tkinter import PhotoImage







###CREACION DE LA VENTANA Y SUS CONFIGURACIONES PARA CENTRARSE###################################################################33
# Crear la ventana principal
registro = tk.Tk()

# Establecer el título de la ventana
registro.title("Registro de usuario")

# Establecer las dimensiones de la ventana
registro.geometry("800x600")

# Evitar que se pueda modificar el tamaño de la ventana
registro.resizable(False, False)





# Obtener el ancho y la altura de la pantalla
ancho_pantalla = registro.winfo_screenwidth()
altura_pantalla = registro.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (800 // 2)  # La mitad del ancho de la pantalla menos la mitad del ancho de la ventana
y = (altura_pantalla // 2) - (600 // 2)  # La mitad de la altura de la pantalla menos la mitad de la altura de la ventana

# Establecer las dimensiones de la ventana y su posición centrada
registro.geometry("800x600+{}+{}".format(x, y))
###FIN DEL CENTRADO DE LA VENTANA###################################################################################################################




########################ELEMENTOS DE LA VENTANA##################################################################################################











# Agregar el logo########################################
logo_imagen = Image.open("/home/brama/pruebabd/imagenes/logo.png")  # Reemplaza "ruta_del_logo.png" con la ruta real de tu imagen
logo_imagen = logo_imagen.resize((150, 100), Image.ANTIALIAS)  # Ajusta el tamaño del logo
logo = ImageTk.PhotoImage(logo_imagen)
logo_label = tk.Label(registro, image=logo)
logo_label.image = logo  # Mantener una referencia
logo_label.pack(pady=10)

# Cargar un logotipo
logo_image = PhotoImage(file="/home/brama/pruebabd/imagenes/logo.png")

# Crear la barra de menú
menu_bar = tk.Menu(registro, font=("Helvetica", 16))



# Crear un widget Label para mostrar el logotipo en la barra de menú
logo_label = tk.Label(menu_bar, image=logo_image)
logo_label.photo = logo_image  # Referencia para evitar que la imagen sea eliminada por el recolector de basura
logo_label.pack(side="left")



# Nombre de usuario
etiqueta_usuario = tk.Label(registro, text="Nombre de Usuario:")
etiqueta_usuario.pack(pady=10)
nombre_usuario = tk.Entry(registro)
nombre_usuario.pack()

# Contraseña
etiqueta_contrasena = tk.Label(registro, text="Contraseña:")
etiqueta_contrasena.pack(pady=10)
contrasena = tk.Entry(registro, show="*")
contrasena.pack()

# COnfirmacion de contraseña
etiqueta_confirmacion_contrasena = tk.Label(registro, text="Confirmacion de contraseña:")
etiqueta_confirmacion_contrasena.pack(pady=10)
contrasena = tk.Entry(registro, show="*")
contrasena.pack()







def abrelogin():
    
    with open("login.py") as f:
        registro.destroy()
        exec(f.read())






# Boton de creacion de cuenta  
boton_crear_cuenta =tk.Button(registro,text="Crear cuenta",command=abrelogin)
boton_crear_cuenta.pack(pady=20)

##############################FIN DE LOS ELEMENTOS DE LA PANTALLA#########################################################################################



# Ejecutar el bucle principal
registro.mainloop()


