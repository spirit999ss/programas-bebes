#Convertidor de Peso/Masa
print("..............................................")
print("..............................................")
print("..............................................")
print("Bienvenido a el Convertidor de Peso/Masa:) ")
def Peso   ():    
    while True :
        try :
            print("..............................................")
            cantidad= int(input(" Ingresa la Cantidad a Convertir : "))
            break
        except ValueError :
            print("..............................................")
            print ("Ingresa un Numero por Favor :(  ") 
    while True :
        print("..............................................")
        print("Puedes Hacer Cualquiera de las Siguientes Conversiones : ")
        print(" Miligramos(M), Gramos(G) , Kilogramos(KG) , Libras(L) , Onzas(O) y Toneladas(T)")
        conversion=input("Ingrese el Diminutivo a Convertir EJM Si Desea Convertir a todas la unidades con Miligramos  = M : ").lower()
        while len(conversion) == 3 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Miligramos  
        if conversion ==  "m" : 
            m =cantidad * 0.001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} gramos")
            print("..............................................")
            m = cantidad  * 0.000001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} kg")
            print("..............................................")
            m = cantidad * 0.00000220462
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} libras")
            print("..............................................")
            m = cantidad  * 0.00003527396
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} onz")
            print("..............................................")
            m = cantidad * 0.000000001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} t")
            print("..............................................")
            break 
        #Todas las Conversiones con Gramos  
        elif conversion ==  "g" : 
            g =cantidad * 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {g} mg")
            print("..............................................")
            g = cantidad * 0.001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {g} kg")
            print("..............................................")
            g = cantidad  * 0.00220462
            print("..............................................")
            print(f"El Resultado de la Conversion es : {g} libras")
            print("..............................................")
            g = cantidad  * 0.03527396
            print("..............................................")
            print(f"El Resultado de la Conversion es : {g} onz")
            print("..............................................")
            g = cantidad * 0.000001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {g} t")
            print("..............................................")
            break 
        #Todas las Conversiones con Kilogramos  
        elif conversion == "kg" :
            kg = cantidad  * 1000000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kg} mg")
            print("..............................................")
            kg =cantidad * 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kg} gramos")
            print("..............................................")
            kg = cantidad * 2.20462262185
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kg} libras")
            print("..............................................")
            kg = cantidad   * 35.27396
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kg} onz")
            print("..............................................")
            kg = cantidad * 0.001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kg} t")
            print("..............................................")
            break 
        #Todas las Conversiones con libras  
        elif conversion == "l" :
            l = cantidad  * 453592.37
            print("..............................................")
            print(f"El Resultado de la Conversion es : {l} mg")
            print("..............................................")
            l =cantidad * 453.59237
            print("..............................................")
            print(f"El Resultado de la Conversion es : {l} gramos")
            print("..............................................")
            l = cantidad * 0.45359237
            print("..............................................")
            print(f"El Resultado de la Conversion es : {l} kg")
            print("..............................................")
            l = cantidad    * 16
            print("..............................................")
            print(f"El Resultado de la Conversion es : {l} onz")
            print("..............................................")
            l = cantidad * 0.00045359237
            print("..............................................")
            print(f"El Resultado de la Conversion es : {l} t")
            print("..............................................")
            break
        #Todas las Conversiones con Onzas  
        elif conversion == "o" :
            o = cantidad  * 28349.5231
            print("..............................................")
            print(f"El Resultado de la Conversion es : {o} mg")
            print("..............................................")
            o =cantidad * 28.34952
            print("..............................................")
            print(f"El Resultado de la Conversion es : {o} gramos")
            print("..............................................")
            o = cantidad * 0.0283495
            print("..............................................")
            print(f"El Resultado de la Conversion es : {o} kg")
            print("..............................................")
            o = cantidad    * 0.0625
            print("..............................................")
            print(f"El Resultado de la Conversion es : {o} libras")
            print("..............................................")
            o = cantidad * 0.0000283495231
            print("..............................................")
            print(f"El Resultado de la Conversion es : {o} t")
            print("..............................................")
            break
        #Todas las Conversiones con Toneladas  
        elif conversion == "t" :
            t = cantidad  * 1000000000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {t} mg")
            print("..............................................")
            t =cantidad * 1000000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {t} gramos")
            print("..............................................")
            t = cantidad * 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {t} kg")
            print("..............................................")
            t = cantidad    * 2204.62262185
            print("..............................................")
            print(f"El Resultado de la Conversion es : {t} libras")
            print("..............................................")
            t = cantidad * 35273.96195
            print("..............................................")
            print(f"El Resultado de la Conversion es : {t} onz")
            print("..............................................")
            break
      
            
Peso ()

#Se Pregunta al Usuario SI Quiere Seguir con el convertidos
resultado =input("Ingrese un Espacio y ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    Peso ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS") 
    break

                
                
