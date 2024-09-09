def punto1():
    print("Ejercicio Punto 1")
    # Código para el ejercicio 14
def punto2():
    print("Ejercicio Punto 2")
    # Código para el ejercicio 2

def punto3():
    print("Ejercicio Punto 3")
    # Código para el ejercicio 3

def punto4():
    print("Ejercicio Punto4")
    # Código para el ejercicio 4
def punto5():
    print("Ejercicio Punto 5")
    # Código para el ejercicio 5

def punto6():
    print("Ejercicio Punto 6")
    # Código para el ejercicio 6

def punto7():
    print("Ejercicio Punto 7")
    # Código para el ejercicio 7

def punto8():
    print("Ejercicio Punto 8")
    # Código para el ejercicio 8

def punto9():
    print("Ejercicio Punto 9")
    # Código para el ejercicio 9

def punto10():
    print("Ejercicio Punto 10")
    # Código para el ejercicio 10

def mostrar_menu():
    print("Seleccione un punto de ejercicio (1-10) o 0 para salir:")
    print("1. Punto 1")
    print("2. Punto 2")
    print("3. Punto 3")
    print("4. Punto 4")
    print("5. Punto 5")
    print("6. Punto 6")
    print("7. Punto 7")
    print("8. Punto 8")
    print("9. Punto 9")
    print("10. Punto 10")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            punto1()
        elif opcion == '2':
            punto2()
        elif opcion == '3':
            punto3()
        elif opcion == '4':
            punto4()
        elif opcion == '5':
            punto5()
        elif opcion == '6':
            punto6()
        elif opcion == '7':
            punto7()
        elif opcion == '8':
            punto8()
        elif opcion == '9':
            punto9()
        elif opcion == '10':
            punto10()
        elif opcion == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, seleccione un número del 0 al 10.")

if __name__ == "__main__":
    main()
