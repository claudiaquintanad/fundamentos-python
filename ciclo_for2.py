
#Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
#Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora [-1, "big", "big", -5]
def biggie_size(a):
    for x in range(0, len(a), 1):
        if a[x] > 0:
            a[x] = "big"
    return a
print(biggie_size([-1,3,5,-5]))

#Contar positivos : dada una lista de números, cree una función para reemplazar el último valor con el número de valores positivos. (Tenga en cuenta que cero no se considera un número positivo).
#Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a [-1,1,1,3] y la devuelve
#Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a [1,6, -4, -2, -7,2] y la devuelve
def count_positives(b):
    contador = 0
    for x in range(0, len(b), 1):
        if b[x] > 0:
            contador = contador + 1
    b[len(b)-1] = contador
    return b
print(count_positives([-1,1,1,1]))

#Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
#Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
#Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def sum_total(c):
    suma = 0
    for x in range(0, len(c), 1):
        suma = suma + c[x]
    return suma 
print(sum_total([1,2,3,4]))

#Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
#Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def promedio_total(d):
    suma = 0
    for x in range(0, len(d), 1):
        suma = suma + d[x]
    promedio = suma/len(d)
    return promedio
print(promedio_total([1,2,3,4]))


#Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
#Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
#Ejemplo: longitud ([]) debería devolver 0
def longitud(e):
    long = 0
    if len(e) == 0:
        return 0
    else:
        for x in range(0, len(e), 1):
            long = long + 1
        return long
print(longitud([37,2,1,-9]))
print(longitud([]))

#respuesta corta, pero sin ciclo for
def longitud(e):
    return len(e)
print(longitud([37,2,1,-9]))
print(longitud([]))

#Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
#Ejemplo: mínimo ([]) debería devolver False
def minimo(f):
    if len(f) == 0:
        return False
    else:
        min = f[0]
        for x in range(0, len(f), 1):
            if min>f[x]:
                min = f[x]
        return min
print(minimo([37,2,1,-9]))
print(minimo([]))

#Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. Si la lista está vacía, haga que la función devuelva False.
#Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
#Ejemplo: máximo ([]) debería devolver False
def maximo(g):
    if len(g) == 0:
        return False
    else:
        max = g[0]
        for x in range(0, len(g), 1):
            if max<g[x]:
                max = g[x]
        return max
print(maximo([37,2,1,-9]))
print(maximo([]))

#Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, promedio, mínimo, máximo y longitud de la lista.
#Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}
def ultimate_analysis(lista):
    minimo = 0
    maximo = 0
    total = 0
    promedio = 0
    longitud = 0
    for x in range(len(lista)):
        longitud = longitud + 1
        if lista[x] < minimo:
            minimo = lista[x]
        
        if lista[x] > maximo:
            maximo = lista [x]

        total += lista[x]

    promedio = (total/len(lista))

    diccionario = { "total": total, "prom": promedio, "min":minimo, "max": maximo, "longitud": longitud }
    return   diccionario  

print(ultimate_analysis([37,2,1, -9]))

#Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def reverse_list(h):
    largo = len(h) - 1
    for x in range(0, int(len(h)/2), 1):
        temp = h[largo]
        h[largo] = h[x]
        h[x] = temp
        largo -= 1 
    return h
print(reverse_list([37,2,1, -9]))



#estudiar este otro metodo
def rever(lista):
    return lista[::-1] 
mylist = [1, 2, 3, 4,] 
mylist2 = [6, 3, -2]   
print(rever(mylist))
print(rever(mylist2))