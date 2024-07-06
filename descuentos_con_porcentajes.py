#Caluladora de Descuento con Porcentaje
print("Bienvenido a la Calculadora de Descuento")
def d_p () :
    while True :
        try :
            precio_o = int(input(" Ingrese el Precio  : "))
            break
        except ValueError :
            print (" Ingresa un Numero por Favor :(  ")
            break
    while True :
        try :
            porcentaje= int(input(" Ingresa el Porcentaje a Descontar : "))
            break
        except ValueError :
            print (" Ingresa un Numero por Favor :(  ")
            break
    porcentaje_d = precio_o * (porcentaje / 100)
    precio_f1 = precio_o - porcentaje_d
    print (f"El Precio Final es {precio_f1}")

d_p ()

#Se Pregunta al Usuario SI Quiere Seguir Calculando 
resultado =input("Presione ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    d_p ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS")
    break