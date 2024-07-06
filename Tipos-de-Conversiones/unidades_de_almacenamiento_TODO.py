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
        print("Bytes (B) , kilobytes (KB) , Megabytes (MG) , Gigabytes (GB) , Terabytes (TB) ")
        conversion=input("Ingrese el Diminutivo a Convertir EJM Si Desea Convertir a todas la unidades con Bytes=B : ").lower()
        while len(conversion) == 3 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Bytes   
        if conversion ==  "b" : 
            b = cantidad / 1024
            print("..............................................")
            print(f"El Resultado de la Conversion es : {b} KB")
            print("..............................................") 
            b = cantidad  / 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {b} MB")
            print("..............................................")
            b = cantidad / 1024 **3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {b} GB")
            print("..............................................")
            b = cantidad  / 1024 **4
            print("..............................................")
            print(f"El Resultado de la Conversion es : {b} TB")
            print("..............................................")
            break
        #Todas las Conversiones con kilobytes  
        elif conversion ==  "kb" : 
            kb = cantidad * 1024
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kb} B")
            print("..............................................")
            kb = cantidad  / 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kb} MB")
            print("..............................................")
            kb = cantidad / 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kb} GB")
            print("..............................................")
            kb = cantidad  / 1024 **3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {kb} TB")
            print("..............................................")
            break 
        #Todas las Conversiones con megabytes
        elif conversion ==  "mg" : 
            mg = cantidad * 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mg} B")
            print("..............................................")
            mg = cantidad  * 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mg} KB")
            print("..............................................")
            mg = cantidad / 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mg} GB")
            print("..............................................")
            mg = cantidad  / 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mg} TB")
            print("..............................................")
            break
        #Todas las Conversiones con Gigabytes 
        elif conversion ==  "gb" : 
            gb = cantidad * 1024 **3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gb} B")
            print("..............................................")
            gb = cantidad  * 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gb} KB")
            print("..............................................")
            gb = cantidad * 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gb} MG")
            print("..............................................")
            gb = cantidad  / 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {gb} TB")
            print("..............................................")
            break
         #Todas las Conversiones con Terabytes 
        elif conversion ==  "tb" : 
            tb = cantidad * 1024 **4
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tb} B")
            print("..............................................")
            tb = cantidad  * 1024 **3
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tb} KB")
            print("..............................................")
            tb = cantidad * 1024 **2
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tb} MG")
            print("..............................................")
            tb = cantidad  * 1024 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {tb} GB")
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

                
                
