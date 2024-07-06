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
        conversion=input("Ingrese los Diminutivo a Convertir EJM Si Desea Convertir de Miligramos  a Kilogramos = MK : ").lower()
        while len(conversion) == 1 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Miligramos  
        if conversion ==  "mg" : 
            mg =cantidad * 0.001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mg} gramos")
            print("..............................................")
            break
        elif conversion == "mkg" :
            mkg = cantidad  * 0.000001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mkg} kg")
            print("..............................................")
            break
        elif conversion == "ml" :
            ml = cantidad * 0.00000220462
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ml} libras")
            print("..............................................")
            break
        elif conversion == "mo" :
            mo = cantidad  * 0.00003527396
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mo} onz")
            print("..............................................")
            break 
        elif conversion == "mt" :
            mt = cantidad * 0.000000001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mt} t")
            print("..............................................")
            break 
        #Todas las Conversiones con Gramos  
        elif conversion ==  "gm" : 
            gm =cantidad * 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gm} mg")
            print("..............................................")
            break
        elif conversion == "gkg" :
            gkg = cantidad * 0.001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gkg} kg")
            print("..............................................")
            break
        elif conversion == "gl" :
            gl = cantidad  * 0.00220462
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gl} libras")
            print("..............................................")
            break
        elif conversion == "go" :
            go = cantidad  * 0.03527396
            print("..............................................")
            print(f"El Resultado de la Conversion es : {go} onz")
            print("..............................................")
            break 
        elif conversion == "gt" :
            gt = cantidad * 0.000001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gt} t")
            print("..............................................")
            break 
        #Todas las Conversiones con Kilogramos  
        elif conversion == "kgm" :
            kgm = cantidad  * 1000000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kgm} mg")
            print("..............................................")
            break
        elif conversion ==  "kgg" : 
            kgg =cantidad * 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kgg} gramos")
            print("..............................................")
            break
        elif conversion == "kgl" :
            kgl = cantidad * 2.20462262185
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kgl} libras")
            print("..............................................")
            break
        elif conversion == "kgo" :
            kgo = cantidad   * 35.27396
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kgo} onz")
            print("..............................................")
            break 
        elif conversion == "kgt" :
            kgt = cantidad * 0.001
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kgt} t")
            print("..............................................")
            break 
        #Todas las Conversiones con libras  
        elif conversion == "lm" :
            lm = cantidad  * 453592.37
            print("..............................................")
            print(f"El Resultado de la Conversion es : {lm} mg")
            print("..............................................")
            break
        elif conversion ==  "lg" : 
            lg =cantidad * 453.59237
            print("..............................................")
            print(f"El Resultado de la Conversion es : {lg} gramos")
            print("..............................................")
            break
        elif conversion == "lkg" :
            lkg = cantidad * 0.45359237
            print("..............................................")
            print(f"El Resultado de la Conversion es : {lkg} kg")
            print("..............................................")
            break
        elif conversion == "lo" :
            lo = cantidad    * 16
            print("..............................................")
            print(f"El Resultado de la Conversion es : {lo} onz")
            print("..............................................")
            break 
        elif conversion == "lt" :
            lt = cantidad * 0.00045359237
            print("..............................................")
            print(f"El Resultado de la Conversion es : {lt} t")
            print("..............................................")
            break
        #Todas las Conversiones con Onzas  
        elif conversion == "om" :
            om = cantidad  * 28349.5231
            print("..............................................")
            print(f"El Resultado de la Conversion es : {om} mg")
            print("..............................................")
            break
        elif conversion ==  "og" : 
            og =cantidad * 28.34952
            print("..............................................")
            print(f"El Resultado de la Conversion es : {og} gramos")
            print("..............................................")
            break
        elif conversion == "okg" :
            okg = cantidad * 0.0283495
            print("..............................................")
            print(f"El Resultado de la Conversion es : {okg} kg")
            print("..............................................")
            break
        elif conversion == "ol" :
            ol = cantidad    * 0.0625
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ol} libras")
            print("..............................................")
            break 
        elif conversion == "ot" :
            ot = cantidad * 0.0000283495231
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ot} t")
            print("..............................................")
            break
        #Todas las Conversiones con Toneladas  
        elif conversion == "tm" :
            tm = cantidad  * 1000000000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tm} mg")
            print("..............................................")
            break
        elif conversion ==  "tg" : 
            tg =cantidad * 1000000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tg} gramos")
            print("..............................................")
            break
        elif conversion == "tkg" :
            tkg = cantidad * 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tkg} kg")
            print("..............................................")
            break
        elif conversion == "tl" :
            tl = cantidad    * 2204.62262185
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tl} libras")
            print("..............................................")
            break 
        elif conversion == "to" :
            to = cantidad * 35273.96195
            print("..............................................")
            print(f"El Resultado de la Conversion es : {to} onz")
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

                
                
