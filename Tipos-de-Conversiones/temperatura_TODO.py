#Convertidor de Temperatura
print("..............................................")
print("..............................................")
print("..............................................")
print("Bienvenido a el Convertidor de Temperatura :) ")
def Temperatura   ():    
    while True :
        try :
            print("..............................................")
            cantidad= int(input(" Ingresa la Temperatura a Convertir : "))
            break
        except ValueError :
            print("..............................................")
            print ("Ingresa un Numero por Favor :(  ") 
    while True :
        print("..............................................")
        print("Puedes Hacer Cualquiera de las Siguientes Conversiones : ")
        print("Celsius (C) , Fahrenheit (F) , Kelvin (K) , Rankine (R) , Reaumur (Re) , Delisle(D), Newton (N)")
        conversion=input("Ingrese el Diminutivo a Convertir EJM Si Desea Convertir a todas la unidades con Fahrenheit=F : ").lower()
        while len(conversion) == 3 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Celsius 
        if conversion ==  "c" : 
            c= cantidad  * 1.8 + 32
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} °F")
            print("..............................................")
            c = cantidad + 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} K")
            print("..............................................")
            c = (cantidad * 9/5 )+ 491.67 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} °R")
            print("..............................................")
            c = cantidad  * 0.8
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} °Re")
            print("..............................................")
            c = (cantidad - 100 ) * 3/2 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-c} °De")
            print("..............................................")
            c = cantidad   * 0.33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} °N")
            print("..............................................")
            break
        #Todas las Conversiones con Fahrenheit  
        elif conversion ==  "f" : 
            f = (cantidad - 32) * 5/9
            print("..............................................")
            print(f"El Resultado de la Conversion es : {f} °C")
            print("..............................................")
            f = (cantidad -32) * 5/9 + 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {f} K")
            print("..............................................")
            f = cantidad + 459.67
            print("..............................................")
            print(f"El Resultado de la Conversion es : {f} °R")
            print("..............................................")
            f = (cantidad  - 32)/2.25
            print("..............................................")
            print(f"El Resultado de la Conversion es : {f} °Re")
            print("..............................................")
            f = (cantidad  - 212) * 5/6
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-f} °De")
            print("..............................................")
            f = (cantidad   - 32) * 11 / 60
            print("..............................................")
            print(f"El Resultado de la Conversion es : {f} °N")
            print("..............................................")
            break
         #Todas las Conversiones con Kelvin
        elif conversion ==  "k" : 
            k = cantidad  - 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} °C")
            print("..............................................")
            k = (cantidad - 273.15) * 9/5 + 32
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} °F")
            print("..............................................")
            k = cantidad * 1.8
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} °R")
            print("..............................................")
            k = (cantidad - 273.15) * 4/5
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} °Re")
            print("..............................................")
            k = (cantidad  - 373.15 ) * 3/2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-k} °De")
            print("..............................................")
            k = (cantidad   - 273.15 )* 0.33 / 100 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} °N")
            print("..............................................")
            break
        #Todas las Conversiones con rankine
        elif conversion == "r" :
            r =( cantidad  - 491.67) * 5 / 9
            print("..............................................")
            print(f"El Resultado de la Conversion es : {r} °C")
            print("..............................................")
            r = cantidad   - 459.67
            print("..............................................")
            print(f"El Resultado de la Conversion es : {r} °F")
            print("..............................................")
            r = cantidad / 1.8
            print("..............................................")
            print(f"El Resultado de la Conversion es : {r} K")
            print("..............................................")
            r = (cantidad  - 491.67) * 4 / 9
            print("..............................................")
            print(f"El Resultado de la Conversion es : {r} °Re")
            print("..............................................")
            r = (cantidad - 671.67) * 5 / 6
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-r} °De")
            print("..............................................")
            r = ((cantidad - 491.67) * 5 / 9) * 100 / 33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {r} °N")
            print("..............................................")
            break
         #Todas las Conversiones con Reaumur
        elif conversion == "re" :
            re = cantidad  * 1.25
            print("..............................................")
            print(f"El Resultado de la Conversion es : {re} °C")
            print("..............................................")
            re = cantidad  * 2.25 + 32
            print("..............................................")
            print(f"El Resultado de la Conversion es : {re} °F")
            print("..............................................")
            re = cantidad * 1.25 + 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {re} K")
            print("..............................................")
            re = (cantidad  * 9 / 4) + 491.67
            print("..............................................")
            print(f"El Resultado de la Conversion es : {re} °R")
            print("..............................................")
            re = (cantidad  -80) * 15 / 8
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-re} °De")
            print("..............................................")
            re = (cantidad * 33 / 80)
            print("..............................................")
            print(f"El Resultado de la Conversion es : {re} °N")
            print("..............................................")
            break
        #Todas las Conversiones con deslile   
        elif conversion == "d" :
            d = (cantidad  - 100) * 2 / 3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-d} °C")
            print("..............................................")
            d = 212 - (100 - cantidad ) * 6/5
            print("..............................................")
            print(f"El Resultado de la Conversion es : {d} °F")
            print("..............................................")
            d =  273.15 - (100 - cantidad)  * 2/3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {d} K")
            print("..............................................")
            d = (671.67 - cantidad) * 5 / 6
            print("..............................................")
            print(f"El Resultado de la Conversion es : {d} °R")
            print("..............................................")
            d = (cantidad  - 80) * 8 / 15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-d} °Re")
            print("..............................................")
            d = (33 - cantidad) * 100 / 50 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {d} °N")
            print("..............................................")
            break
        #Todas las Conversiones con Newton
        elif conversion == "n" :
            n = cantidad   * 100 /33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {n} °C")
            print("..............................................")
            n = cantidad   * 180 /33 +32
            print("..............................................")
            print(f"El Resultado de la Conversion es : {n} °F")
            print("..............................................")
            n = cantidad  * 100 / 33 + 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {n} K")
            print("..............................................")
            n = (cantidad * 180 / 33 + 32 + 459.67)
            print("..............................................")
            print(f"El Resultado de la Conversion es : {n} °R")
            print("..............................................")
            n = cantidad * 80 / 33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {n} °Re")
            print("..............................................")
            n = cantidad   * 100 / 33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {n} °De")
            print("..............................................")
            break

Temperatura   ()



#Se Pregunta al Usuario SI Quiere Seguir con el convertidos
resultado =input("Ingrese un Espacio y ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    Temperatura ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS") 
    break

        
        

