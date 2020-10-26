#P4 E1 - rgion
#Pida al usuario 5 números y diga cual es el mayor y cuál el menor

numero1=float(input("Introduzca el primer número "))
numero2=float(input("Introduzca el segundo número "))
numero3=float(input("Introduzca el tercero número "))
numero4=float(input("Introduzca el cuarto número "))
numero5=float(input("Introduzca el quinto número "))

#opción más pensada, elimina muchas condiciones
maximo=minimo=numero1
if (numero2>maximo):
    maximo=numero2
else:
    if (numero2<minimo):
        minimo=numero2
if (numero3>maximo):
    maximo=numero3
else:
    if (numero3<minimo):
        minimo=numero3
if (numero4>maximo):
    maximo=numero4
else:
    if (numero4<minimo):
        minimo=numero4
if (numero5>maximo):
    maximo=numero5
else:
    if (numero5<minimo):
        minimo=numero5

    print(maximo, "es el mayor y" ,minimo, "es el menor")


#opción que suele hacer los principiantes
if(numero1==numero2==numero3==numero4==numero5):
    print("Todos los numeros son iguales")
else:
    if(numero1>numero2):
        mayor=numero1
        menor=numero2
    else:
        mayor=numero2
        menor=numero1
    if(numero3>mayor):
        mayor=numero3
    if(numero3<menor):
        menor=numero3
    if(numero4>mayor):
        mayor=numero4
    if(numero4<menor):
        menor=numero4
    if(numero5>mayor):
        mayor=numero5
    if(numero5<menor):
        menor=numero5
    print(mayor, "es el mayor y" ,menor, "es el menor")

    
    
