#P4 E2 - rgion
#Pida al usuario 5 números y diga si estos estaban en orden decreciente,
#creciente o desordenados.

numero1=float(input("Introduzca el primer número "))
numero2=float(input("Introduzca el segundo número "))
numero3=float(input("Introduzca el tercero número "))
numero4=float(input("Introduzca el cuarto número "))
numero5=float(input("Introduzca el quinto número "))
if(numero1>numero2)and(numero2>numero3)and(numero3>numero4)and(numero4>numero5):
    print("Los números están en orden decreciente")
elif(numero1<numero2)and(numero2<numero3)and(numero3<numero4)and(numero4<numero5):
    print("Los números están en orden creciente")
else:
    print("Los números están desordenados")
    
