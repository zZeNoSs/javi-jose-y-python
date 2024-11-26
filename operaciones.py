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
        resultado = 0
        for _ in range(abs(b)):
            resultado += a
        return resultado if b >= 0 else -resultado
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
