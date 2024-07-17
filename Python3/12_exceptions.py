### exceptions ###

numberOne, numberTwo = 5, "1"

#try except

try:
    print (numberOne + numberTwo)
    print("No se ha cumplido un error")
except:
    print("se ha producido un error")

#try except else
else: #solo se ejecuta si no hay errores
    print("La ejecución continúa correctamente")
finally: #continúa con el código siempre no importa si hay excepciones o no, es opcional
    print("la ejecución continúa")


#print (numberOne + numberTwo)

#excepciones por tipo
try:
    print (numberOne + numberTwo)
    print("No se ha cumplido un error")
except TypeError as e:
    print(e)
except ValueError:
    print("se ha producido un error de valores")
except Exception as e:
    print(e)


