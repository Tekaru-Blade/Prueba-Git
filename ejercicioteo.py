suma = 0
for i in range(4):
    numero= int(input("Ingrese un número: "))
    suma += numero

    print("La suma es: ", suma)

    if suma>=0 and suma<=5:
        print("La suma es: ", suma, "y esta entre 0 y 5")
    elif suma>5 and suma<=10:
        print("La suma es: ", suma, "y esta entre 5 y 10")
    elif suma>10 and suma<=15:
        print("La suma es: ", suma, "y esta entre 10 y 15")