#P4 E3 - rgion
#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado,
#y pida los datos según que caso y muestre el resultado


area=input("Introduzca la figura geométrica de la cual quiere calcular su área ")
if(area=="triángulo"):
    base=float(input("Introduzca la base "))
    altura=float(input("Introduzca la altura "))
    area=(base*altura)/2
    print("El área del triángulo es" ,area,)
if(area=="cuadrado"):
    lado=float(input("Introduzca la longitud del lado "))
    area=lado**2
    print("El área del cuadrado es" ,area,)
