import math
print ("Que operacion desea calcular.")
print(" Operaciones Basicas = 1\n Funciones trigonometricas = 2\n Raiz enesima = 3\n Potencia enecima = 4\n Factoriales = 5\n Fibonacci = 6\n M.C.M = 7\n M.C.D = 8\n IVA = 9")
operacion=int(input(" Ingrese una operacion de las mensionadas anteriormente: "))
if operacion < 0 or operacion > 9:
    
    print("ERROR")

else:

    if operacion == 1:

        print("Ingrese la operacion deseada.\n")
        print(" Suma = 1\n Resta = 2\n Multiplicacion = 3\n Divicion = 4")
        basico=int(input(" ingrese la operacion que desea hacer: "))
        if basico < 1 or basico > 4:
            print("ERROR")
        else:
            n1=float(input("Ingrese el primer numero: "))
            n2=float(input("ingrese el segundo numero: "))
            if basico == 1:
                
                suma=n1+n2
                print("El resultado es: ", suma)

            else:

                if basico == 2:
                   
                   resta=n1-n2
                   print("El resultado es: ", resta)

                else:

                    if basico == 3:

                        multiplicacion=n1*n2
                        print("El resultado es: ", multiplicacion)

                    else:

                        if basico==4:

                            if n2 <=0:

                                print("ERROR MATEMATICO")

                            else:

                                divicion=n1/n2
                                print("El resultado es: ", divicion)

    else:

        if operacion == 2:

            print(" Ingrese la operacion trigonometrica que desea calcular:")
            print(" Sen = 1\n Cos = 2\n Tan =3")
            trigo=int(input(" Su funcion trigonometrica es: "))
            if trigo < 1 or trigo > 3:
                print("ERROR")
            else:
                n1=float(input(" Ingrese el numero que desea operar: "))
                if trigo==1:
                    seno= math.sin(n1)
                    print("sen(",n1,")=",seno)
                else:
                    if trigo==2:
                        coseno=math.cos(n1)
                        print("cos(",n1,")=",coseno)
                    else:
                        if trigo==3:
                            tangente=math.tan(n1)
                            print("tan(",n1,")=",tangente)
        else:
            if operacion == 3:
                Nu=float(input(" Ingrese un numero positivo: "))
                r=int(input(" Ingrese el indice de la raiz: "))
                if Nu < 0:
                    print("ERROR EL RESULTADO ES UN NUMERO IMAGINARIO")
                else:
                    if r<=1:
                        print("\n ERROR MAT")
                    else:
                        raiz=math.pow(Nu,1/r)
                        print(" El resultado es: ",raiz)
            else:
                if operacion==4:
                    num=float(input(" Ingrese un numero: "))
                    exp=float(input(" Ingrese el exponente: "))
                    resul=math.pow(num,exp)
                    print(" El resultado es: ",resul)
                else:
                    if operacion==5:
                        fac=int(input(" Ingrese un numero para calcular el factorial: "))
                        if fac<0:
                            print(" INDEFINIDO")
                        else:
                            resul=math.factorial(fac)
                            print("el factorial de ",fac," es: ",resul)
                    else:
                        if operacion == 6 :
                            n=int(input(" Ingrese un n de la serie fibonacci: "))
                            def fibonacci(n):
                                a,b=0,1
                                for _ in range (n):
                                    print(a, end=" ")
                                    a,b = b ,a +b