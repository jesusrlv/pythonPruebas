### Functions ###

def my_function ():
    print("Hola mundo desde una función")

my_function()
my_function()
my_function()

def sum_two_values ():
    num1 = 5
    num2 = 10
    return num1 + num2

print(sum_two_values())

def sum_and_multiply_two_values (num1, num2):
    result = num1 + num2
    return result * 2

print(sum_and_multiply_two_values(5, 10))

def print_name(name,surname):
    print(f"Mi nombre es {name} y me dicen {surname}")

print_name(surname="rodolfo", name="jesusrlv")

def print_name_with_default(name,surname,alias="sin alias"):
    print(f"Mi nombre es {name} y me dicen {surname} y {alias}")

print_name_with_default("rodolfo","leaños")
print_name_with_default("rodolfo","leaños","rojo")

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("hola","python","jesusrlv")
print_texts("python","jesusrlv")

