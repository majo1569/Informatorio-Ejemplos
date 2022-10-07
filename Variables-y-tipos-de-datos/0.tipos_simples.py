#tipos de datos simples:

#Los tipos numericos se diferencian en
#INT
#enteros --> numeros sin coma --> class <int>
un_entero = 55
print(un_entero, "es del tipo de dato: ", type(un_entero)) #la funcion type nos devuelve el tipo de dato del valor de la variable

#FLOAT
#reales --> numeros con coma --> class <float>
un_real = 3.4 #en python la coma de los numeros es con punto . 
print(un_real, "es del tipo de dato: ", type(un_real))

#BOOLEANOS
'''Un tipo muy importante es el booleano o logico
solo puede tomar los valores True (Verdadero) o False(Falso) '''
un_bool = True
print(un_bool, "es del tipo de dato: ", type(un_bool))
#para cambiar el valor de una variable bastaba con asignarle uno nuevo
un_bool = False
print(un_bool, "es del tipo de dato: ", type(un_bool))

#CHAR
'''char --> se refiere a caracteres , osea una cadena de caracteres de longitud 1
en realidad python no lo trata como un tipo atomico, sino que lo entiende como un string de longitud 1
por ende entraria en las secuencias'''

#si indicamos un caracter va entre comillas
caracter = "a"
print(caracter, "es del tipo de dato: ", type(caracter))
