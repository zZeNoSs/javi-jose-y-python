# operaciones.py
def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        b_int = int(abs(b))
        resultado = 0

        for _ in range(b_int):
            resultado += a

        if b < 0:
            resultado = -resultado

        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def dividir(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b == 0:
            raise ValueError("El divisor no puede ser cero")
        resultado = 0
        while a >= b:
            a -= b
            resultado += 1
        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser int o float")
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> feature/fibonacci
def factorial_iterativo(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El valor debe ser un entero no negativo")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
<<<<<<< HEAD
=======
def factorial_recursivo(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El valor debe ser un entero no negativo")
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
o
>>>>>>> feature/factorial_recursivo
=======

def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("El valor debe ser un entero")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
>>>>>>> feature/fibonacci
