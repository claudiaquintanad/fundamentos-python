# 1. Actualiza los valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
#Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)
#En el directorio sports_directory, cambia 'Messi' a 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#Cambia el valor 20 en z a 30
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

#2. Itera a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)que, dada una lista de diccionarios, 
# la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:
def iterateDictionary(some_list):
    for x in range(0, len(some_list), 1):
        print(some_list[x])
        print(f"first_name - {students[x]['first_name']}, last_name - {students[x]['last_name']}")


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 
# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
"""first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel"""


#3. Obtén valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y 
# un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
"""Michael
John
Mark
KB"""
#Y iterateDictionary2('last_name', students) debería generar:
"""Jordan
Rosales
Guillen
Tonel"""

def iterateDictionary2(key_name, some_list):
    for x in range(0, len(some_list), 1):
        print(some_list[x][key_name])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2 ('first_name', students)
iterateDictionary2('last_name', students)
# 4. Itera a través de un diccionario con valores de listas
#Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas,
# imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
# asociados dentro de la lista de cada clave. Por ejemplo:
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
"""
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""

def printInfo(some_dict):
    for key, val in some_dict.items():
        key_swap = key.swapcase()
        print(f"{len(val)} {key_swap}")
        for element in val:
            print(element)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)