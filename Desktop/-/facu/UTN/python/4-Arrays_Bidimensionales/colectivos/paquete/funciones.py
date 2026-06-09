def validar_legajo(su_legajo:int, legajos:list)->bool:

    for i in range (len(legajos)):
        for j in range (len(legajos)):    

            if legajos[j] == su_legajo:
                
                return True
        else:
            return False

def printear_matriz(matriz:list):    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"[",matriz[i][j],"]", end=" ")
        print("")

def inicializar_matriz (matriz:list)->list:
    for i in range(5):
        fila = [0] * 3
        matriz += [fila]
    return matriz

def printear_matriz_completa(matriz:list,coches:list,lineas:list)->None:

    for i in range(len(matriz)+1):
        for j in range(len(matriz[0])+1):

            if j == 0 and i == 0:
                print("     ", end=" ")
            elif i == 0 and j > 0:
                print("[",lineas[j - 1],"]", end=" ")
            elif i > 0:
                if j == 0:
                    print("[",coches[i-1],"]", end=" ")
                else:
                    print("[",matriz[i-1][j-1],"]", end=" ")
        print("")

def ingresar_datos(matriz:list, coches:list, lineas:list)->list:

    continuar = "s"
    while continuar == "s":

        linea = int(input("Que linea quiere cargar?[0-1-2]:"))
        while linea < 0 or linea > 2:
            linea = int(input("Error, ingrese una linea valida...[0-1-2]:"))

        coche = int(input("Que coche quiere cargar?[0-1-2-3-4]:"))   
        while coche < 0 or coche > 4:
            coche = int(input("Error, ingrese una linea valida...[0-1-2-3-4]:"))

        precio = int(input(f"[linea:{lineas[linea]}]Ingrese lo recaudado del vehiculo {coches[coche]}:"))
                
        matriz[coche][linea] += precio

        continuar = input("Desea cargar de nuevo? s/n:")
    
    return matriz
    
def calcular_recaudacion_coches(matriz:list, coches:list)->list:
    valor_filas = [0] * len(coches)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
    
            valor_filas[i] += matriz[i][j]
        
        #print(f"Recaudacion de coche[{i}]: {valor_filas[i]}")
    coche = int(input("la recaudacion de que choche quiere ver?:"))
    while coche < 0 or coche > 4:
        coche = int(input("Error, ingrese una linea valida...[0-1-2-3-4]:"))
    print(f"Recaudacion de coche[{coche}]: {valor_filas[coche]}")
    return valor_filas

def calcular_recaudacion_lineas(matriz:list, lineas:list)->list:
    valor_columnas = [0] * len(lineas)

    for i in range(len(lineas)):
        for j in range(len(matriz)):
    
            valor_columnas[i] += matriz[j][i]

        print(f"Recaudacion de linea[{i}]: {valor_columnas[i]}")
    return valor_columnas

def sumar_total(coches)->int:
    acumulador = 0

    for i in range(len(coches)):

        acumulador += coches[i] 
    
    print(f"El total recaudado es:",acumulador)


def validar_opcion(opcion)->bool:
    if opcion < 1 or opcion > 6:
        return False
    else:
        True