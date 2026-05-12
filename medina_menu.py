print("hola")
# programa principal de Menú de operciones, edades, salida, salir #
print("hola, bienvenidos al menu")
print("escoja una de las opciones del menu")

salir = 0

while salir == 0:

    print("MENU PRINCIPAL")
    print("1. Operaciones")
    print("2. Edades")
    print("3. Salir")

    op = input("Opción: ")

    if op == "3":
        print("Saliendo...")
        salir = 1

    elif op == "1":
        volver = 0
        while volver == 0:
            print("OPERACIONES")
            print("1. Sumar")
            print("2. Multiplicar")
            print("3. Volver")

            sub = input("Opción: ")

            if sub == "3":
                volver = 1

            elif sub == "1":
                a = int(input("Número 1: "))
                b = int(input("Número 2: "))
                print("Suma:", a + b)

            elif sub == "2":
                a = int(input("Número 1: "))
                b = int(input("Número 2: "))
                print("Multiplicación:", a * b)

            else:
                print("Opción inválida")

    elif op == "2":
        volver = 0
        while volver == 0:
            print("EDADES")
            print("1. Mayor o menor de edad")
            print("2. Promedio de 3 edades")
            print("3. Volver")

            sub = input("Opción: ")

            if sub == "3":
                volver = 1

            elif sub == "1":
                edad = int(input("Edad: "))
                if edad >= 18:
                    print("Mayor de edad")
                else:
                    print("Menor de edad")

            elif sub == "2":
                suma = 0
                for i in range(3):
                    e = int(input("Edad: "))
                    suma = suma + e
                print("Promedio:", suma / 3)

            else:
                print("Opción inválida")

    else:
        print("Opción inválida")