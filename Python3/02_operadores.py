#operadores

print(3 + 6)
print(3 - 6)
print(3 * 6)
print(3 / 6)

print(3 % 6) #divide y deja el resto o más bien lo imprime
print(3 // 6) #se divide y da un nùmero entero
print(2 ** 3) #exponencial al cubo o a lo que se le ponga
print("hola" + "python") #concatena de otra manera
print("hola " * 5) #multiplica por 5 la palabra hola pero no puede por 2.5

my_intv = 2.5 * 2
print(type(my_intv)) #da el tipo float en el console
print(int(my_intv)) #cambiar a integer y lo imprime
print("hola " * int(my_intv))

#operadores 

print(3 > 4) #mayor
print(3 < 4) #menor
print(3 <= 4) #mayor o igual
print(3 >= 4) #menor o igual
print(3 == 4) #identico
print(3 != 4) #diferente

print ("aaa" == "bbb") #compara cadenas de texto por orden alfabético mayor
print ("aaa" >= "bbb")
print ("aaa" <= "bbb")
print ("aaa" <= "bbb")

#operadores lógicos
print("-------------")
print ( 3 > 4 and "Hola" > "Python")
print ( 3 > 4 or "Hola" > "Python")
print ( 3 < 4 and "Hola" < "Python")
print ( 3 < 4 or "Hola" > "Python")
print ( 3 < 4 or "Hola" > "Python" and 4 == 4)
print (not( 3 > 4 ))
