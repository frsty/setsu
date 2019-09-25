from os import system
system("cls")

nombres=[]
apellidos=[]

nombres.append("wacoldo")
nombres.append("diogenes")
nombres.append("amada")

apellidos.append("soto")
apellidos.append("carrasco")
apellidos.append(input("ingrese apellido:"))



for i in range(len(nombres)):
    n=i+1
    print(f"Persona {n}: {nombres[i]} {apellidos[i]}")