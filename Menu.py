
def mostrar_menu():
    opc  = [0,1,2,3,4,5,6,7,8,9,10]
    print("\n¿Que punto deseas mostrar? (1 -> 10)")
    print("(0) para finalizar busqueda. \n")
    while True:
        try:
            response = int(input())
            if response in opc:
                break
            else:
                print("¡Porfavor ingrese una opcion valida! \n")
                continue
        except:
            print("¡Porfavor ingrese una opcion valida! \n")
        
    return response

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            pass
        elif opcion == 2:
            import punto2
        elif opcion == 3:
            pass
        elif opcion == 4:
            import punto4
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            pass
        elif opcion == 10:
            pass
        elif opcion == 0:
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
