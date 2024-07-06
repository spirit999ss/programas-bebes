#Convertidor de Longuitud
print("..............................................")
print("..............................................")
print("..............................................")
print("Bienvenido a el Convertidor de Longuitud :) ")
def loguitud ():    
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
        print("Metros=(m) , Centimetros=(c) , Pulgadas=(p) , Pies=(ps) , Yardas=(y) , MIllas=(ml) y Kiometros=(k)")
        conversion=input("Ingrese los Diminutivo a Convertir EJM Si Desea Convertir de Metros a Centimetros = mc : ").lower()
        while len(conversion) == 1 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Metro 
        if conversion ==  "mc" :
            mc=cantidad * 100
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mc} centimetros")
            print("..............................................")
            break
        elif conversion == "mp" :
            mp = cantidad * 39.37
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mp} pulgadas")
            print("..............................................")
            break
        elif conversion == "mps" :
            mps = cantidad * 3.281
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mps} pies aproximadamente")
            print("..............................................")
            break
        elif conversion == "my" :
            my = cantidad * 1.094
            print("..............................................")
            print(f"El Resultado de la Conversion es : {my} yardas aproximadamente")
            print("..............................................")
            break 
        elif conversion == "mml" :  
            mml = cantidad * 1609
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mml} millas aproximadamente")
            print("..............................................")
            break
        elif conversion == "mk" :
            mk = cantidad / 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mk} kilometros")
            print("..............................................")
            break   
        #Todas las Conversiones con Centimetro
        elif conversion == "cm" :
            cm= cantidad / 100
            print("..............................................")
            print(f"El Resultado de la Conversion es : {cm} metros")
            print("..............................................")
            break
        elif conversion == "cp" :
            cp = cantidad / 2.54
            print("..............................................")
            print(f"El Resultado de la Conversion es : {cp} pulgadas")
            print("..............................................")
            break   
        elif conversion == "cps" :
            cps = cantidad / 30.48
            print("..............................................")
            print(f"El Resultado de la Conversion es : {cps} pies")
            print("..............................................")
            break
        elif    conversion == "cy" :
            cy = cantidad / 91.44
            print("..............................................")
            print(f"El Resultado de la Conversion es : {cy} yardas")
            print("..............................................")
            break     
        elif    conversion == "cml" :
            cml = cantidad / 160900
            print("..............................................")
            print(f"El Resultado de la Conversion es : {cml} millas aproximadamente")
            print("..............................................")
            break
        elif    conversion == "ck" :
            ck = cantidad / 100000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ck} kilometros")
            print("..............................................")
            break
            #Todas las Conversiones con Pulgadas
        elif     conversion == "pm" :
            pm= cantidad / 39.37
            print("..............................................")
            print(f"El Resultado de la Conversion es : {pm} metros")
            print("..............................................")
            break
        elif    conversion == "pc" :
            pc = cantidad * 2.54
            print("..............................................")
            print(f"El Resultado de la Conversion es : {pc} centimetros")
            print("..............................................")
            break   
        elif    conversion == "pps" :
            pps = cantidad / 12
            print("..............................................")
            print(f"El Resultado de la Conversion es : {pps} pies")
            print("..............................................")
            break
        elif    conversion == "py" :
            py = cantidad / 36
            print("..............................................")
            print(f"El Resultado de la Conversion es : {py} yardas")
            print("..............................................")
            break     
        elif     conversion == "pml" :
            pml = cantidad / 63360
            print("..............................................")
            print(f"El Resultado de la Conversion es : {pml} millas")
            print("..............................................")
            break
        elif     conversion == "pk" :
            pk = cantidad / 39370
            print("..............................................")
            print(f"El Resultado de la Conversion es : {pk} kilometros aproximadamente")
            print("..............................................")
            break    
            #Todas las Conversiones con Pie
        elif    conversion == "psm" :
            psm= cantidad / 3.281
            print("..............................................")
            print(f"El Resultado de la Conversion es : {psm} metros aproximadamente")
            print("..............................................")
            break
        elif    conversion == "psc" :
            psc = cantidad * 30.48
            print("..............................................")
            print(f"El Resultado de la Conversion es : {psc} centimetros")
            print("..............................................")
            break   
        elif     conversion == "psp" :
            psp = cantidad * 12
            print("..............................................")
            print(f"El Resultado de la Conversion es : {psp} pulgadas")
            print("..............................................")
            break
        elif    conversion == "psy" :
            psy = cantidad / 3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {psy} yardas")
            print("..............................................")
            break     
        elif    conversion == "psml" :
            psml = cantidad / 5280
            print("..............................................")
            print(f"El Resultado de la Conversion es : {psml} millas")
            print("..............................................")
            break
        elif    conversion == "psk" :
            psk = cantidad / 3281
            print("..............................................")
            print(f"El Resultado de la Conversion es : {psk} Kilometros aproximadamente")
            print("..............................................")
            break
            #Todas las Conversiones con Yarda
        elif    conversion == "ym" :
            ym= cantidad / 1.094
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ym} metros aproximadamente")
            print("..............................................")
            break
        elif    conversion == "yc" :
            yc = cantidad * 91.44
            print("..............................................")
            print(f"El Resultado de la Conversion es : {yc} Centimetros")
            print("..............................................")
            break   
        elif    conversion == "yp" :
            yp = cantidad * 36
            print("..............................................")
            print(f"El Resultado de la Conversion es : {yp} Pulgadas")
            print("..............................................")
            break
        elif    conversion == "yps" :
            yps = cantidad * 3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {yps} Pies")
            print("..............................................")
            break     
        elif    conversion == "yml" :
            yml = cantidad / 1760
            print("..............................................")
            print(f"El Resultado de la Conversion es : {yml} Millas")
            print("..............................................")
            break
        elif    conversion == "yk" :
            yk = cantidad / 1094
            print("..............................................")
            print(f"El Resultado de la Conversion es : {yk} kilometros aproximadamente")
            print("..............................................")
            break    
            #Todas las Conversiones con Milla
        elif    conversion == "mlm" :
            mlm= cantidad * 1609
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mlm} metros aproximadamente")
            print("..............................................")
            break
        elif    conversion == "mlc" :
            mlc = cantidad * 160900
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mlc} Centimetros aproximadamente")
            print("..............................................")
            break   
        elif    conversion == "mlp" :
            mlp = cantidad * 63360
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mlp} Pulgada")
            print("..............................................")
            break
        elif    conversion == "mlps" :
            mlps = cantidad * 5280
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mlps} Pies")
            print("..............................................")
            break     
        elif    conversion == "mly" :
            mly = cantidad * 1760
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mly} Yardas")
            print("..............................................")
            break
        elif    conversion == "mlk" :
            mlk = cantidad * 1.609
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mlk} Kilometros aproximadante ")
            print("..............................................")
            break
                #Todas las Conversiones con Kilometro
        elif    conversion == "km" :
            km= cantidad * 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {km} metros")
            print("..............................................")
            break
        elif    conversion == "kc" :
            kc = cantidad * 100000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kc} Centimetros aproximadamente")
            print("..............................................")
            break   
        elif    conversion == "kp" :
            kp = cantidad * 39370
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kp} Pulgadas aproximadamente")
            print("..............................................")
            break
        elif    conversion == "kps" :
            kps = cantidad * 3281
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kps} Pies aproximadante")
            print("..............................................")
            break     
        elif    conversion == "ky" :
            ky = cantidad * 1094
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ky} Yardas aproximadamente")
            print("..............................................")
            break
        elif    conversion == "kml" :
            kml = cantidad / 1.609
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kml} Millas aproximadamente")
            print("..............................................")
            break    
            
      
            
loguitud ()

#Se Pregunta al Usuario SI Quiere Seguir con el convertidos
resultado =input("Presione ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    loguitud ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS")
    break

                
                
