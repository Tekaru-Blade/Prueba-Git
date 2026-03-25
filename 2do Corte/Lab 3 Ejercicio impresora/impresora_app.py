import tkinter as tk
from tkinter import messagebox
from collections import deque
import threading
import time
# Importamos la clase desde el archivo correspondiente
from documento import Documento

class ImpresoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cola de Impresion UMNG")
        self.cola = deque() # Implementacion FIFO
        self.root.geometry("640x480")
        self.imprimiendo = False

        # Interfaz con Tkinter
        tk.Label(root, text="Nombre:").pack()
        self.ent_nombre = tk.Entry(root)
        self.ent_nombre.pack()

        tk.Label(root, text="Paginas:").pack()
        self.ent_paginas = tk.Entry(root)
        self.ent_paginas.pack()

        tk.Label(root, text="Tiempo x Pagina (seg):").pack()
        self.ent_tiempo = tk.Entry(root)
        self.ent_tiempo.pack()

        tk.Button(root, text="Agregar Documento", command=self.agregar).pack()
        tk.Button(root, text="Empezar Impresion", command=self.iniciar).pack()

        self.lbl_estado = tk.Label(root, text="Esperando...")
        self.lbl_estado.pack()

    def agregar(self):
        try:
            nombre = self.ent_nombre.get()
            paginas = int(self.ent_paginas.get())
            tiempo = float(self.ent_tiempo.get())
            
            doc = Documento(nombre, paginas, tiempo)
            self.cola.append(doc) 
            self.lbl_estado.config(text=f"En cola: {len(self.cola)}")
        except ValueError:
            messagebox.showerror("Error", "Asegúrate de ingresar números válidos en páginas y tiempo.")

    def iniciar(self):
        if not self.imprimiendo and self.cola:
            self.imprimiendo = True
            threading.Thread(target=self.proceso, daemon=True).start()

    def proceso(self):
        while self.cola:
            doc = self.cola.popleft() 
            for p in range(1, doc.paginas + 1):
                self.lbl_estado.config(text=f"Imprimiendo {doc.nombre}: Pagina {p} de {doc.paginas}")
                time.sleep(doc.tiempo_pag)
        
        self.lbl_estado.config(text="No hay mas documentos")
        self.imprimiendo = False