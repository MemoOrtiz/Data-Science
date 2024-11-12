condicion = "0"

# celsiud = (F -32) * (5/9)
# F = (C*9/5)+ 32

def cel_fah(celsius):
    fahrenheit =  (celsius * (9/5)) + 32
    print(str(celsius) + " = "+ str(fahrenheit))
    return fahrenheit

def fah_cel(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    print(str(fahrenheit) + " = " + str(celsius))
    return celsius

while condicion != 3:
    print(""" 
    1. Celsius a Fahrenheit
    2. Fahrenheit a Celsius
    3. Salir
    """)
    eleccion = input("Seleccione una opcion: ")
    condicion = int(eleccion)
    if condicion == 1:
        temp = int(input("Ingrese la temperatura: "))
        cel_fah(temp)
    if condicion == 2:
        temp = int(input("Ingrese la temperatura: "))
        fah_cel(temp)
    
