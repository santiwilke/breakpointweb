# Desafío: Sistema de Recomendación de Productos
# Una tienda online quiere mejorar su sistema de recomendaciones analizando el comportamiento de sus clientes. 
# Para ello, dispone del historial de compras de dos usuarios distintos, almacenado en listas de productos.
# 
# 📌 Objetivo: Escribir un programa en Python que permita analizar estos historiales de compra y responder las siguientes preguntas:
#  1️⃣ Productos en común: ¿Qué productos han comprado ambos usuarios?
#  2️⃣ Productos exclusivos: ¿Qué productos ha comprado cada usuario que el otro no ha adquirido?
#  3️⃣ Catálogo total: ¿Cuál sería el conjunto total de productos comprados entre los dos usuarios?
#  4️⃣ Recomendaciones: ¿Cómo podrías utilizar esta información para sugerir productos a cada usuario?
# 
# 🎯 Requisitos:
#  ✔️ El programa debe recibir como entrada dos listas de productos (pueden ser ingresadas manualmente o predefinidas).
#  ✔️ Debe procesar y mostrar los resultados de forma clara.
#  ✔️ Se valorará el uso de funciones para estructurar el código de manera organizada.
# 🔹 Extras opcionales:
# Permitir que los usuarios ingresen sus listas manualmente.
# Ampliar el programa para comparar más de dos usuarios.
from funciones_especificas import *
lista_usuario_1 = ["leche", "pan","queso","yogurt","avena"]
lista_usuario_2 = ["pan", "carbon","papa","jamon","yogurt"]

def encontrar_prod_en_comun (lista_1:list, lista_2:list)->list:

    lista_aux = [False] * (len(lista_1)+len(lista_2))
    indice_aux = 0

    for i in range(len(lista_1)):

        for j in range(len(lista_1)):
            
            if lista_1[i] == lista_2[j]:

                lista_aux[indice_aux] = lista_1[i]
        
                indice_aux += 1

    lista_final = recortar_listas(lista_aux)

    return lista_final  
def encontrar_prod_exclusivo (lista_1:list, lista_2:list)->list:

    lista_aux = [False] * (len(lista_1)+len(lista_2))
    indice_aux = 0
    indice_final = 0
    
    for i in range(len(lista_1)):

        for j in range(len(lista_1)):
            
            if lista_1[i] == lista_2[j]:
                lista_aux[indice_aux] = ""
                break
            else :
            
                lista_1[i] != lista_2[j]

                lista_aux[indice_aux] = lista_1[i]
        
        indice_aux += 1
        
    indice_final = len(lista_1)

    for i in range(len(lista_2)):

        for j in range(len(lista_2)):
            
            if lista_2[i] == lista_1[j]:
                lista_aux[indice_final] = ""
                
                break

            else:
                lista_aux[indice_final] = lista_2[i]
        indice_final += 1
    
    return lista_aux
def mostrar_total(lista_1:list, lista_2:list)->list:

    lista_aux = [0] * (len(lista_1) + len(lista_2))
    indice_aux = 0

    for i in range(len(lista_1)):

        lista_aux[i] = lista_1[i]
    

    for i in range(len(lista_1), len(lista_aux)):
        
        lista_aux[i] = lista_2[indice_aux]
    
        indice_aux += 1

    return lista_aux
def recomendar_usuario_1(lista_1:list, lista_2:list)->list:

    maximo = len (lista_1)

    lista_retorno = [False] * maximo
    
    indice_retorno = 0
    
    for i in range(maximo):
        
        bandera = False
        
        for j in range(len(lista_2)):
            
            if lista_1[i] == lista_2[j]:
            
                bandera = True

        if bandera == False:
            
            lista_retorno[indice_retorno]= lista_1[i]
            
            indice_retorno += 1

    lista_final = recortar_listas(lista_retorno)

    return lista_final
def recomendar_usuario_2(lista_1:list, lista_2:list)->list:

    maximo = len (lista_2)

    lista_retorno = [False] * maximo
    
    indice_retorno = 0
    
    for i in range(maximo):
        
        bandera = False
        
        for j in range(len(lista_1)):
            
            if lista_2[i] == lista_1[j]:
            
                bandera = True

        if bandera == False:
            
            lista_retorno[indice_retorno]= lista_2[i]
            
            indice_retorno += 1

    lista_final = recortar_listas(lista_retorno)

    return lista_final
