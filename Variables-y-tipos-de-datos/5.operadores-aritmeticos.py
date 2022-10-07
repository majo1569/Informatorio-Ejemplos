#Operadores aritmeticos o MATEMATICOS
'''Los operadores nos sirven para transformar datos, en este caso hacer calculos
los podemos usar entre los tipos NUMERICOS y el resultado tambien siempre sera del tipo NUMERICO (entero o real)'''
#SUMA --> +
suma = 5 + 3
print("suma: ", suma)
#RESTA
resta = 10 -2
print("resta", resta)
#MULTIPLICACION *
mult = suma * resta
print("multiplicacion: ", mult)

#podemos poner literales, los numeros como en suma y resta, o expresiones.
#aqui hara la multiplicacion de los valores que contengan las variables suma y resta

#DIVISION // --> resultado es del tipo real <float>
division = 8 /3
print("division: ", division)
#podemos indicarles cuantos decimales devolver con la funcion round(). se pone entre parentesis el numero y luego la cantidad de decimales
print("division: ", round(division,2))

#DIVISION ENTERA // --> trunca la parte decimal si la tiene y devuelve un entero <int>
division_ent = 8// 3
print("division entera: ", division_ent)



#POTENCIA **
pot = 5**2
print("potencia", pot)

#MODULO - RESTO %
#Retorna el resto de dividir los dos numeros, lo usamos mucho!
# 9 dividido 2 da 4 con resto 1
modulo = 9 % 2
print("el resto de dividir 9 y 2 es: ", modulo)

'''al modulo tambien lo podemos usar para obtener cada digito de un numero, o partes de el, usando multiplos de 10'''
numero = 1543
print(numero)
#si quisieramos el ultimo numero, la unidad, al dividirlo entre 10 el resto representa la unidad
print("La unidad es: ", numero % 10)
print( numero % 100, "La decena es: ", (numero%100)//10)
print("La centena es: ", numero % 1000)



