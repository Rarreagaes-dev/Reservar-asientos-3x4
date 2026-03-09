# Sistema de Reserva de Asientos de Cine
# 3 filas y 4 columnas

sala = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

while True:

    print("----- Bienvenido al Sistema de Reserva de Asientos -----")
    print("----- Menu Principal -----")
    print("1. Lista de Asientos disponibles")
    print("2. Comprar un asiento")
    print("3. Salir")

    opcion = int(input("Ingrese una opcion (1, 2, 3): "))

    if opcion == 1:

        print("----- Lista de Asientos -----")

        for fila in sala:
            print(fila)

        print("-----------------------------")

    elif opcion == 2:

        print("----- Compra de Asientos -----")

        fila = int(input("Ingrese la fila (1, 2, 3): "))
        columna = int(input("Ingrese la columna (1, 2, 3, 4): "))

        # convertir a indice de matriz
        fila -= 1
        columna -= 1

        # validar rango
        if fila < 0 or fila > 2 or columna < 0 or columna > 3:
            print("Asiento fuera de rango")
            continue

        # verificar si esta reservado
        if sala[fila][columna] == 1:
            print("Lo sentimos, el asiento ya esta reservado")
        else:
            sala[fila][columna] = 1
            print("Se reservo con exito")

    elif opcion == 3:

        print("Gracias por usar el sistema.")
        break

    else:
        print("Opcion no valida")