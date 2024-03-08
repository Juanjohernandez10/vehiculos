#un parqueadero registra el ingreso y salida de vehiculos, el sistema lleva un conteo de por #ejemplo: 

#motos
#autos 
#bicicletas 
#patinetas 

#cada vez que ingresa un vehiculo el sistema debe sumar a la categoria del vehiculo

#el sistema tambien contempla la salida de vehiculos 
#el istema no ndebe permitir valores negativos en la cantidad  
import os
os.system('cls')
motos = 0
carros = 0
bicis = 0
patinetas = 0
os.system('cls')
controlBln = True
while controlBln == True :

    opciones = input( '\n\.  \n1. motos \n2. carros \n3. bicis  \n4. patinetas \n5. mostrar \n.6 salir \n.opcion es - > ' )
    
    
    if opciones == '1':
        cantidad_motosInt = int(input('ingrese una cantidad de motos -> '))
        movimientoStr =  input('\n1. entrada  \n2. salida \n.opcion -> ')
        if movimientoStr == "1":
            motos += cantidad_motosInt
        if movimientoStr == '2': 
            if  cantidad_motosInt <= motos:
                motos -= cantidad_motosInt
            else:
                print("no hay tantos vehiculos registrados")
    elif opciones == '2':
        cantidad_carrosInt = int(input('ingrese la cantidad  de carros -> ') )
        movimientoStr =  input('\n1. entrada  \n2. salida \n.opcion -> ')
        if movimientoStr == '1':
            carros += cantidad_carrosInt
        if movimientoStr == '2':
            if  cantidad_carrosInt <= carros:
                carros -= cantidad_carrosInt
            else:
                print("No hay tantos carros disponibles")
    elif opciones == '3':
        cantidad_bicicletasInt = int(input('ingrese la cantidad de  bicicletas -> '))
        movimientoStr =  input('\n1. entrada  \n2. salida \n.opcion -> ')
        if movimientoStr == '1':
            bicis += cantidad_bicicletasInt
        if movimientoStr == '2':
            if   cantidad_bicicletasInt <= bicis:
                bicis -= cantidad_bicicletasInt
            else:
                print('No hay tanto en bicicletas') 
    elif opciones == '4':
        cantidad_patinetasInt = int(input('ingrese la cantidad de patinetas -> '))
        movimientoStr =  input('\n1. entrada  \n2. salida \n.opcion -> ')
        if movimientoStr == '1':
            patinetas += cantidad_patinetasInt
        if movimientoStr  == '2':
            if cantidad_patinetasInt <= patinetas:
                patinetas -= cantidad_patinetasInt
            else:
                print('No hay tantas patinetas disponibles')
    elif opciones == '5':
        print ('\nla cantidad total de motos es : ', motos)
        print ('la cantidad total de carros es :', carros)
        print('la cantidad total de bicicletas  es :', bicis)
        print('la cantidad total de patinetas es :', patinetas)
    elif opciones == '6':
        controlBln = False

    
