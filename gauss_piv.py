import numpy as np

def gauss_piv(A, b, n, Piv):
    """
    GaussPiv: Calcula la solución de un sistema de ecuaciones Ax=b con diferentes tipos de pivoteo.
    
    Parámetros:
    A   - Matriz de coeficientes (nxn)
    b   - Vector de términos independientes (nx1)
    n   - Tamaño de la matriz (número de ecuaciones y variables)
    Piv - Tipo de pivoteo: 
          0 -> Sin pivoteo 
          1 -> Pivoteo parcial 
          2 -> Pivoteo total
    
    Retorna:
    x    - Vector de soluciones aproximadas
    mark - Vector que mantiene el orden de las columnas (para pivoteo total)
    """
    # Crear la matriz aumentada Ab combinando A y b
    Ab = np.hstack((A, b.reshape(-1, 1)))
    
    # Crear un marcador para hacer seguimiento del orden de las columnas en caso de pivoteo total
    mark = np.arange(n)
    
    # Proceso de eliminación de Gauss
    for k in range(n - 1):
        # Seleccionar el tipo de pivoteo a utilizar
        if Piv == 1:
            # Pivoteo parcial
            Ab = pivpar(Ab, n, k)
        elif Piv == 2:
            # Pivoteo total
            Ab, mark = pivtot(Ab, mark, n, k)
        
        # Eliminación hacia adelante
        for i in range(k + 1, n):
            M = Ab[i, k] / Ab[k, k]
            Ab[i, k:] = Ab[i, k:] - M * Ab[k, k:]
    
    # Resolver el sistema utilizando sustitución hacia atrás
    x = sustreg(Ab, n)
    
    return x, mark

def pivpar(Ab, n, k):
    """
    pivpar: Implementa el pivoteo parcial.
    Encuentra el mayor valor absoluto en la columna k desde la fila k hasta n y realiza el intercambio de filas.
    
    Parámetros:
    Ab - Matriz aumentada
    n  - Tamaño de la matriz
    k  - Columna actual (paso de la eliminación)
    
    Retorna:
    Ab - Matriz aumentada modificada con el pivoteo parcial realizado
    """
    # Encontrar el índice de la fila con el valor máximo en la columna k
    max_row_index = np.argmax(np.abs(Ab[k:, k])) + k
    if max_row_index != k:
        # Intercambiar la fila actual (k) con la fila del pivote máximo
        Ab[[k, max_row_index], :] = Ab[[max_row_index, k], :]
    
    return Ab

def pivtot(Ab, mark, n, k):
    """
    pivtot: Implementa el pivoteo total.
    Encuentra el mayor valor absoluto en la submatriz y realiza el intercambio de filas y columnas.
    
    Parámetros:
    Ab   - Matriz aumentada
    mark - Vector que mantiene el seguimiento de las columnas intercambiadas
    n    - Tamaño de la matriz
    k    - Columna actual (paso de la eliminación)
    
    Retorna:
    Ab   - Matriz aumentada modificada con el pivoteo total realizado
    mark - Vector de marcas actualizado para reflejar los intercambios de columnas
    """
    # Encontrar el índice de fila y columna con el valor máximo en la submatriz
    max_row, max_col = np.unravel_index(np.argmax(np.abs(Ab[k:, k:n]), axis=None), (n-k, n-k))
    max_row += k
    max_col += k
    
    # Intercambiar la fila k con la fila del pivote máximo
    if max_row != k:
        Ab[[k, max_row], :] = Ab[[max_row, k], :]
    
    # Intercambiar la columna k con la columna del pivote máximo
    if max_col != k:
        Ab[:, [k, max_col]] = Ab[:, [max_col, k]]
        # Actualizar el vector de marcas para reflejar el intercambio de columnas
        mark[[k, max_col]] = mark[[max_col, k]]
    
    return Ab, mark

def sustreg(Ab, n):
    """
    sustreg: Realiza la sustitución hacia atrás para resolver el sistema triangular superior.
    
    Parámetros:
    Ab - Matriz aumentada con el sistema triangular superior
    n  - Tamaño de la matriz (número de ecuaciones y variables)
    
    Retorna:
    x - Vector solución
    """
    x = np.zeros(n)
    
    # Sustitución hacia atrás
    for i in range(n-1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    
    return x


# Cálculo del error escalar
def calcular_error(A, x, b):
    """
    Calcula el error escalar relativo ||Ax - b|| / ||b||.
    
    Parámetros:
    A - Matriz de coeficientes
    x - Vector solución aproximada
    b - Vector de términos independientes
    
    Retorna:
    error_escalar - El error escalar relativo
    """
    error = np.linalg.norm(np.dot(A, x) - b) / np.linalg.norm(b)
    return error

# Ejemplo de uso:
if __name__ == "__main__":
    # Ejemplo de sistema de ecuaciones
    A = np.array([[9, -6, 6],
                  [2, -1, 4],
                  [7, -8, 19]], dtype=float)
    b = np.array([100, 200, 100], dtype=float)
    
    # Parámetros
    n = len(b)  # Número de variables
    Piv = 2     # 0 -> Sin pivoteo, 1 -> Pivoteo parcial, 2 -> Pivoteo total
    
    # Llamar a la función GaussPiv
    x, mark = gauss_piv(A, b, n, Piv)
    
    # Mostrar el resultado
    print("Solución:", x)
    print("Marcador de columnas (si hubo pivoteo total):", mark)

    x_reordenado = np.zeros_like(x)
    for i in range(n):
        x_reordenado[mark[i]] = x[i]

    # Calcular el error escalar
    error_escalar = calcular_error(A, x_reordenado, b)
    print("Error escalar:", error_escalar)


    print("Ax-b:", np.dot(A, x_reordenado) - b)

    print("Norma infinita de la solución:", np.linalg.norm(x_reordenado, np.inf))
