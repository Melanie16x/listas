def contarOrdenarValores(lista):
    conteo = {}
    for i in lista:
        conteo[i] = conteo.get(i, 0) + 1

    ordenarValores = sorted(conteo.items(), key=lambda x: x[1])
    
    return ordenarValores

listaOriginal = [1, 2, 3, 4, 3, 2, 1, 5, 5, 5]
resultado = contarOrdenarValores(listaOriginal)
print("Lista contada y ordenada:", resultado)
