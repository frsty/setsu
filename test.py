#comentarios
'''varias lineas
de comentarios wacho'''

#CALCULADORA

from os import system

def Pausa():
    print("Apreta algo loko")
    input()
    system("cls")

def Sumar(a,b):
    print("Tu suma hermano ",str(a+b))
    
def Restar(a,b):
    print("Tu resta hermano ",str(a-b))
def Multiplicar(a,b):
    print("Tu multiplicacion hermano ",str(a*b))
def Dividir(a,b):
    print("Tu divicion hermano ",str(a/b))

def Menu():
    print("""SELECCIONE OPERACION
1.Suma
2.Restar
3.Multiplicar
4.Dividir
9.Salir""")

    
while True:
    num1=float(input("Ingrese un numero : "))
    num2=float(input("Ingrese otro numero: "))
    Menu()
    op= int(input("Ingrese su opcion: "))
    if op ==1:
        Sumar(num1,num2)
    elif op==2:
        Restar(num1,num2)
    elif op==3:
        Multiplicar(num1,num2)
    elif op==4:
        Dividir(num1,num2)
    elif op==9:
        print("Terminamos por hoy wacho")
        input()
        break
    else:
        print("Opcion no valida")
    
    Pausa()