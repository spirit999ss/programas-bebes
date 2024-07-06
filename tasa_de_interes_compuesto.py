#Calcular Tasa de Interes Compuesto
print("..............................................................")
print("Bienvenido a la Calculadora de Interes COMPUESTO")

def i_c (): 
     #El Programa continua solo si el Usuario ingresa un Numero
    while True :
        try :
            print("..............................................................")
            monto_p =int(input("Ingresa el Capital inicial : "))
            break
        except ValueError :
            print("..............................................................")
            print (" Ingresa un Numero por Favor :(  ")
            continue
    while True :
        try :
            print("..............................................................")
            tasa_de_interes= float(input(" Ingresa la Tasa de Interes: "))
            break
        except ValueError :
            print("..............................................................")
            print (" Ingresa un Numero por Favor :(  ")
            continue
    while True :
        try :
            print("..............................................................")
            tiempo= int(input(" Ingresa por cuanto  tiempo en año: "))
            break
        except ValueError :
            print("..............................................................")
            print (" Ingresa un Numero por Favor :(  ")
            continue
        
    #Formula para Calcular el Interes Compuesto
    i_c= monto_p * (tasa_de_interes + 1) **tiempo
    Is_re = round(i_c )  
    print(f" El Interes es ${Is_re}  ")
      
i_c ()

#Se Pregunta al Usuario SI Quiere Seguir Calculando 
resultado =input("Presione ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    i_c ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS")
    break
