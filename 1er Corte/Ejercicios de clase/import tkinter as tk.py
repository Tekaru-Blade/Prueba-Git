import tkinter as tk


def aplicartexto():
    texto.config(text=entrada.get())
ventana = tk.Tk()
ventana.title("Mi primera GUI")
ventana.geometry("400x300")
ventana.configure(bg="lightblue")
ventana.attributes("-alpha", 0.9)

entrada = tk.Entry(ventana)
entrada.pack()

texto = tk.Label(ventana, text="¡Hola, mundo!")
texto.pack()  

def saludar():
    print("Hola")

boton = tk.Button(ventana, text="Haz clic", command=saludar)
boton.configure(bg="black", fg="white")
boton.pack()

frame = tk.Frame(ventana)
frame.configure(width=50, height=50, bg="cyan4")
frame.pack() 
frame = tk.Frame(ventana)
frame.configure(width=35, height=35, bg="midnight blue")
frame.pack() 

ventana.mainloop()