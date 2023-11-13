






##############################################PRUEBAS#########################################
import tkinter as tk
from tkinter import messagebox

from pymongo import MongoClient

class SeleccionAsientosApp:
    def __init__(self, root, vuelo_id):
        self.root = root
        self.root.title("Seleccion de Asientos")
        self.vuelo_id = vuelo_id

        # Conectar a la base de datos MongoDB
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["fly"]
        self.asientos_collection = self.db["asientos"]

        # Inicializar la interfaz
        self.asientos_disponibles = set(range(1, 51))
        self.asientos_seleccionados = set()
        self.crear_interfaz()

    def crear_interfaz(self):
        self.botones_asientos = []

        for fila in range(5):
            fila_botones = []
            for columna in range(10):
                numero_asiento = fila * 10 + columna + 1
                estado_asiento = self.obtener_estado_asiento(numero_asiento)
                boton_asiento = tk.Button(
                    self.root,
                    text=str(numero_asiento),
                    width=5,
                    height=2,
                    command=lambda n=numero_asiento: self.toggle_asiento(n),
                    bg=estado_asiento["color"],
                    fg="white"
                )
                boton_asiento.grid(row=fila, column=columna, padx=5, pady=5)
                fila_botones.append(boton_asiento)
            self.botones_asientos.append(fila_botones)

        # Botón de confirmación
        boton_confirmar = tk.Button(self.root, text="Confirmar", command=self.confirmar_seleccion)
        boton_confirmar.grid(row=5, column=0, columnspan=10, pady=10)

    def toggle_asiento(self, numero_asiento):
        if numero_asiento in self.asientos_seleccionados:
            self.desseleccionar_asiento(numero_asiento)
        else:
            if numero_asiento in self.asientos_disponibles:
                self.seleccionar_asiento(numero_asiento)
            else:
                messagebox.showinfo("Asiento Ocupado", "Este asiento ya está ocupado.")

    def seleccionar_asiento(self, numero_asiento):
        self.asientos_seleccionados.add(numero_asiento)
        fila, columna = self.obtener_fila_columna(numero_asiento)
        self.botones_asientos[fila][columna].config(bg="blue", fg="white")
        print("Asiento seleccionado:", numero_asiento)

    def desseleccionar_asiento(self, numero_asiento):
        self.asientos_seleccionados.remove(numero_asiento)
        fila, columna = self.obtener_fila_columna(numero_asiento)
        self.botones_asientos[fila][columna].config(bg="green", fg="white")
        print("Asiento desseleccionado:", numero_asiento)

    def confirmar_seleccion(self):
        print("Asientos confirmados:", self.asientos_seleccionados)
        # Aquí podrías implementar la lógica para guardar los asientos en tu base de datos MongoDB
        for numero_asiento in self.asientos_seleccionados:
            self.bloquear_asiento(numero_asiento)
        self.asientos_seleccionados.clear()

    def bloquear_asiento(self, numero_asiento):
        self.asientos_disponibles.remove(numero_asiento)
        estado_asiento = {
            "vuelo_id": self.vuelo_id,
            "numero_asiento": numero_asiento,
            "estado": "bloqueado"
        }
        self.asientos_collection.insert_one(estado_asiento)
        fila, columna = self.obtener_fila_columna(numero_asiento)
        self.botones_asientos[fila][columna].config(bg="red", fg="white")

    def obtener_estado_asiento(self, numero_asiento):
        # Consultar el estado actual del asiento en la base de datos
        estado_asiento = self.asientos_collection.find_one({
            "vuelo_id": self.vuelo_id,
            "numero_asiento": numero_asiento
        })

        if estado_asiento:
            return {"color": "red", "estado": estado_asiento["estado"]}
        elif numero_asiento in self.asientos_disponibles:
            return {"color": "green", "estado": "disponible"}
        else:
            return {"color": "", "estado": ""}

    def obtener_fila_columna(self, numero_asiento):
        fila = (numero_asiento - 1) // 10
        columna = (numero_asiento - 1) % 10
        return fila, columna

if __name__ == "__main__":
    vuelo_id = "vuelo_123"  # Reemplaza con un identificador de vuelo real
    root = tk.Tk()
    app = SeleccionAsientosApp(root, vuelo_id)
    root.mainloop()






##########################################FIN DE LAS PRUEBAS###############################33