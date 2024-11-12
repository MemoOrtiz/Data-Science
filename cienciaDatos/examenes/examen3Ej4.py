def es_par_o_impar(numero):
    
    if(numero % 2 == 0):
        print("Es par")
    print("Es impar")

#condicion = 999
numero = 1
while(numero != 0):
    numero = int(input("Ingresa un numero (0 para salir): "))
    if numero == 0:
        break
    es_par_o_impar(numero)
    