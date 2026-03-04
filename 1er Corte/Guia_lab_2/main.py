import random
from matriz import OperacionesMatriciales
from ordenamiento import AlgoritmosOrdenamiento

class MenuPrincipal:
    """Controlador de la interfaz de consola y navegación."""

    def __init__(self):
        self.mat_ops = OperacionesMatriciales()
        self.ord_ops = AlgoritmosOrdenamiento()

    def ejecutar(self):
        while True:
            print("\n--- LABORATORIO 2: ESTRUCTURAS Y ORDENAMIENTO ---")
            print("1. Operaciones con Matrices (Punto 3.1)")
            print("2. Algoritmos de Ordenamiento (Punto 3.2)")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.submenu_matrices()
            elif opcion == '2':
                self.submenu_ordenamiento()
            elif opcion == '3':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida.")

    def submenu_matrices(self):
        print("\n--- SUBMENÚ MATRICES ---")
        print("a. Suma\nb. Producto\nc. Inversa\nd. Producto Matriz x Vector")
        sub = input("Opción: ").lower()
        
        if sub == 'a':
            f, c = int(input("Filas: ")), int(input("Cols: "))
            print("\nDatos Matriz A:"); A = self.mat_ops.crear_matriz(f, c)
            print("\nDatos Matriz B:"); B = self.mat_ops.crear_matriz(f, c)
            res = self.mat_ops.sumar_matrices(A, B)
            print("--- RESULTADO SUMA ---")
            self.mat_ops.imprimir_matriz(res)
            
        elif sub == 'b':
            f1, c1 = int(input("Filas A: ")), int(input("Cols A: "))
            f2, c2 = int(input("Filas B: ")), int(input("Cols B: "))
            if c1 != f2:
                print("¡Error! Columnas de A deben ser iguales a filas de B.")
            else:
                print("\nDatos Matriz A:"); A = self.mat_ops.crear_matriz(f1, c1)
                print("\nDatos Matriz B:"); B = self.mat_ops.crear_matriz(f2, c2)
                res = self.mat_ops.multiplicar_matrices(A, B)
                print("--- RESULTADO PRODUCTO ---")
                self.mat_ops.imprimir_matriz(res)

        elif sub == 'c':
            n = int(input("Dimensión de matriz cuadrada: "))
            M = self.mat_ops.crear_matriz(n, n)
            res = self.mat_ops.invertir_matriz(M)
            print("--- RESULTADO INVERSA ---")
            self.mat_ops.imprimir_matriz(res)

        elif sub == 'd':
            f, c = int(input("Filas matriz: ")), int(input("Cols matriz: "))
            M = self.mat_ops.crear_matriz(f, c)
            print(f"Ingrese los {c} valores del vector:")
            V = [float(input(f"Valor [{i}]: ")) for i in range(c)]
            res = self.mat_ops.producto_matriz_vector(M, V)
            print("--- RESULTADO VECTOR ---")
            print(res)

    def submenu_ordenamiento(self):
        n = int(input("¿Cuántos números generar?: "))
        original = [round(random.uniform(0, 100), 2) for _ in range(n)]
        print(f"\nLista Original: {original}")
        print("Burbuja:   ", self.ord_ops.burbuja(original))
        print("MergeSort: ", self.ord_ops.mergesort(original))

if __name__ == "__main__":
    app = MenuPrincipal()
    app.ejecutar()