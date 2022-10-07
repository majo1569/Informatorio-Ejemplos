'''Los tipos de datos compuestos combinan datos simples
Las secuencias son tipos de datos compuestos que son colecciones ordenadas (por indices !) de datos simples y compuestos
Dentro de esta clasificacion van las listas,tuplas e incluso strings! (cadena de caracteres)'''

#STRINGS
''' Los strings al final del dia son colecciones de 1 o mas caracteres 
- recorda que un caracter no es solo letras pueden ser numeros, comas, guiones -
para indicar un string debemos poner la cadena entre "" y python lo entendera como string'''
un_string = "cadena de caracteres"
print(un_string, "es del tipo: ", type(un_string))


#LISTAS
'''Son colecciones de datos que pueden ser de distintos tipos y  pueden tener elementos repetidos. 
Se le puede agregar y quitar elementos, y modificar los existentes.
Se las define entre corchetes [ ] y se separan los elementos con coma ,  '''
una_lista = [1,2,"hola", True, "una cadena de caracteres", 3.14]
print(una_lista, "es del tipo: ", type(una_lista))

#TUPLAS
''' Son colecciones de datos que pueden ser de distintos tipos y tener elementos repetidos
Son estructuras inmutables, lo que significa que a diferencia de las listas, una vez definida no se le pueden agregar o quitar elementos
Se las declara con o sin parentesis () separando los elementos con coma ,'''
una_tupla = (1,2,3,"holis", True)
print(una_tupla, "es del tipo: ", type(una_tupla))
una_tupla = 1,2,3,"holis", True
print(una_tupla, "es del tipo: ", type(una_tupla))

#TODOS ESTOS ELEMENTOS SON INDEXADOS
'''Esto significa que los elementos estan ordenados por su posicion por lo que se llaman indices
usando indices podemos acceder a cada elemento, usando corechetes [] que contengan el indice
comienzan en 0, por lo que el primer elemento de una lista,tupla o string se indica con [0]'''

#si quiero el primer elemento de la lista
print("lista: ", una_lista, "\n Primer elemento: ", una_lista[0], "y el elemento es del tipo", type(una_lista[0]))
#cada elemento puede ser tratado como una variable de su tipo de dato 

#si quiero el tercer caracter del string
print("string: ", un_string, "\n Tercer elemento: ", un_string[2])

#Tambien las podemos recorrer de atras para adelante
# de izquierda --> a derecha usamos indices del 0 en adelante
# de derecha <-- a izquierda usamos los indices en negativos desde el -1

#indice -1 significa el ultimo elemento de la estructura
print("lista: ", una_lista, "\n Ultimo elemento: ", una_lista[-1])



