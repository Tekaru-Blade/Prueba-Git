import tkinter as tk
import random

def enviar(e):
    info = entradaUsuario.get()
    labelResultado.configure(text=info)

def cambiarA(e):
    colores = ["red", "blue", "green", "yellow", "orange"]
    labelA.configure(fg=random.choice(colores))

def cambiarB(e):
    colores = ["purple", "pink", "brown", "cyan", "gold"]
    labelB.configure(fg=random.choice(colores))

ventana = tk.Tk()
ventana.title("Quiz")
ventana.geometry("400x400")

labelInstruccion = tk.Label(ventana, text="Ingresa tus datos usuario")
labelInstruccion.pack()

entradaUsuario = tk.Entry(ventana)
entradaUsuario.pack()

boton1 = tk.Button(ventana, text="Mostrar texto")
boton1.pack()

boton2 = tk.Button(ventana, text="Color de A")
boton2.pack()

boton3 = tk.Button(ventana, text="Color de B")
boton3.pack()

boton1.bind("<Button-3>", enviar)
boton2.bind("<Button-3>", cambiarA)
boton3.bind("<Button-3>", cambiarB)

labelA = tk.Label(ventana, text="Label numero 1")
labelA.pack()

labelB = tk.Label(ventana, text="Label numero 2")
labelB.pack()

marco = tk.LabelFrame(ventana, text="Resultado")
marco.pack()

labelResultado = tk.Label(marco, text="")
labelResultado.pack()

ventana.mainloop()