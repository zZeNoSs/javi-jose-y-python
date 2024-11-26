# menu.py
from operaciones import sumar, restar, multiplicar

def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
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
