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

print_name("rodolfo", "jesusrlv")