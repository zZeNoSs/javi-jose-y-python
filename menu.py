# menu.py
from operaciones import sumar, restar, multiplicar, dividir

def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def ejecutar_operacion(opcion):
    if opcion == '5':
        print("Saliendo del programa...")
        return False

    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    try:
        if opcion == '1':
            resultado = sumar(a, b)
            print(f"Resultado: {resultado}")
        elif opcion == '2':
            resultado = restar(a, b)
            print(f"Resultado: {resultado}")
        elif opcion == '3':
            resultado = multiplicar(a, b)
            print(f"Resultado: {resultado}")
        elif opcion == '4':
            resultado = dividir(a, b)
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida")
            return True
    except ValueError as e:
        print(e)
    return True
