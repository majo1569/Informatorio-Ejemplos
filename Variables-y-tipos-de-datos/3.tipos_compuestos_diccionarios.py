#Los diccionarios tambien son colecciones, pero no se ordenan por su posicion (indices!)
#Cada elemento de un diccionario tiene dos partes (clave - valor)

#DICT
''' Para definir un diciconario lo hacemos entre llaves { } separado por comas ,
pero cada elemento tiene dos partes, y las separamos con  dos puntos  clave : valor
Luego en vez de ubicar los valores con indices, lo hacemos con sus claves'''

un_diccionario = {"red" : "rojo", "blue": "azul", "green": "verde"}
print(un_diccionario, "es del tipo: ", type(un_diccionario))


#la otra manera de definirlos es usar la funcion dict()
'''aca ponemos entre parentesis todos los pares clave valor separados por comas
y encerramos en corchetes el diccionario'''
un_diccionario = dict([("red", "rojo"),  ("blue","azul"), ("green","verde")])
print(un_diccionario, "es del tipo: ", type(un_diccionario))
#vemos que el resultado es el mismo!
