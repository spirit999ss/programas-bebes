#Convertidor de Unidades de Almacenamiento
print("..............................................")
print("..............................................")
print("..............................................")
print("Bienvenido a el Convertidor de Unidades de Almacenamiento :) ")
def a   ():    
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
        print("Bytes (B) , kilobytes (KB) , Mgabytes (MB) , Gigabytes (GB) , Terabytes (TB) ")
        conversion=input("Ingrese los Diminutivo a Convertir EJM Si Desea Convertir de Bytes a  gigabytes =  BGB: ").lower()
        while len(conversion) == 1 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Bytes   
        if conversion ==  "bkb" : 
            bkb = cantidad / 1024
            print("..............................................")
            print(f"El Resultado de la Conversion es : {bkb} KB")
            print("..............................................")
            break
        elif conversion == "bmb" :
            bmb = cantidad  / 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {bmb} MB")
            print("..............................................")
            break
        elif conversion == "bgb" :
            bgb = cantidad / 1024 **3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {bgb} GB")
            print("..............................................")
            break
        elif conversion == "btb" :
            btb = cantidad  / 1024 **4
            print("..............................................")
            print(f"El Resultado de la Conversion es : {btb} TB")
            print("..............................................")
            break
        #Todas las Conversiones con kilobytes  
        elif conversion ==  "kbb" : 
            kbb = cantidad * 1024
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kbb} B")
            print("..............................................")
            break
        elif conversion == "kbmb" :
            kbmb = cantidad  / 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kbmb} MB")
            print("..............................................")
            break
        elif conversion == "kbgb" :
            kbgb = cantidad / 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kbgb} GB")
            print("..............................................")
            break
        elif conversion == "kbtb" :
            kbtb = cantidad  / 1024 **3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kbtb} TB")
            print("..............................................")
            break 
        #Todas las Conversiones con megabytes
        elif conversion ==  "mgb" : 
            mgb = cantidad * 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mgb} B")
            print("..............................................")
            break
        elif conversion == "mgkb" :
            mgkb = cantidad  * 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mgkb} KB")
            print("..............................................")
            break
        elif conversion == "mggb" :
            mggb = cantidad / 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mggb} GB")
            print("..............................................")
            break
        elif conversion == "mgtb" :
            mgtb = cantidad  / 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mgtb} TB")
            print("..............................................")
            break
        #Todas las Conversiones con Gigabytes 
        elif conversion ==  "gbb" : 
            gbb = cantidad * 1024 **3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gbb} B")
            print("..............................................")
            break
        elif conversion == "gbkb" :
            gbkb = cantidad  * 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gbkb} KB")
            print("..............................................")
            break
        elif conversion == "gbmg" :
            gbmg = cantidad * 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gbmg} MG")
            print("..............................................")
            break
        elif conversion == "gbtb" :
            gbtb = cantidad  / 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gbtb} TB")
            print("..............................................")
            break
         #Todas las Conversiones con Terabytes 
        elif conversion ==  "tbb" : 
            tbb = cantidad * 1024 **4
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tbb} B")
            print("..............................................")
            break
        elif conversion == "tbkb" :
            tbkb = cantidad  * 1024 **3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tbkb} KB")
            print("..............................................")
            break
        elif conversion == "tbmg" :
            tbmg = cantidad * 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tbmg} MG")
            print("..............................................")
            break
        elif conversion == "tbgb" :
            tbgb = cantidad  * 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tbgb} GB")
            print("..............................................")
            break
      
            
a ()

#Se Pregunta al Usuario SI Quiere Seguir con el convertidos
resultado =input("Ingrese un Espacio y ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    a ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS") 
    break

                
                
