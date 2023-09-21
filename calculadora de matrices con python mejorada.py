import numpy as np

print("BIENVENIDO A LA CALCULADORA DE MATRICES CON PYTHON")
print("Servicios que ofrecemos:\n - SUMA\n - RESTA\n - MULTIPLICACION\n - TRANSPUESTA\n - INVERSA\n - DETERMINANTE")

operacion = input("INGRESA LA OPERACIÓN QUE DESEAS REALIZAR (En minúsculas POR FAVOR): ")
print()

# Función para leer una matriz desde la entrada estándar
def leer_matriz():
    R = int(input("Ingrese el número de reglones: "))
    C = int(input("Ingrese el número de columnas: "))
    matriz = np.zeros((R, C))

    print("Introduzca los datos de la matriz: ")
    for r in range(R):
        for c in range(C):
            valor = float(input("Reglón {}, Columna {}: ".format(r + 1, c + 1)))
            matriz[r, c] = valor

    return matriz

# ----------------------------------------------SUMA-------------------------------------------

if operacion == "suma":
    matriz1 = leer_matriz()
    matriz2 = leer_matriz()

    if matriz1.shape != matriz2.shape:
        print("No se pueden sumar matrices de diferentes dimensiones.")
    else:
        resultado = matriz1 + matriz2
        print("Resultado de la suma:")
        print(resultado)

# --------------------------------------------RESTA--------------------------------------------

elif operacion == "resta":
    matriz1 = leer_matriz()
    matriz2 = leer_matriz()

    if matriz1.shape != matriz2.shape:
        print("No se pueden restar matrices de diferentes dimensiones.")
    else:
        resultado = matriz1 - matriz2
        print("Resultado de la resta:")
        print(resultado)

# --------------------------------------MULTIPLICACION-----------------------------------------

elif operacion == "multiplicacion":
    matriz1 = leer_matriz()
    matriz2 = leer_matriz()

    if matriz1.shape[1] != matriz2.shape[0]:
        print("No se pueden multiplicar matrices con dimensiones incompatibles.")
    else:
        resultado = np.dot(matriz1, matriz2)
        print("Resultado de la multiplicación:")
        print(resultado)

# -----------------------------------------DETERMINANTE----------------------------------------

elif operacion == "determinante":
    n = int(input("Ingrese el orden de la matriz (solo matrices cuadradas): "))
    if n <= 0:
        print("El orden de la matriz debe ser un número positivo mayor que cero.")
    else:
        matriz = leer_matriz()

        if matriz.shape != (n, n):
            print("La matriz no es cuadrada.")
        else:
            determinante = np.linalg.det(matriz)
            print("La determinante de la matriz es:", determinante)

# ----------------------------------------TRANSPUESTA------------------------------------------

elif operacion == "transpuesta":
    matriz = leer_matriz()
    matriz_transpuesta = np.transpose(matriz)
    print("MATRIZ TRANSPUESTA:")
    print(matriz_transpuesta)

# ------------------------------------------INVERSA--------------------------------------------

elif operacion == "inversa":
    n = int(input("Ingrese el orden de la matriz (solo matrices cuadradas): "))
    if n <= 0:
        print("El orden de la matriz debe ser un número positivo mayor que cero.")
    else:
        matriz = leer_matriz()

        if matriz.shape != (n, n):
            print("La matriz no es cuadrada.")
        else:
            try:
                matriz_inversa = np.linalg.inv(matriz)
                print("MATRIZ INVERSA:")
                print(matriz_inversa)
            except np.linalg.LinAlgError:
                print("La matriz no tiene inversa.")

else:
    print("Lo siento, no puedo realizar esa operación.")
print("NO OLVIDES EL MARCO TEORICO POR FAVOR")