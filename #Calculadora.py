#Calculadora
print("Bienvenido a la Calculadora")
Nombre = input("Ingrese su Nombre : ")
def calculadora (): 
  #El Programa continua solo si el Usuario ingresa un Numero
    while True :
        try :
            num1= int(input(f"{Nombre} Ingresa el Primer Numero : "))
            break
        except ValueError :
            print (f"{Nombre} Ingresa un Numero por Favor :(  ")
            continue
    while True :
        try :
            num2= int(input(f"{Nombre} Ingresa el Segundo Numero : "))
            break
        except ValueError :
                print (f"{Nombre} Ingresa un Numero por Favor :(  ")
#Pedir al Usuario que Operacion va a Realizar
    while True :
        try :
            operacion =input("Ingrese que operacion va a Realizar : +,-,*,/: ")
        except ValueError :
            print (f"{Nombre} Ingresa una Operacion :( : ")
            continue
        if operacion == "+" :
            print(f"{Nombre} , El Resultado de La Suma es = ",num1 + num2)
            break
        elif   operacion == "-" :
                print(f"{Nombre} , El Resultado de La Resta es = ",num1 - num2)
                break
        elif   operacion == "*" :
                print(f"{Nombre} , El Resultado de La Multiplicacion es = ",num1 * num2)
                break
        elif   operacion == "/" :
                print(f"{Nombre} , El Resultado de La Division es = ",num1 / num2)
                break
#SE EJECUTA LA CALCULADORA
calculadora ()                

#Se Pregunta al Usuario SI Quiere Seguir Calculando 
resultado =input("Presione ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    calculadora ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS")
    break



