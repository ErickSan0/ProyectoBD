import tkinter as tk

from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk 






def iniciar_sesion():
    username = nombre_usuario.get()
    password = contrasena.get()
    # Aquí puedes implementar la lógica de verificación del nombre de usuario y la contraseña

    if username == "usuario" and password == "contrasena":  # Verificación de ejemplo, reemplaza con tu lógica de verificación
        etiqueta_estado.config(text="Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales inválidas")










###CREACION DE LA VENTANA Y SUS CONFIGURACIONES PARA CENTRARSE###################################################################33
# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Inicio sesion")

# Establecer las dimensiones de la ventana
ventana.geometry("400x300")

# Evitar que se pueda modificar el tamaño de la ventana
ventana.resizable(False, False)





# Obtener el ancho y la altura de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla // 2) - (400 // 2)  # La mitad del ancho de la pantalla menos la mitad del ancho de la ventana
y = (altura_pantalla // 2) - (300 // 2)  # La mitad de la altura de la pantalla menos la mitad de la altura de la ventana

# Establecer las dimensiones de la ventana y su posición centrada
ventana.geometry("400x400+{}+{}".format(x, y))
###FIN DEL CENTRADO DE LA VENTANA###################################################################################################################






########################ELEMENTOS DE LA VENTANA##################################################################################################


# Agregar el logo
logo_imagen = Image.open("/home/brama/pruebabd/imagenes/logo.png")  # Reemplaza "ruta_del_logo.png" con la ruta real de tu imagen
logo_imagen = logo_imagen.resize((150, 100), Image.ANTIALIAS)  # Ajusta el tamaño del logo
logo = ImageTk.PhotoImage(logo_imagen)
logo_label = tk.Label(ventana, image=logo)
logo_label.image = logo  # Mantener una referencia
logo_label.pack(pady=10)

# Nombre de usuario
etiqueta_usuario = tk.Label(ventana, text="Nombre de Usuario:")
etiqueta_usuario.pack(pady=10)
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack()

# Contraseña
etiqueta_contrasena = tk.Label(ventana, text="Contraseña:")
etiqueta_contrasena.pack(pady=10)
contrasena = tk.Entry(ventana, show="*")
contrasena.pack()




# Botón de inicio de sesión
boton_inicio_sesion = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
boton_inicio_sesion.pack(pady=20)




def registr():
    
    with open("registro.py") as f:
        ventana.destroy()
        exec(f.read())




def menu():
    
    with open("menu.py") as f:
        ventana.destroy()
        exec(f.read())

# Boton de creacion de cuenta  
boton_crear_cuenta =tk.Button(ventana,text="Crear cuenta",command=registr)
boton_crear_cuenta.pack(pady=20)

##############################FIN DE LOS ELEMENTOS DE LA PANTALLA#########################################################################################



# Ejecutar el bucle principal
ventana.mainloop()