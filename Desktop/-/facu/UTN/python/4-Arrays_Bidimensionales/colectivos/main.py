from paquete.funciones import * 
matriz = []
matriz = inicializar_matriz(matriz)
coches = ["0","1","2","3","4"]
lineas = ["518","8","51"]
legajos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print("[**********B I E N V E N I D O**********]")
opcion = 0
while opcion != 6:

    print("1️⃣ Cargar planilla de recaudación")
    print("2️⃣ Mostrar la recaudación de cada coche y línea")              
    print("3️⃣ Calcular y mostrar la recaudación por línea") 
    print("4️⃣ Calcular y mostrar la recaudación por coche")
    print("5️⃣ Calcular y mostrar la recaudación total")
    print("6️⃣ Salir del programa")


    opcion = int(input("Elija una opcion[1-2-3-4-5-6]: "))
    while validar_opcion(opcion) == False:
        opcion = int(input("Por favor elija una opcion valida[1-2-3-4-5-6]: "))
    

    match opcion:
        
        case 1:
            su_legajo =  int(input("Ingrese su numero de legajo: "))
            while validar_legajo(su_legajo, legajos) == False:
                su_legajo = int(input("Error ingrese un legajo valido![1-15]: "))
            matriz = ingresar_datos(matriz,coches,lineas)

        case 2:    
            printear_matriz_completa(matriz,coches,lineas)

        case 3:     
            recaudacion_lineas = calcular_recaudacion_lineas(matriz, lineas)

        case 4:     
            recaudacion_coches = calcular_recaudacion_coches(matriz, coches)

        case 5: 
            sumar_total(recaudacion_coches)

        case 6:
            print("Finalizando programa...")
            break