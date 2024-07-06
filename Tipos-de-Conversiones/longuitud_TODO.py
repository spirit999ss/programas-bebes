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
        conversion=input("Ingrese el Diminutivo a Convertir EJM Si Desea Convertir a todas la unidades con  Metros = M : ").lower()
        while len(conversion) == 3 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Metro 
        if conversion ==  "m" :
            m=cantidad * 100
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} centimetros")
            print("..............................................")
            m = cantidad * 39.37
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} pulgadas")
            print("..............................................")
            m = cantidad * 3.281
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} pies aproximadamente")
            print("..............................................")
            m = cantidad * 1.094
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} yardas aproximadamente")
            print("..............................................")
            m = cantidad * 1609
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} millas aproximadamente")
            print("..............................................")
            m = cantidad / 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {m} kilometros")
            print("..............................................")
            break   
        #Todas las Conversiones con Centimetro
        elif conversion == "c" :
            c= cantidad / 100
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} metros")
            print("..............................................")
            c = cantidad / 2.54
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} pulgadas")
            print("..............................................")
            c = cantidad / 30.48
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} pies")
            print("..............................................")
            c = cantidad / 91.44
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} yardas")
            print("..............................................")
            c = cantidad / 160900
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} millas aproximadamente")
            print("..............................................")
            c = cantidad / 100000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {c} kilometros")
            print("..............................................")
            break
            #Todas las Conversiones con Pulgadas
        elif     conversion == "p" :
            p= cantidad / 39.37
            print("..............................................")
            print(f"El Resultado de la Conversion es : {p} metros")
            print("..............................................")
            p = cantidad * 2.54
            print("..............................................")
            print(f"El Resultado de la Conversion es : {p} centimetros")
            print("..............................................")
            p = cantidad / 12
            print("..............................................")
            print(f"El Resultado de la Conversion es : {p} pies")
            print("..............................................")
            p = cantidad / 36
            print("..............................................")
            print(f"El Resultado de la Conversion es : {p} yardas")
            print("..............................................")
            p = cantidad / 63360
            print("..............................................")
            print(f"El Resultado de la Conversion es : {p} millas")
            print("..............................................")
            p = cantidad / 39370
            print("..............................................")
            print(f"El Resultado de la Conversion es : {p} kilometros aproximadamente")
            print("..............................................")
            break    
            #Todas las Conversiones con Pie
        elif    conversion == "ps" :
            ps = cantidad / 3.281
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ps} metros aproximadamente")
            print("..............................................")
            ps = cantidad * 30.48
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ps} centimetros")
            print("..............................................")
            ps = cantidad * 12
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ps} pulgadas")
            print("..............................................")
            ps = cantidad / 3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ps} yardas")
            print("..............................................")
            ps = cantidad / 5280
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ps} millas")
            print("..............................................")
            ps = cantidad / 3281
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ps} Kilometros aproximadamente")
            print("..............................................")
            break
            #Todas las Conversiones con Yarda
        elif    conversion == "y" :
            y = cantidad / 1.094
            print("..............................................")
            print(f"El Resultado de la Conversion es : {y} metros aproximadamente")
            print("..............................................")
            y = cantidad * 91.44
            print("..............................................")
            print(f"El Resultado de la Conversion es : {y} Centimetros")
            print("..............................................")
            y = cantidad * 36
            print("..............................................")
            print(f"El Resultado de la Conversion es : {y} Pulgadas")
            print("..............................................")
            y = cantidad * 3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {y} Pies")
            print("..............................................")
            y = cantidad / 1760
            print("..............................................")
            print(f"El Resultado de la Conversion es : {y} Millas")
            print("..............................................")
            y = cantidad / 1094
            print("..............................................")
            print(f"El Resultado de la Conversion es : {y} kilometros aproximadamente")
            print("..............................................")
            break    
            #Todas las Conversiones con Milla
        elif    conversion == "ml" :
            ml = cantidad * 1609
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ml} metros aproximadamente")
            print("..............................................")
            ml = cantidad * 160900
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ml} Centimetros aproximadamente")
            print("..............................................")
            ml = cantidad * 63360
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ml} Pulgada")
            print("..............................................")
            ml = cantidad * 5280
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ml} Pies")
            print("..............................................")
            ml = cantidad * 1760
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ml} Yardas")
            print("..............................................")
            ml = cantidad * 1.609
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ml} Kilometros aproximadante ")
            print("..............................................")
            break
                #Todas las Conversiones con Kilometro
        elif    conversion == "k" :
            k = cantidad * 1000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} metros")
            print("..............................................")
            k = cantidad * 100000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} Centimetros aproximadamente")
            print("..............................................")
            k = cantidad * 39370
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} Pulgadas aproximadamente")
            print("..............................................")
            k = cantidad * 3281
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} Pies aproximadante")
            print("..............................................")
            k = cantidad * 1094
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} Yardas aproximadamente")
            print("..............................................")
            k = cantidad / 1.609
            print("..............................................")
            print(f"El Resultado de la Conversion es : {k} Millas aproximadamente")
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

                
                
