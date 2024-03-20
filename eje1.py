def quitar_repetidos(lista):
    return list(set(lista))

listaOriginal = [2, 4, 6, 4, 9, 2]
listaSinRepetidos = quitar_repetidos(listaOriginal)

print("La lista original es: ", listaOriginal)
print("Lista sin los valores repetidos: ", listaSinRepetidos)
