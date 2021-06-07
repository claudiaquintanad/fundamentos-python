#Básico : imprime todos los enteros del 0 al 150.
for x in range(0, 150+1, 1):
    print(x)

#Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
for x in range(5, 1000+1, 5):
    print(x)

#Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".
for x in range(1, 100+1, 1):
    if x % 5 == 0
        x = 'Coding'
    else if x % 10 == 0
        x = 'Coding Dojo'
    print(x)

#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
sum = 0
for x in range(1, 500000, 2):
    sum = sum + x 
print(sum)


#Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
for x in range(2018, 0, -4):
    print(x)

#Contador flexible : establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. 
# Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)
lowNum = 0
highNum = 0
mult = 0
