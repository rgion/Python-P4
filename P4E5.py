#P4 E5 - rgion
#Pida al usuario un importe en euros y diga si el cajero automático
#le  puede dar dicho importe utilizando el mismo billete y el más
#grande(recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5€).
importe=int(input("Introduzca un importe "))
if(importe%500==0):
    billetes=importe/500
    print("El cajero devuelve" ,billetes, "de 500 euros")
elif(importe%200==0):
    billetes=importe/200
    print("El cajero devuelve" ,billetes, "de 200 euros")
elif(importe%100==0):
    billetes=importe/100
    print("El cajero devuelve" ,billetes, "de 100 euros")
elif(importe%50==0):
    billetes=importe/50
    print("El cajero devuelve" ,billetes, "de 50 euros")
elif(importe%20==0):
    billetes=importe/20
    print("El cajero devuelve" ,billetes, "de 20 euros")
elif(importe%10==0):
    billetes=importe/10
    print("El cajero devuelve" ,billetes, "de 10 euros")
elif(importe%5==0):
    billetes=importe/5
    print("El cajero devuelve" ,billetes, "de 5 euros")
