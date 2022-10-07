#Los operadores logicos estan basados en la logica proposicional
# se trata de comparar valores de a pares 
#siempre retornan un valor booleano o logico (True or False)
# y los operandos tambien deben ser del tipo booleno

ver = True
falso = False

#AND --> conjuncion logica es como un "y". Debe cumplirse esto Y tambien esto
#Solo retorna True si ambas partes son True
print("True and True: ", ver and ver)
print("True and False: ", ver and falso)
print("False and True: ", falso and ver)
print("False and False: ", falso and falso, "\n")

#OR --> disyuncion logica, es como un "o". Debe cumplirse esto o debe cumplirse lo otro
#Para que sea verdadero, alguna de las partes debe ser True
#Solo retorna False si ambas partes son False
print("True or True: ", ver or ver)
print("True or False: ", ver or falso)
print("False or True: ", falso or ver)
print("False or False: ", falso or falso, "\n")

#NOT --> negacion. Invierte el valor logico
#Si era True, retorna False. Si era False, retorna True
print("not verdadero: ", not ver)
print("not falso: ", not falso)