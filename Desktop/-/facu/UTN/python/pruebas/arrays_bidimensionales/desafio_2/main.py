from funciones import *
from funciones_especificas import *
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
def main():

    lista_usuario_1 = ["leche", "pan","queso","yogurt","avena"]
    lista_usuario_2 = ["pan", "carbon","papa","jamon","yogurt"]

    usuario = int(input("Bienvenido, usted es el usuario 1 o el 2?: "))
    print("1️⃣  Productos en común: ¿Qué productos han comprado ambos usuarios?")
    print("2️⃣  Productos exclusivos: ¿Qué productos ha comprado cada usuario que el otro no ha adquirido?")
    print("3️⃣  Catálogo total: ¿Cuál sería el conjunto total de productos comprados entre los dos usuarios?")
    print("4️⃣  Recomendaciones: ¿Cómo podrías utilizar esta información para sugerir productos a cada usuario?")
    
    continuar = "S"
    while continuar == "S":

        opcion = int(input("➡  Seleccione una opcion[1-4]: "))

        match opcion:

            case 1:
                print("Los productos que ambos han comprado en comun son:",encontrar_prod_en_comun(lista_usuario_1, lista_usuario_2))
            case 2:
                print("Los productos que uno ha comprado y el otro no son:", encontrar_prod_exclusivo(lista_usuario_1, lista_usuario_2))
            case 3:
                print("Todos los productos que han comprado son:",mostrar_total(lista_usuario_1, lista_usuario_2))
            case 4:
                if usuario == 1:
                    print("Hemos visto que otros usuarios llevaron",recomendar_usuario_1(lista_usuario_1, lista_usuario_2),"y tu no, te lo recomendamos!")
                else:
                    print("Hemos visto que otros usuarios llevaron",recomendar_usuario_2(lista_usuario_1, lista_usuario_2),"y tu no, te lo recomendamos!")

        continuar = input("Desea continuar? S/N:")
main()