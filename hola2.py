import math  # Librería para funciones matemáticas avanzadas
import os    # Librería para interactuar con el sistema (limpiar pantalla)

def calcular_fibonacci(n: int) -> int:
    """Calcula el n-ésimo número de la serie de Fibonacci."""
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def calculadora() -> None:
    """
    Función principal: Ejecuta una calculadora acumulativa con validación
    de errores matemáticos y manejo de excepciones.
    """
    # Variable acumuladora: guarda el resultado para la siguiente operación
    memoria: float = 0.0 
    
    while True:
        # 1. Limpieza y Menú
        print("\n" + "="*40)
        print(f" VALOR ACUMULADO (MEMORIA): {memoria}")
        print("="*40)
        print("1. Suma (+)           2. Resta (-)")
        print("3. Multiplicación (*) 4. División (/)")
        print("5. Seno (sin)         6. Coseno (cos)")
        print("7. Tangente (tan)     8. Raíz enésima")
        print("9. Potencia enésima   10. Factorial (!)")
        print("11. Fibonacci (n)     12. MCM")
        print("13. MCD               14. Calcular IVA")
        print("15. REINICIAR MEMORIA 16. SALIR")
        
        opcion: str = input("\nSeleccione una operación (1-16): ")

        if opcion == "16":
            print("Cerrando calculadora...")
            break

        try:
            match opcion:
                # --- OPERACIONES BÁSICAS (ACUMULATIVAS) ---
                case "1" | "2" | "3" | "4":
                    nombres = {"1": "SUMA", "2": "RESTA", "3": "MULTIPLICACIÓN", "4": "DIVISIÓN"}
                    print(f"\n--- {nombres[opcion]} ---")
                    
                    # Lógica de acumulación
                    usar_mem = input(f"¿Usar {memoria} como primer número? (s/n): ").lower()
                    a = memoria if usar_mem == 's' else float(input("Ingrese primer número: "))
                    b = float(input("Ingrese segundo número: "))
                    
                    match opcion:
                        case "1": memoria = a + b
                        case "2": memoria = a - b
                        case "3": memoria = a * b
                        case "4":
                            if b == 0: raise ZeroDivisionError("No se puede dividir por cero.")
                            memoria = a / b
                    print(f"Resultado: {memoria}")

                # --- FUNCIONES TRIGONOMÉTRICAS ---
                case "5" | "6" | "7":
                    nombres = {"5": "SENO", "6": "COSENO", "7": "TANGENTE"}
                    print(f"\n--- {nombres[opcion]} ---")
                    g = float(input("Ingrese ángulo en grados: "))
                    rad = math.radians(g)
                    
                    if opcion == "5": memoria = math.sin(rad)
                    elif opcion == "6": memoria = math.cos(rad)
                    elif opcion == "7": memoria = math.tan(rad)
                    print(f"Resultado: {memoria}")

                # --- RAÍZ ENÉSIMA (VALIDACIÓN DE IMAGINARIOS) ---
                case "8":
                    print("\n--- RAÍZ ENÉSIMA ---")
                    x = float(input("Ingrese la base: "))
                    n = float(input("Ingrese el índice (n): "))
                    # Validación de números imaginarios (Base negativa e índice par)
                    if x < 0 and n % 2 == 0:
                        print("Error: El resultado es un número imaginario.")
                    else:
                        memoria = x ** (1/n)
                        print(f"Resultado: {memoria}")

                # --- POTENCIA ENÉSIMA ---
                case "9":
                    print("\n--- POTENCIA ENÉSIMA ---")
                    base = float(input("Base: "))
                    exp = float(input("Exponente: "))
                    memoria = math.pow(base, exp)
                    print(f"Resultado: {memoria}")

                # --- FACTORIAL ---
                case "10":
                    print("\n--- FACTORIAL ---")
                    num = int(input("Ingrese número entero: "))
                    if num < 0: print("Error: No existe factorial de números negativos.")
                    else:
                        memoria = math.factorial(num)
                        print(f"Resultado: {memoria}")

                # --- FIBONACCI ---
                case "11":
                    print("\n--- SERIE FIBONACCI ---")
                    pos = int(input("Ingrese la posición n: "))
                    memoria = calcular_fibonacci(pos)
                    print(f"El número en la posición {pos} es: {memoria}")

                # --- MCM Y MCD ---
                case "12" | "13":
                    nombre = "MCM" if opcion == "12" else "MCD"
                    print(f"\n--- {nombre} ---")
                    n1, n2 = int(input("Número 1: ")), int(input("Número 2: "))
                    memoria = math.lcm(n1, n2) if opcion == "12" else math.gcd(n1, n2)
                    print(f"Resultado: {memoria}")

                # --- IVA ---
                case "14":
                    print("\n--- CALCULAR IVA ---")
                    base = float(input("Ingrese monto base: "))
                    iva_porcent = float(input("Ingrese % de IVA: "))
                    iva_valor = base * (iva_porcent / 100)
                    memoria = base + iva_valor
                    print(f"IVA: {iva_valor} | Total: {memoria}")

                # --- UTILIDADES ---
                case "15":
                    memoria = 0.0
                    os.system('cls')
                    print("Memoria reiniciada.")

                case _:
                    print("Opción no válida.")

        except ZeroDivisionError as e:
            print(f"Error Matemático: {e}")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    calculadora()