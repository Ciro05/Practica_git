def Ope (num1, num2):
    
    if resp == 1:
        resultado = num1+num2
        
    elif resp ==2:
        resultado = num1 - num2
        
    elif resp == 3:
        resultado = num1 * num2
        
    elif resp == 4:
        resultado = num1 / num2
    else: 
        print("Favor de ingresar una opcion valida")
    
    return resultado

resp = int(input("Cual es la operacion que quieres realizar? No.1 suma, No.2 resta, No.3 multiplicación, No.4 Division "))

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

Rs_ope = Ope (num1, num2)
print(f"El resultado de la operacion es:  {Rs_ope}")
        