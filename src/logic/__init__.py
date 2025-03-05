from logic import Logica

def main():
    logica = Logica()

    while True:
        print("\n=== OPERACIONES LÓGICAS ===")
        print("1. AND")
        print("2. OR")
        print("3. NOT")
        print("4. XOR")
        print("5. NAND")
        print("6. NOR")
        print("7. XNOR")
        print("8. Implicación")
        print("9. Bi-implicación")
        print("10. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "10":
            print("Saliendo del programa...")
            break

        if opcion in ["3"]:
            a = int(input("Ingrese el valor (0 o 1): "))
            print(f"Resultado: {logica.NOT(a)}")
        elif opcion in ["1", "2", "4", "5", "6", "7", "8", "9"]:
            a = int(input("Ingrese el primer valor (0 o 1): "))
            b = int(input("Ingrese el segundo valor (0 o 1): "))

            operaciones = {
                "1": logica.AND,
                "2": logica.OR,
                "4": logica.XOR,
                "5": logica.NAND,
                "6": logica.NOR,
                "7": logica.XNOR,
                "8": logica.implicacion,
                "9": logica.bi_implicacion
            }

            resultado = operaciones[opcion](a, b)
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
