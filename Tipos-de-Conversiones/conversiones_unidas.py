# Unimos los Convertidores
print("..............................................")
print("Hola! BIENVENIDO al Convertidor de Unidades")
while True :
    print("..............................................")
    print("Puedes Elegir Cualquiera de las Siguientes Conversiones : ")
    print("Longuitud (L) , Peso (P) , Temperatura (T) , Tiempo (TP) , Unidades de Almacenamiento (UA) ")
    conversion=input("Ingrese los Diminutivo a Convertir EJM Si Desea Convertir Longuitud = L : ").lower()
    while len(conversion) != 1 :
        print("..............................................")
        print ("Ingresa los Diminutivos Correctos :( ")
        break 
        # Llamamos al Convertidor de Longuitud
    if conversion == "l" :
        print("..............................................")
        print("HOLA :) Para Hacer Conversiones de LONGUITUD Te Tengo 2 OPCIONES AQUI")
        print("( DIGITA 1 ) Puedes hacer Conversiones Individualmente es Decir Si Solo Quieres hacer una conversion de uná en una EJM Pulgadas a Metros(Convertiras tu Cantidad a la elejida nomas) ")
        print("( DIGITA 2 ) Puedes hacer Conversiones Totales es Decir tu  Cantidad Puedes convertirla en todas las Unidades dadas EJM Pulgada(Convertiras tu Cantidad a TODAS LAS DEMAS)  ")
        while True :
            try :
                print("..............................................")
                R = int(input("Que Conversion Elijes Conversion Individual (1) , Conversion Total (2): "))
                if R not in [1,2] :
                    print ("Solo Ingresa  1 o 2 :) ")
                elif R == 1 :
                    import longuitud
                    break
                elif R == 2 :
                    import longuitud_TODO
                    break
                
            except ValueError :
                print("..............................................")
                print ("Ingresa un Numero por Favor :(  ") 
                continue
        # Llamamos al Convertidor de Peso/Masa                  
    elif conversion == "p" :
        print("..............................................")
        print("HOLA :) Para Hacer Conversiones de Peso/Masa Te Tengo 2 OPCIONES AQUI")
        print("( DIGITA 1 ) Puedes hacer Conversiones Individualmente es Decir Si Solo Quieres hacer una conversion de uná en una EJM Kilogramos a Libras(Convertiras tu Cantidad a la elejida nomas) ")
        print("( DIGITA 2 ) Puedes hacer Conversiones Totales es Decir tu  Cantidad Puedes convertirla en todas las Unidades dadas EJM Kilogramos(Convertiras tu Cantidad a TODAS LAS DEMAS)  ")
        while True :
            try :
                print("..............................................")
                R = int(input("Que Conversion Elijes Conversion Individual (1) , Conversion Total (2): "))
                if R not in [1,2] :
                   print ("Solo Ingresa  1 o 2 :) ")
                elif R == 1 :
                    import peso
                    break
                elif R == 2 :
                    import peso_TODO
                    break
            except ValueError :
                print("..............................................")
                print ("Ingresa un Numero por Favor :(  ") 
                continue
        # Llamamos al Convertidor de Temperatura 
    elif conversion == "t" :
        print("..............................................")
        print("HOLA :) Para Hacer Conversiones de Temperatura Te Tengo 2 OPCIONES AQUI")
        print("( DIGITA 1 ) Puedes hacer Conversiones Individualmente es Decir Si Solo Quieres hacer una conversion de uná en una EJM Celsius a Delisle(Convertiras tu Cantidad a la elejida nomas) ")
        print("( DIGITA 2 ) Puedes hacer Conversiones Totales es Decir tu  Cantidad Puedes convertirla en todas las Unidades dadas EJM Celsius(Convertiras tu Cantidad a TODAS LAS DEMAS)  ")
        while True :
            try :
                print("..............................................")
                R = int(input("Que Conversion Elijes Conversion Individual (1) , Conversion Total (2): "))
                if R not in [1,2] :
                   print ("Solo Ingresa  1 o 2 :) ")
                elif R == 1 :
                    import temperatura
                    break
                elif R == 2 :
                    import temperatura_TODO
                    break
            except ValueError :
                print("..............................................")
                print ("Ingresa un Numero por Favor :(  ") 
                continue
        # Llamamos al Convertidor de Tiempo  
    elif conversion == "tp" :
        print("..............................................")
        print("HOLA :) Para Hacer Conversiones de Temperatura Te Tengo 2 OPCIONES AQUI")
        print("( DIGITA 1 ) Puedes hacer Conversiones Individualmente es Decir Si Solo Quieres hacer una conversion de uná en una EJM Hora a Minuto (Convertiras tu Cantidad a la elejida nomas) ")
        print("( DIGITA 2 ) Puedes hacer Conversiones Totales es Decir tu  Cantidad Puedes convertirla en todas las Unidades dadas EJM Semana(Convertiras tu Cantidad a TODAS LAS DEMAS)  ")
        while True :
            try :
                print("..............................................")
                R = int(input("Que Conversion Elijes Conversion Individual (1) , Conversion Total (2): "))
                if R not in [1,2] :
                   print ("Solo Ingresa  1 o 2 :) ")
                elif R == 1 :
                    import tiempo
                    break
                elif R == 2 :
                    import tiempo_TODO
                    break
            except ValueError :
                print("..............................................")
                print ("Ingresa un Numero por Favor :(  ") 
                continue
        # Llamamos al Convertidor de Unidades de Almacenamiento
    elif conversion == "ua" :
        print("..............................................")
        print("HOLA :) Para Hacer Conversiones de Unidades de Almacenamiento Te Tengo 2 OPCIONES AQUI")
        print("( DIGITA 1 ) Puedes hacer Conversiones Individualmente es Decir Si Solo Quieres hacer una conversion de uná en una EJM Bytes a kilobytes (Convertiras tu Cantidad a la elejida nomas) ")
        print("( DIGITA 2 ) Puedes hacer Conversiones Totales es Decir tu  Cantidad Puedes convertirla en todas las Unidades dadas EJM kilobytes (Convertiras tu Cantidad a TODAS LAS DEMAS)  ")
        while True :
            try :
                print("..............................................")
                R = int(input("Que Conversion Elijes Conversion Individual (1) , Conversion Total (2): "))
                if R not in [1,2] :
                   print ("Solo Ingresa  1 o 2 :) ")
                elif R == 1 :
                    import unidades_de_almacenamiento
                    break
                elif R == 2 :
                    import unidades_de_almacenamiento_TODO
                    break
            except ValueError :
                print("..............................................")
                print ("Ingresa un Numero por Favor :(  ") 
                continue
        # Llamamos al Convertidor de Indice de Masa Corporal
    elif conversion == "imc" :
        import imc
        # Llamamos al Convertidor de Descuentos con Porcentaje
    elif conversion == "dp" :
        import descuentos_con_porcentajes
    