# menu.py
from operaciones import factorial_recursivo

def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial de un número (iterativo)")
    print("6- Calcular el factorial de un número (recursivo)")
    opcion = input("Seleccione una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == '1':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        try:
            resultado = sumar(a, b)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '2':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        try:
            resultado = restar(a, b)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '3':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        try:
            resultado = multiplicar(a, b)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '4':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        try:
            resultado = dividir(a, b)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(e)
    elif opcion == '6':
        a = int(input("Ingrese un número: "))
        try:
            resultado = factorial_recursivo(a)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(e)
