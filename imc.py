#Convertidor de IndIce de Masa Corporaral IMC
print("Bienvenido al Convertidor de IndIce de Masa Corporaral IMC")
nombre = input("Ingrese su Nombre : ")
def imc (): 
     #El Programa continua solo si el Usuario ingresa un Numero
    while True :
        try :
            peso= float(input(f"{nombre} Ingresa tu Peso en Kilogramos : "))
            break
        except ValueError :
            print (f"{nombre} Ingresa un Numero por Favor :(  ")
            continue
    while True :
        try :
            esta= float(input(f"{nombre} Ingresa tu Estatura en Metros: "))
            break
        except ValueError :
            print (f"{nombre} Ingresa un Numero por Favor :(  ")
            continue
    IMC= peso / (esta * esta)
    IMC_re = round(IMC, 2)
    if IMC < 18.5 :
        print(f"{nombre} Tu Indice de Masa Corporal es {IMC_re} Este Resultado indica  : BAJO PESO :( ")
    elif IMC == 18.5 or IMC < 25 :
        print(f"{nombre} Tu Indice de Masa Corporal es {IMC_re} Este Resultado indica : PESO NORMAL :) : ")
    elif IMC == 25 or IMC < 30 :
        print(f"{nombre} Tu Indice de Masa Corporal es {IMC_re} Este Resultado indica : SOBREPESO :( ")
    elif IMC >=  30 :
        print(f"{nombre} Tu Indice de Masa Corporal es {IMC_re} Este Resultado indica :  OBESIDAD :( ")
        
imc ()

#Se Pregunta al Usuario SI Quiere Seguir Calculando 
resultado =input("Presione ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    imc ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS")
    break
   
