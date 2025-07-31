# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Imprimir la lista
print("Lista de números:", numeros)

# Acceder a un elemento de la lista por índice
primer_numero = numeros[0]
print("Primer número:", primer_numero)

# Modificar un elemento de la lista
numeros[1] = 10
print("Lista después de modificar:", numeros)

# Añadir elementos a la lista
numeros.append(6)
numeros.append(7)
print("Lista después de añadir elementos:", numeros)

# Obtener la longitud de la lista
longitud = len(numeros)
print("Longitud de la lista:", longitud)

# Eliminar un elemento de la lista
numeros.remove(4)
print("Lista después de eliminar el número 4:", numeros)

# Revertir la lista
numeros.reverse()
print("Lista después de revertir:", numeros)
