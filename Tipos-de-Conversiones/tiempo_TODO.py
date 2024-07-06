#Convertidor de Tiempo
print("..............................................")
print("..............................................")
print("..............................................")
print("Bienvenido a el Convertidor de Tiempo :) ")
def Tiempo   ():    
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
        print("Segundos=(Sg) , Minutos=(Mn) , Horas=(H) , Dias=(D) , Semanas=(Sm) , Mes(Ms) Años=(Añ) , Decadas=(Dc) y Siglos =(Sgl)")
        conversion=input("Ingrese los Diminutivo a Convertir EJM Si Desea Convertir de Segundos a Minutos = SM : ").lower()
        while len(conversion) == 3 :
            print("..............................................")
            print ("Ingresa los Diminutivos Correctos :( ")
            break 
            #Todas las Conversiones con Segundos 
        if conversion ==  "sg" : 
            sg=cantidad /  60 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sg} minutos")
            print("..............................................")
            sg = cantidad / 3600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sg} horas")
            print("..............................................")
            sg = cantidad / 86400
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sg} dias")
            print("..............................................")
            sg = cantidad /604800
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sg} semanas")
            print("..............................................")  
            sg = cantidad / 2628000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sg} meses aproximadamente")
            print("..............................................")
            sg = cantidad / 315360000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sg} años aproximadamente")
            print("..............................................")
            sg = cantidad / 3155760000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sg} decadas aproximadamente")
            print("..............................................")
            sg = cantidad / 31557600000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sg} siglos aproximadamente")
            print("..............................................")
            break   
        #Todas las Conversiones con Minutos
        elif conversion == "mn" :
            mn = cantidad * 60
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mn} segundos")
            print("..............................................")
            mn = cantidad / 60
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mn} horas")
            print("..............................................")
            mn = cantidad / 1440
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mn} dias")
            print("..............................................")  
            mn = cantidad / 10080
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mn} semanas")
            print("..............................................")
            mn = cantidad / 43800
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mn} meses aproximadamente")
            print("..............................................")
            mn = cantidad / 525600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mn} años")
            print("..............................................")
            mn = cantidad / 5256000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mn} decadas")
            print("..............................................") 
            mn = cantidad /  52560000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mn} siglos")
            print("..............................................")
            break
        #Todas las Conversiones con Horas
        elif conversion == "h" :
            h = cantidad * 3600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {h} segundos")
            print("..............................................")
            break
        elif conversion == "h" :
            h = cantidad * 60
            print("..............................................")
            print(f"El Resultado de la Conversion es : {h} minutos")
            print("..............................................")
            h = cantidad / 24
            print("..............................................")
            print(f"El Resultado de la Conversion es : {h} dias")
            print("..............................................")  
            h = cantidad / 168
            print("..............................................")
            print(f"El Resultado de la Conversion es : {h} semanas")
            print("..............................................")
            h = cantidad / 730
            print("..............................................")
            print(f"El Resultado de la Conversion es : {h} meses aproximadamente")
            print("..............................................")
            h = cantidad / 8760
            print("..............................................")
            print(f"El Resultado de la Conversion es : {h} años")
            print("..............................................")
            h = cantidad / 87600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {h} decadas")
            print("..............................................")
            h = cantidad / 876000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {h} siglos")
            print("..............................................")
            break   
        #Todas las Conversiones con Dias
        elif conversion == "dsg" :
            dsg =  cantidad * 86400
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dsg} segundos")
            print("..............................................")
            break
        elif conversion == "dmn" :
            dmn = cantidad * 1440
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dmn} minutos")
            print("..............................................")
            break 
        elif conversion == "dh" :
            dh = cantidad * 24
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dh} horas")
            print("..............................................")
            break
        elif conversion == "dsm" :  
            hsm = cantidad / 7
            print("..............................................")
            print(f"El Resultado de la Conversion es : {hsm} semanas")
            print("..............................................")
            break
        elif conversion == "dms" :
            dms = cantidad / 30
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dms} meses aproximadamente ")
            print("..............................................")
            break  
        elif conversion == "da" :
            da = cantidad / 365
            print("..............................................")
            print(f"El Resultado de la Conversion es : {da} años")
            print("..............................................")
            break
        elif conversion == "ddc" :
            ddc = cantidad / 3650
            print("..............................................")
            print(f"El Resultado de la Conversion es : {ddc} decadas")
            print("..............................................")
            break
        elif conversion == "dsgl" :
            dsgl = cantidad / 36500
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dsgl} siglos")
            print("..............................................")
            break
        #Todas las Conversiones con Semana
        elif conversion == "smsg" :
            smsg =  cantidad * 604800
            print("..............................................")
            print(f"El Resultado de la Conversion es : {smsg} segundos")
            print("..............................................")
            break
        elif conversion == "smmn" :
            smmn = cantidad * 10080
            print("..............................................")
            print(f"El Resultado de la Conversion es : {smmn} minutos")
            print("..............................................")
            break 
        elif conversion == "smh" :
            smh = cantidad * 168
            print("..............................................")
            print(f"El Resultado de la Conversion es : {smh} horas")
            print("..............................................")
            break
        elif conversion == "smd" :
            smd = cantidad * 7
            print("..............................................")
            print(f"El Resultado de la Conversion es : {smd} dias")
            print("..............................................")
            break 
        elif conversion == "smms" :
            smms = cantidad / 4.34524
            print("..............................................")
            print(f"El Resultado de la Conversion es : {smms} meses aproximadamente")
            print("..............................................")
            break  
        elif conversion == "smañ" :
            smañ = cantidad / 52.1775 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {smañ} años")
            print("..............................................")
            break
        elif conversion == "smdc" :
            smdc = cantidad / 520
            print("..............................................")
            print(f"El Resultado de la Conversion es : {smdc} decadas aproximadamente")
            print("..............................................")
            break
        elif conversion == "smsgl" :
            smsgl = cantidad / 5200
            print(".......................................... }....")
            print(f"El Resultado de la Conversion es : {smsgl} siglos aproximadamente")
            print("..............................................")
            break   
        #Todas las Conversiones con Mes
        elif conversion == "mssg" :
            mssg =  cantidad * 2592000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mssg} segundos aproximadamente")
            print("..............................................")
            break
        elif conversion == "msmn" :
            msmn = cantidad * 43200
            print("..............................................")
            print(f"El Resultado de la Conversion es : {msmn} minutos aproximadamente")
            print("..............................................")
            break 
        elif conversion == "msh" :
            msh = cantidad * 730 
            print("..............................................")
            print(f"El Resultado de la Conversion es : {msh} horas aproximadamente")
            print("..............................................")
            break
        elif conversion == "msd" :
            msd = cantidad * 30.417
            print("..............................................")
            print(f"El Resultado de la Conversion es : {msd} dias aproximadamente")
            print("..............................................")
            break
        elif conversion == "mssm" :  
            mssm = cantidad * 4.345
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mssm} semanas aproximadamente")
            print("..............................................")
            break 
        elif conversion == "msañ" :
            msañ = cantidad  / 12
            print("..............................................")
            print(f"El Resultado de la Conversion es : {msañ} años ")
            print("..............................................")
            break
        elif conversion == "msdc" :
            msdc = cantidad / 120
            print("..............................................")
            print(f"El Resultado de la Conversion es : {msdc} decadas ")
            print("..............................................")
            break
        elif conversion == "mssgl" :
            mssgl = cantidad / 1200
            print("..............................................")
            print(f"El Resultado de la Conversion es : {mssgl} siglos aproximadamente")
            print("..............................................")
            break 
        #Todas las Conversiones con Años
        elif conversion == "añsg" :
            añsg =  cantidad * 31536000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {añsg} segundos aproximadamente")
            print("..............................................")
            break
        elif conversion == "añmn" :
            añmn = cantidad *  525600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {añmn} minutos")
            print("..............................................")
            break 
        elif conversion == "añh" :
            añh = cantidad * 8760
            print("..............................................")
            print(f"El Resultado de la Conversion es : {añh} horas")
            print("..............................................")
            break
        elif conversion == "añd" :
            msd = cantidad * 365
            print("..............................................")
            print(f"El Resultado de la Conversion es : {msd} dias")
            print("..............................................")
            break
        elif conversion == "añsm" :  
            añsm = cantidad * 52.143
            print("..............................................")
            print(f"El Resultado de la Conversion es : {añsm} semanas")
            print("..............................................")
            break
        elif conversion == "añms" :
            añms = cantidad * 12
            print("..............................................")
            print(f"El Resultado de la Conversion es : {añms} meses")
            print("..............................................")
            break
        elif conversion == "añdc" :
            añdc = cantidad  / 10
            print("..............................................")
            print(f"El Resultado de la Conversion es : {añdc} decadas")
            print("..............................................")
            break
        elif conversion == "añsgl" :
            añsgl = cantidad / 100
            print("..............................................")
            print(f"El Resultado de la Conversion es : {añsgl} siglos")
            print("..............................................")
            break 
        #Todas las Conversiones con Decadas
        elif conversion == "dcsg" :
            dcsg =  cantidad * 315360000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dcsg} segundos aproximadamente")
            print("..............................................")
            break
        elif conversion == "dcmn" :
            dcmn = cantidad * 5256600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dcmn} minutos")
            print("..............................................")
            break 
        elif conversion == "dch" :
            dch = cantidad * 87600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dch} horas")
            print("..............................................")
            break
        elif conversion == "dcd" :
            dcd = cantidad * 3650
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dcd} dias")
            print("..............................................")
            break
        elif conversion == "dcsm" :  
            dcsm = cantidad * 521.4
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dcsm} semanas aproximadamente")
            print("..............................................")
            break
        elif conversion == "dcms" :
            dcms = cantidad * 120
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dcms} meses")
            print("..............................................")
            break
        elif conversion == "dcañ" :
            dcañ = cantidad  * 10
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dcañ} años")
            print("..............................................")
            break
        elif conversion == "dcsgl" :
            dcsgl = cantidad / 10
            print("..............................................")
            print(f"El Resultado de la Conversion es : {dcsgl} siglos")
            print("..............................................")
            break
        #Todas las Conversiones con Siglos
        elif conversion == "sglsg" :
            sglsg =  cantidad * 315360000
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sglsg} segundos aproximadamente")
            print("..............................................")
            break
        elif conversion == "sglmn" :
            sglmn = cantidad * 5256600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sglmn} minutos")
            print("..............................................")
            break 
        elif conversion == "sglh" :
            sglh = cantidad * 87600
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sglh} horas")
            print("..............................................")
            break
        elif conversion == "sgld" :
            sgld = cantidad * 36500

            print("..............................................")
            print(f"El Resultado de la Conversion es : {sgld} dias")
            print("..............................................")
            break
        elif conversion == "sglsm" :
            sglsm = cantidad * 5214
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sglsm} semanas aproximadamente")
            print("..............................................")
            break 
        elif conversion == "sglms" :  
            sglms = cantidad * 1200
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sglms} meses aproximadamente")
            print("..............................................")
            break
        elif conversion == "sglañ" :
            sglañ = cantidad * 100
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sglañ} años")
            print("..............................................")
            break  
        elif conversion == "sgldc" :
            sgldc = cantidad * 10
            print("..............................................")
            print(f"El Resultado de la Conversion es : {sgldc} decadas")
            print("..............................................")
            break
        
      
            
Tiempo ()

#Se Pregunta al Usuario SI Quiere Seguir con el convertidos
resultado =input("Ingrese un Espacio y ENTER para Continuar o Si Quiere Salir Cualquier Caracter : ")             
while resultado == "" :
    Tiempo ()
    continue
while resultado == resultado.lower() :
    print("GRACIAS :) POR ELEGIRNOS") 
    break

                
                
