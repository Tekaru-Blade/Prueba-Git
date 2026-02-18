import math

def mostrar_menu():
    print("\n" + "="*30)
    print("   CALCULADORA MULTIFUNCION")
    print("="*30)
    print("1. Operaciones Basicas")
    print("2. Trigonometria")
    print("3. Raiz Enesima")
    print("4. Potencia")
    print("5. Factorial")
    print("6. Serie Fibonacci")
    print("7. M.C.M (Minimo Comun Multiplo)")
    print("8. M.C.D (Maximo Comun Divisor)")
    print("9. Calculo de IVA")
    print("0. Salir")
    print("-" * 30)

def calcular_fibonacci(n):
    if n < 0: return "No definido para negativos"
    a, b = 0, 1
    serie = []
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    return serie

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una categoria (0-9): ")

        try:
            match opcion:
                case "1":
                    print("\n[BASICAS] 1: Suma | 2: Resta | 3: Multi | 4: Div")
                    sub = input("Seleccione: ")
                    n1 = float(input("Primer numero: "))
                    n2 = float(input("Segundo numero: "))
                    match sub:
                        case "1": print(f"Resultado: {n1 + n2}")
                        case "2": print(f"Resultado: {n1 - n2}")
                        case "3": print(f"Resultado: {n1 * n2}")
                        case "4": 
                            if n2 == 0: print("ERROR: No se puede dividir por cero.")
                            else: print(f"Resultado: {n1 / n2}")
                        case _: print("Sub-opcion no valida.")

                case "2":
                    print("\n[TRIGONOMETRIA] 1: Seno | 2: Coseno | 3: Tangente")
                    sub = input("Seleccione: ")
                    val = float(input("Ingrese el angulo en GRADOS: "))
                    rad = math.radians(val) 
                    match sub:
                        case "1": print(f"Seno({val}°) = {math.sin(rad)}")
                        case "2": print(f"Coseno({val}°) = {math.cos(rad)}")
                        case "3": print(f"Tangente({val}°) = {math.tan(rad)}")
                        case _: print("Sub-opcion no valida.")

                case "3":
                    num = float(input("Base de la raiz: "))
                    ind = float(input("Indice de la raiz: "))
                    if num < 0 and ind % 2 == 0:
                        print("ERROR: Resultado imaginario.")
                    elif ind == 0:
                        print("ERROR: El Indice no puede ser cero.")
                    else:
                        print(f"Resultado: {num ** (1/ind)}")

                case "4":
                    num = float(input("Base: "))
                    exp = float(input("Exponente: "))
                    print(f"Resultado: {math.pow(num, exp)}")

                case "5":
                    n = int(input("Numero entero para factorial: "))
                    if n < 0: print("ERROR: No existe factorial de negativos.")
                    else: print(f"El factorial de {n} es: {math.factorial(n)}")

                case "6":
                    n = int(input("¿Cuantos numeros de la serie desea ver?: "))
                    print(f"Serie: {calcular_fibonacci(n)}")

                case "7":
                    a = int(input("Primer numero (entero): "))
                    b = int(input("Segundo numero (entero): "))
                    print(f"M.C.M de {a} y {b} es: {math.lcm(a, b)}")

                case "8":
                    a = int(input("Primer numero (entero): "))
                    b = int(input("Segundo numero (entero): "))
                    print(f"M.C.D de {a} y {b} es: {math.gcd(a, b)}")

                case "9":
                    monto = float(input("Monto base: "))
                    tasa = float(input("Porcentaje de IVA (ej. 19): "))
                    iva = monto * (tasa / 100)
                    print(f"IVA: {iva} | Total: {monto + iva}")

                case "0":
                    print("Gracias por usar la calculadora. ¡Hasta luego!")
                    break

                case _:
                    print("Opcion fuera de rango (0-9). Reintente.")

        except ValueError:
            print("ERROR: Entrada invalida. Por favor, use solo numeros.")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_calculadora()