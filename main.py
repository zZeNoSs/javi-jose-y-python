# main.py
from menu import mostrar_menu, ejecutar_operacion

def main():
    while True:
        opcion = mostrar_menu()
        continuar = ejecutar_operacion(opcion)
        if not continuar:
            break

if __name__ == '__main__':
    main()
