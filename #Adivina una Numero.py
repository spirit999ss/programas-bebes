#Adivina un Numero
import random 
print("..............................................")
print("..............................................")
print("..............................................")
print("Bienvenido al Juego Adivina un Numero")
Nombre = input("Ingrese su Nombre : ")
def Adivina ():
    num_r = random.randint(1,100) 
    while True :
        try:
            print("..............................................")
            num_a=int(input(f"{Nombre} Estoy Pensando un Numero del 1 al 100 ¡ADIVINALO! : "))
        except ValueError:
            print (" :( Ingresa un Numero por Favor :(  ")
            continue
        if  num_r  > num_a :
            print("..............................................")
            print(f"{Nombre} El Numero es mas Alto :) ")
        elif num_r < num_a :
            print("..............................................")
            print(f"{Nombre} El Numero es mas Bajo :) ")     
        else :
            print("..............................................")
            print("..............................................")
            print("..............................................")
            print("Adivinaste :) ")
            print("..............................................")
            print("..............................................")
            print("..............................................")

            break 

Adivina()
#Se Pregunta al Usuario SI Quiere Seguir JUGANDO 
resultado =input("Presione ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    Adivina ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS")
    break


    