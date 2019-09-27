
#rut, nombre, activo/inactivo, comuna
#buscar por rut
#Comunas : concepcion, talcahuano, hualpen

from os import system
system("cls")

nombres=[]
rut=[]
act=[]
comuna=[]

nombres.append("wladimir")
rut.append("20194705-7")
act.append("activo")
comuna.append("concepcion")

nombres.append("wacoldo")
rut.append("40")
act.append("activo")
comuna.append("hualpen")

nombres.append("soila")
rut.append("41")
act.append("activo")
comuna.append("talcahuano")

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
    r = str(input("ingrese el rut: "))
    
    for i in range(len(nombres)):
        n = i+1
        ru =str(f"{rut[i]}")
        
        if r == ru:
            print(f"Persona {n}: {nombres[i]} {rut[i]} {act[i]} {comuna[i]}")
            nombres[i]=input("ingrese nuevo nombre :")
            act[i]=input("actividad nueva: ")
            comuna[i]=input("nueva comuna : ")
            print(f"""Los datos se an cambiado por:
            {nombres[i]} {rut[i]} {act[i]} {comuna[i]}""")
    
def Eliminar():
    r = str(input("ingrese el rut: "))
    
    for i in range(len(nombres)):
        n = i+1
        ru =str(f"{rut[i]}")
        
        if r == ru:
            print(f"""Los datos que se borraran:
            {nombres[i]} {rut[i]} {act[i]} {comuna[i]}""")
            input()
            nombres.pop(i)
            rut.pop(i)
            comuna.pop(i)
            act.pop(i)
            print("Datos borrados")
            
    
def Buscar():
    r = str(input("ingrese el rut: "))
    
    for i in range(len(nombres)):
        n = i+1
        ru =str(f"{rut[i]}")
        
        if r == ru:
            print(f"Persona {n}: {nombres[i]} {rut[i]} {act[i]} {comuna[i]}")
        
           
    
    
def ContarInac():
    for i in range(len(rut)):
        ac=str(f"{act[i]}")
        if ac=="inactivo":
            n=i+1
        else:
            n=0
        print(f"Total de personas inactivas: {n}")
def ContarComun():
        
  
    for i in range(len(rut)):
        co=str(f"{comuna[i]}")
        if co=="concepcion" or co=="hualpen" or co=="talcahuano": 
                n=i+1
        else:
            n=0
    print(f"""El total de personas dentro de las comunas de
            (concepcion,talcahuano y hualpen : {n})""")        
        


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
        