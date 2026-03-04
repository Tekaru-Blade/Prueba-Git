class CalculadoraBasica:
    def __init__(self):
        # Atributo para guardar el último resultado obtenido
        self.resultado_actual = 0

    def sumar(self, a, b):
        self.resultado_actual = a + b
        return self.resultado_actual

    def restar(self, a, b):
        self.resultado_actual = a - b
        return self.resultado_actual

    def multiplicar(self, a, b):
        self.resultado_actual = a * b
        return self.resultado_actual

    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        self.resultado_actual = a / b
        return self.resultado_actual

# --- Ejemplo de uso ---
mi_calc = CalculadoraBasica()
print(f"Suma: {mi_calc.sumar(10, 5)}")       # Salida: 15
print(f"Último guardado: {mi_calc.resultado_actual}") # Salida: 15
import math

class MatematicaAvanzada:
    def __init__(self, nombre_usuario):
        self.usuario = nombre_usuario

    def factorial(self, n):
        if n < 0: return "Error: Negativo"
        return math.factorial(n)

    def fibonacci(self, cantidad):
        a, b = 0, 1
        serie = []
        for _ in range(cantidad):
            serie.append(a)
            a, b = b, a + b
        return serie

    def obtener_mcd(self, a, b):
        return math.gcd(a, b)

# --- Ejemplo de uso ---
mate = MatematicaAvanzada("Estudiante")
print(f"Hola {mate.usuario}, el factorial de 5 es: {mate.factorial(5)}")
print(f"Serie Fibonacci (8): {mate.fibonacci(8)}")
class Facturacion:
    def __init__(self, tasa_iva):
        # Guardamos la tasa de IVA al crear el objeto
        self.tasa = tasa_iva

    def calcular_total(self, monto_base):
        iva = monto_base * (self.tasa / 100)
        total = monto_base + iva
        return total

    def cambiar_tasa(self, nueva_tasa):
        self.tasa = nueva_tasa
        print(f"Tasa de IVA actualizada a: {self.tasa}%")

# --- Ejemplo de uso ---
# Creamos una factura para Colombia (IVA 19%)
factura_col = Facturacion(19)
print(f"Total con IVA del 19%: {factura_col.calcular_total(1000)}")

# Cambiamos la tasa para otro país (ej. 10%)
factura_col.cambiar_tasa(10)
print(f"Total con IVA del 10%: {factura_col.calcular_total(1000)}")