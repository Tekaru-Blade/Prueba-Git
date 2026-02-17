import math

# Función auxiliar para Fibonacci
def calcular_fibonacci(n: int) -> int:
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculadora():
    while True:
        print("\n=== CALCULADORA (SOLO CASES) ===")
        print("1. Suma            2. Resta           3. Multiplicación")
        print("4. División        5. Seno            6. Coseno")
        print("7. Tangente        8. Raíz enésima    9. Potencia")
        print("10. Factorial      11. Fibonacci      12. MCM")
        print("13. MCD            14. Calcular IVA   15. Salir")
        
        opcion: str = input("\nSeleccione su opción: ")

        try:
            match opcion:
                case "1":
                    print("\n--- SUMA ---")
                    a, b = float(input("Num 1: ")), float(input("Num 2: "))
                    print(f"Resultado: {a + b}")
                
                case "2":
                    print("\n--- RESTA ---")
                    a, b = float(input("Num 1: ")), float(input("Num 2: "))
                    print(f"Resultado: {a - b}")

                case "3":
                    print("\n--- MULTIPLICACIÓN ---")
                    a, b = float(input("Num 1: ")), float(input("Num 2: "))
                    print(f"Resultado: {a * b}")

                case "4":
                    print("\n--- DIVISIÓN ---")
                    a, b = float(input("Dividendo: ")), float(input("Divisor: "))
                    # Aquí el único if necesario por seguridad matemática
                    if b != 0: print(f"Resultado: {a / b}")
                    else: print("Error: División por cero.")

                case "5":
                    print("\n--- SENO ---")
                    g = float(input("Grados: "))
                    print(f"Resultado: {math.sin(math.radians(g))}")

                case "6":
                    print("\n--- COSENO ---")
                    g = float(input("Grados: "))
                    print(f"Resultado: {math.cos(math.radians(g))}")

                case "7":
                    print("\n--- TANGENTE ---")
                    g = float(input("Grados: "))
                    print(f"Resultado: {math.tan(math.radians(g))}")

                case "8":
                    print("\n--- RAÍZ ENÉSIMA ---")
                    x, n = float(input("Base: ")), float(input("Índice: "))
                    print(f"Resultado: {x ** (1/n)}")

                case "9":
                    print("\n--- POTENCIA ENÉSIMA ---")
                    b, e = float(input("Base: ")), float(input("Exponente: "))
                    print(f"Resultado: {math.pow(b, e)}")

                case "10":
                    print("\n--- FACTORIAL ---")
                    n = int(input("Número entero: "))
                    print(f"Resultado: {math.factorial(n)}")

                case "11":
                    print("\n--- FIBONACCI ---")
                    n = int(input("Posición: "))
                    print(f"Resultado: {calcular_fibonacci(n)}")

                case "12":
                    print("\n--- MCM ---")
                    a, b = int(input("Num 1: ")), int(input("Num 2: "))
                    print(f"Resultado: {math.lcm(a, b)}")

                case "13":
                    print("\n--- MCD ---")
                    a, b = int(input("Num 1: ")), int(input("Num 2: "))
                    print(f"Resultado: {math.gcd(a, b)}")

                case "14":
                    print("\n--- IVA ---")
                    m = float(input("Monto: "))
                    p = float(input("Porcentaje IVA: "))
                    print(f"IVA: {m * (p/100)} | Total: {m + (m * (p/100))}")

                case "15":
                    print("Saliendo...")
                    break

                case _:
                    print("Opción inválida.")

        except ValueError:
            print("Error: Entrada no válida.")

if __name__ == "__main__":
    calculadora()