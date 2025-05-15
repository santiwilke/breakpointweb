def recortar_listas (lista: list)->list:

    for i in range (len(lista)):
        if lista[i] == False :
            indice_final = i
            break
    
    lista = lista[:indice_final]

    return  lista
