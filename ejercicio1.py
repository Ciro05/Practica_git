def tabla (numero):
    for x in range(1,11):
        print (f"{numero}X{x} = {numero*x}")

tabla(int(input("Cual es la tabla que quieres: ")))