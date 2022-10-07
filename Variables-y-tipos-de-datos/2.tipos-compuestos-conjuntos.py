#Los conjuntos tambien son colecciones pero desordenadas (no podemos usar indices como en listas!)

#SET
''' conjuntos --> class <set>
Colecciones de datos que pueden ser de distintos datos pero NO PUEDE TENER ELEMENTOS REPETIDOS
Si definimos conjuntos con elementos repetidos, los eliminara.
Se le puede agregar y quitar elementos, pero no modificar los existentes
Para definirlos usamos llaves {} y separando los elementos con ,'''
un_conj = {1,1,1,1,2,3,4,"un string"}
print(un_conj, "es :", type(un_conj))


#FROZENSET
'''Son un tipo especial de conjunto que no admite que se agreguen o quiten elementos
para obtener uno, hay que definir un conjunto y luego convertirlo a frozen set
la conversion de datos se llama casting'''

un_frozenset = {1,2,3,4}
#para convertir hacemos frozenset y entre parentesis la variable a convertir
un_frozenset = frozenset(un_frozenset) #guardamos en la misma variable el conjunto convertido
print(un_frozenset, "es :", type(un_frozenset))