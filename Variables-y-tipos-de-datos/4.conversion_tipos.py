#Tambien podemos convertir el tipo de una variable. 
#Para esto hay que indicar el tipo de dato a convertir y entre parentesis la variable


#Por ejemplo un valor decimal pasarlo a entero
num = 333.14
print("un real: ", num, type(num))
num = int(num)
print("un entero: ", num, type(num))
print(tuple(num))

#O convertir un string a una lista, donde cada caracter pasara a ser un elemento de la lista
un_string = "holis"
print(un_string)
un_string = list(un_string)
print(un_string, type(un_string))

#O una tupla con elementos repetidos, si la convertimos a conjunto (set) los eliminara
tupla_crepetidos = 1,1,1,1,2,2,2,2,3,3,3,3,4,4
print(tupla_crepetidos, type(tupla_crepetidos))
print(set(tupla_crepetidos), type(set(tupla_crepetidos)))

#ahora aca estamos trabajando con tipos compuestos, por lo que no podriamos volver a convertirlo en uno simple
#si descomentan la siguiente linea y la ejecutan deberia dar un TypeError
#print(int(tupla_crepetidos))

#tampoco convertir un dato simple a compuesto, por ejemplo entero a tupla
#si descomentan la siguiente linea y la ejecutan deberia dar un TypeError
#print(tuple(num))

#proba que mas se te ocurre

