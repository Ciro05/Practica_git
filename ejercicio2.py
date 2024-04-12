def area (lado):
    Area = lado*lado
    return area
    
lado = int(input("Cuanto es el lado del cuadrado: "))

area_cua = area(lado)
print(f"El area del cuadrado con el lado de {lado}, es {lado*lado}") 