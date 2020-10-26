#P4 E4 - rgion
#Pida al usuario tres números y un cuarto número, y compruebe si éste
#último es divisor de los tres números primeros.
numero1=float(input("Introduzca el primer número "))
numero2=float(input("Introduzca el segundo número "))
numero3=float(input("Introduzca el tercero número "))
numero4=float(input("Introduzca el cuarto número "))
if(numero1%numero4==0):
    print("El" ,numero4, "es divisor de" ,numero1)
if(numero2%numero4==0):
    print("El" ,numero4, "es divisor de" ,numero2)
if(numero3%numero4==0):
    print("El" ,numero4, "es divisor de" ,numero3)
