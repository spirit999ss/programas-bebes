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
        conversion=input("Ingrese los Diminutivo a Convertir EJM Si Desea Convertir de Celsius a Kelvin CK : ").lower()
        while len(conversion) == 1 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Celsius 
        if conversion ==  "cf" : 
            cf= cantidad  * 1.8 + 32
            print("..............................................")
            print(f"El Resultado de la Conversion es : {cf} °F")
            print("..............................................")
            break
        elif conversion == "ck" :
            ck = cantidad + 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ck} K")
            print("..............................................")
            break
        elif conversion == "cr" :
            cr = (cantidad * 9/5 )+ 491.67 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {cr} °R")
            print("..............................................")
            break
        elif conversion == "cre" :
            cre = cantidad  * 0.8
            print("..............................................")
            print(f"El Resultado de la Conversion es : {cre} °Re")
            print("..............................................")
            break
        elif conversion == "cd" :
            cd = (cantidad - 100 ) * 3/2 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-cd} °De")
            print("..............................................")
            break
        elif conversion == "cn" :
            csnw = cantidad   * 0.33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {csnw} °N")
            print("..............................................")
            break
        #Todas las Conversiones con Fahrenheit  
        elif conversion ==  "fc" : 
            fc = (cantidad - 32) * 5/9
            print("..............................................")
            print(f"El Resultado de la Conversion es : {fc} °C")
            print("..............................................")
            break
        elif conversion == "fk" : 
            fk = (cantidad -32) * 5/9 + 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {fk} K")
            print("..............................................")
            break
        elif conversion == "fr" :
            fr = cantidad + 459.67
            print("..............................................")
            print(f"El Resultado de la Conversion es : {fr} °R")
            print("..............................................")
            break
        elif conversion == "fre" :
            fre = (cantidad  - 32)/2.25
            print("..............................................")
            print(f"El Resultado de la Conversion es : {fre} °Re")
            print("..............................................")
            break
        elif conversion == "fd" :
            fd = (cantidad  - 212) * 5/6
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-fd} °De")
            print("..............................................")
            break
        elif conversion == "fn" :
            fn = (cantidad   - 32) * 11 / 60
            print("..............................................")
            print(f"El Resultado de la Conversion es : {fn} °N")
            print("..............................................")
            break
         #Todas las Conversiones con Kelvin
        elif conversion ==  "kc" : 
            kc = cantidad  - 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kc} °C")
            print("..............................................")
            break
        elif conversion == "kf" :
            kf = (cantidad - 273.15) * 9/5 + 32
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kf} °F")
            print("..............................................")
            break
        elif conversion == "kr" :
            kr = cantidad * 1.8
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kr} °R")
            print("..............................................")
            break
        elif conversion == "kre" :
            kre = (cantidad - 273.15) * 4/5
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kre} °Re")
            print("..............................................")
            break
        elif conversion == "kd" :
            kd = (cantidad  - 373.15 ) * 3/2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-kd} °De")
            print("..............................................")
            break
        elif conversion == "kn" :
            kn = (cantidad   - 273.15 )* 0.33 / 100 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kn} °N")
            print("..............................................")
            break
        #Todas las Conversiones con rankine
        elif conversion == "rc" :
            rc =( cantidad  - 491.67) * 5 / 9
            print("..............................................")
            print(f"El Resultado de la Conversion es : {rc} °C")
            print("..............................................")
            break
        elif conversion ==  "rf" : 
            rf= cantidad   - 459.67
            print("..............................................")
            print(f"El Resultado de la Conversion es : {rf} °F")
            print("..............................................")
            break
        elif conversion == "rk" :
            rk = cantidad / 1.8
            print("..............................................")
            print(f"El Resultado de la Conversion es : {rk} K")
            print("..............................................")
            break
        elif conversion == "rre" :
            rre = (cantidad  - 491.67) * 4 / 9
            print("..............................................")
            print(f"El Resultado de la Conversion es : {rre} °Re")
            print("..............................................")
            break
        elif conversion == "rd" :
            rd = (cantidad - 671.67) * 5 / 6
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-rd} °De")
            print("..............................................")
            break
        elif conversion == "rn" :
            rn = ((cantidad - 491.67) * 5 / 9) * 100 / 33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {rn} °N")
            print("..............................................")
            break
         #Todas las Conversiones con Reaumur
        elif conversion == "rec" :
            rec = cantidad  * 1.25
            print("..............................................")
            print(f"El Resultado de la Conversion es : {rec} °C")
            print("..............................................")
            break
        elif conversion ==  "ref" : 
            ref = cantidad  * 2.25 + 32
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ref} °F")
            print("..............................................")
            break
        elif conversion == "rek" :
            rek = cantidad * 1.25 + 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {rek} K")
            print("..............................................")
            break
        elif conversion == "rer" :
            rer = (cantidad  * 9 / 4) + 491.67
            print("..............................................")
            print(f"El Resultado de la Conversion es : {rer} °R")
            print("..............................................")
            break
        elif conversion == "red" :
            red = (cantidad  -80) * 15 / 8
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-red} °De")
            print("..............................................")
            break
        elif conversion == "ren" :
            ren = (cantidad * 33 / 80)
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ren} °N")
            print("..............................................")
            break
        #Todas las Conversiones con deslile   
        elif conversion == "dc" :
            dc = (cantidad  - 100) * 2 / 3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-dc} °C")
            print("..............................................")
            break
        elif conversion ==  "df" : 
            df = 212 - (100 - cantidad ) * 6/5
            print("..............................................")
            print(f"El Resultado de la Conversion es : {df} °F")
            print("..............................................")
            break
        elif conversion == "dk" :
            dk =  273.15 - (100 - cantidad)  * 2/3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dk} K")
            print("..............................................")
            break
        elif conversion == "dr" :
            dr = (671.67 - cantidad) * 5 / 6
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dr} °R")
            print("..............................................")
            break
        elif conversion == "dre" :
            dre = (cantidad  - 80) * 8 / 15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {-dre} °Re")
            print("..............................................")
            break
        elif conversion == "dn" :
            dn = (33 - cantidad) * 100 / 50 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dn} °N")
            print("..............................................")
            break
        #Todas las Conversiones con Newton
        elif conversion == "nc" :
            nc = cantidad   * 100 /33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {nc} °C")
            print("..............................................")
            break
        elif conversion ==  "nf" : 
            nf = cantidad   * 180 /33 +32
            print("..............................................")
            print(f"El Resultado de la Conversion es : {nf} °F")
            print("..............................................")
            break
        elif conversion == "nk" :
            nk = cantidad  * 100 / 33 + 273.15
            print("..............................................")
            print(f"El Resultado de la Conversion es : {nk} K")
            print("..............................................")
            break
        elif conversion == "nr" :
            nr = (cantidad * 180 / 33 + 32 + 459.67)
            print("..............................................")
            print(f"El Resultado de la Conversion es : {nr} °R")
            print("..............................................")
            break
        elif conversion == "nre" :
            nre = cantidad * 80 / 33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {nre} °Re")
            print("..............................................")
            break
        elif conversion == "nd" :
            nd = cantidad   * 100 / 33
            print("..............................................")
            print(f"El Resultado de la Conversion es : {nd} °De")
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

        
        

