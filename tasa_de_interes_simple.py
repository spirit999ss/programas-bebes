#Calcular Tasa de Interes de un PRESTAMO
print("..............................................................")
print("Bienvenido a la Calculadora de Tasa de Interes sea INVERSION o PRESTAMO")

def i_s (): 
     #El Programa continua solo si el Usuario ingresa un Numero
    while True :
        try :
            print("..............................................................")
            monto_p =int(input(" Ingresa el Monto de tu prestamo : "))
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
        
   #Formula para Calcular el Interes
    IS= monto_p *(tasa_de_interes /100) * tiempo
    Is_re = round(IS, 2)
    print(f" El Interes  es ${Is_re}  ")
      
i_s ()

#Se Pregunta al Usuario SI Quiere Seguir Calculando 
resultado =input("Presione ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    i_s ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS")
    break
