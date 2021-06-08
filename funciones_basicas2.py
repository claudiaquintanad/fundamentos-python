
#Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
#Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
def regresiva(a):
    array = []
    for x in range(a, -1, -1):
        array.append(x)
    return array 
print(regresiva(5))

#Imprimir y volver : crea una función que recibirá una lista con dos números. Imprima el primer valor y devuelva el segundo.
#Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def imprimir_volver(b):
    print(b[0])
    return b[1]
print(imprimir_volver([1,2]))

#First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
#Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def first_plus(c):
    return (c[0] + len(c))
print(first_plus([1,2,3,4,5]))


#Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo 
#los valores de la lista original que sean mayores que su segundo valor. 
# Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, 
# haga que la función devuelva False
#Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#Ejemplo: values_greater_than_second ([3]) debería devolver False
def mayor_segundo(d):
    contador = 0
    array = []
    if (len(d) < 2):
        return False
    else:
        for x in range(0, len(d), 1):
            if (d[x] > d[1]):
                contador = contador + 1
                array.append(d[x])
    print(contador)
    return array
print(mayor_segundo([3]))
print(mayor_segundo([5,2,3,2,1,4]))

#Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
# La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
#Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def longitud_valor(e):
    lista = []
    for x in range(0, e[0], 1):
        lista.append(e[1])
    return lista
print(longitud_valor([4,7]))