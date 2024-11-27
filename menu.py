from operaciones import sumar, restar, multiplicar, dividir, factorial_iterativo, factorial_recursivo

def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial de un número (iterativo)")
    print("7- Calcular el factorial de un número (recursivo)")
    opcion = input("Seleccione una opción: ")
    return opcion

def ejecutar_opcion(opcion):
    if opcion == '5':
        print("Saliendo del programa...")
        return False

    if opcion == '6': 
        a = int(input("Ingrese un número: "))
        try:
            resultado = factorial_iterativo(a)
            print(f"Resultado (iterativo): {resultado}")
        except ValueError as e:
            print(e)
        return True

    if opcion == '7': 
        a = int(input("Ingrese un número: "))
        try:
            resultado = factorial_recursivo(a)
            print(f"Resultado (recursivo): {resultado}")
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
        elif opcion == '4':
            resultado = dividir(a, b)
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida")
            return True
    except ValueError as e:
        print(e)
    
    return True
