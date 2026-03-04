class OperacionesMatriciales:
    """Clase para realizar operaciones con matrices y vectores."""

    def crear_matriz(self, filas, columnas, auto=False):
        """Crea una matriz basada en la entrada del usuario o inicializada en cero."""
        if auto:
            return [[0 for _ in range(columnas)] for _ in range(filas)]
        
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(input(f"Ingrese valor para [{i}][{j}]: "))
                fila.append(valor)
            matriz.append(fila)
        
        # Mostramos la matriz recién creada para confirmación
        print("\nMatriz ingresada:")
        self.imprimir_matriz(matriz)
        return matriz

    def imprimir_matriz(self, M):
        """Muestra la matriz en formato de cuadrícula."""
        if isinstance(M, str): # Por si recibe un mensaje de error
            print(M)
            return
            
        for fila in M:
            # Formateamos cada número a 2 decimales y espacio de 8 caracteres
            print("[" + " ".join(f"{val:8.2f}" for val in fila) + "]")
        print()

    def sumar_matrices(self, A, B):
        """Suma dos matrices de las mismas dimensiones."""
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            return "Error: Dimensiones incompatibles."
        
        filas, cols = len(A), len(A[0])
        resultado = self.crear_matriz(filas, cols, auto=True)
        for i in range(filas):
            for j in range(cols):
                resultado[i][j] = A[i][j] + B[i][j]
        return resultado

    def multiplicar_matrices(self, A, B):
        """Realiza el producto de dos matrices."""
        if len(A[0]) != len(B):
            return "Error: El número de columnas de A debe ser igual a las filas de B."
        
        filas_A, cols_A = len(A), len(A[0])
        cols_B = len(B[0])
        
        resultado = [[0 for _ in range(cols_B)] for _ in range(filas_A)]
        for i in range(filas_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    resultado[i][j] += A[i][k] * B[k][j]
        return resultado

    def producto_matriz_vector(self, M, V):
        """Multiplica una matriz por un vector."""
        if len(M[0]) != len(V):
            return "Error: Dimensiones incompatibles."
        
        resultado = [0 for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(V)):
                resultado[i] += M[i][j] * V[j]
        return resultado

    def invertir_matriz(self, M):
        """Cálculo de la inversa mediante el método de Gauss-Jordan."""
        n = len(M)
        if n != len(M[0]): return "Error: Debe ser cuadrada."
        
        identidad = [[float(i == j) for j in range(n)] for i in range(n)]
        copia = [fila[:] for fila in M]

        for i in range(n):
            pivote = copia[i][i]
            if pivote == 0: return "Error: Matriz no invertible."
            for j in range(n):
                copia[i][j] /= pivote
                identidad[i][j] /= pivote
            for k in range(n):
                if k != i:
                    factor = copia[k][i]
                    for j in range(n):
                        copia[k][j] -= factor * copia[i][j]
                        identidad[k][j] -= factor * identidad[i][j]
        return identidad