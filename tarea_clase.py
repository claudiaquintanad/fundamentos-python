#Crea una función que tome una lista y devuelva un diccionario con su mínimo, máximo, promedio y suma.
def function(lista):
    minimo = 0
    maximo = 0
    suma = 0
    promedio = 0
    for x in range(len(lista)):
        if lista[x] < minimo:
            minimo = lista[x]
        
        if lista[x] > maximo:
            maximo = lista [x]

        suma += lista[x]

    promedio = round(suma/len(lista))

    diccionario = { "min":minimo, "max": maximo, "prom": promedio, "suma": suma}
    return   diccionario  

print(function([1,2,3,4,5]))

#Crea una función que tome una lista y devuelva el primer y el último valor de la lista. Si la longitud de la lista es menor que 2, haga que devuelva False.   
def function(lista=[]):
    if len(lista) < 2:
        return False,     
    else:         
        primer = lista[0]         
        ultimo = lista[-1]                
        return primer, ultimo      

lista_1 = [1, 2, 3, 4] 
lista_2 = [2] 
primer, ultimo = function(lista_1) 
print(f"el primero es {primer} y el ultimo es {ultimo}")




#Crea una función que dado una palabra diga si es palindroma o no

#forma1
miCadenaDeTexto = "ojo"
# Imprime en ese caso "Es palindroma"
if str(miCadenaDeTexto) == str(miCadenaDeTexto)[::-1]:
    print("Es palindroma")
else:
    print("No es palindroma")

#forma2
def text(texto):
    x = ""
    for char in texto:
        x = char + x

    if texto == x:
        return "Es palindroma"
    else:
        return "No es palindroma"
    
print(text("oso"))