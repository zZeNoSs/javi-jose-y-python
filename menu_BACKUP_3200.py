<<<<<<< HEAD
from operaciones import sumar, restar, multiplicar, dividir, factorial_iterativo
=======
# menu.py
from operaciones import factorial_recursivo
>>>>>>> feature/factorial_recursivo

def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial de un número (iterativo)")
<<<<<<< HEAD
    opcion = input("Seleccione una opción: ")
    return opcion

def ejecutar_operacion(opcion):
    if opcion == '5':
        print("Saliendo del programa...")
        return False

    if opcion == '6':
        a = int(input("Ingrese un número: "))
=======
    print("6- Calcular el factorial de un número (recursivo)")
    opcion = input("Seleccione una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == '1':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
>>>>>>> feature/factorial_recursivo
        try:
            resultado = factorial_iterativo(a)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(e)
        return True

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
<<<<<<< HEAD
        elif opcion == '4':
            resultado = dividir(a, b)
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida")
            return True
    except ValueError as e:
        print(e)
    return True
=======
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
>>>>>>> feature/factorial_recursivo
