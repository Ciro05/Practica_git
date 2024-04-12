def tabla (numero):
    for x in range(1,11):
        print (f"{numero}X{x} = {numero*x}")

tabla(int(input("Cual es la tabla que quieres: ")))


def area (lado):
    int(input("Cuanto es el lado del cuadrado: "))
    print (f"El area del cuadrado es: {lado*lado}")