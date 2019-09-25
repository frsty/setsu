
#rut, nombre, activo/inactivo, comuna
#buscar por rut
#Comunas : concepcion, talcahuano, hualpen

from os import system

nombres=[]
rut=[]
act=[]
comuna=[]

def Pausa():
    print("Apreta algo loko")
    input()
    system("cls")


def Ingresar():
    rut.append(input("ingrese el rut: "))
    nombres.append(input("Ingrese el nombre: "))
    act.append(input("ingrese si esta activo o inactivo: "))
    comuna.append(input("ingrese la comuna: "))

    
def Modificar():
    pass
def Eliminar():
    pass
def Buscar():
    r = str(input("ingrese el rut: "))
    
    for i in range(len(nombres)):
        n = i+1
        ru =str(f"{rut[i]}")
        
        if r == ru:
             print(f"Persona {n}: {nombres[i]} {rut[i]} {act[i]} {comuna[i]}")
        else:
            print("No existe esa persona :C") 
           
    
    
def ContarInac():
    pass
def ContarComun():
    pass


def Menu():
    print("""1.Ingresar Cliente
2.Modificar cliente
3.Eliminar cliente
4.Buscar cliente
5.Contar Clientes Inactivos
6.Contar clientes comuna
0.Salir""")
    


system("cls")

while True:
    Menu()
    op = int(input("Seleccione algo wacho:"))
    if op==1:
        Ingresar()
    elif op==2:
        Modificar()
    elif op==3:
        Eliminar()
    elif op==4:
        Buscar()
    elif op==5:
        ContarInac()
    elif op==6:
        ContarComun()
    elif op==0:
        print("Hasta la proximaaaaaaaa")
        input()
        break
    else:
        print("No esta bien")
    
    Pausa()
        