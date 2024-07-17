## Higher order functions ##

def sum_one(value):
    return value + 1
def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_one(7,2, sum_one))
print(sum_two_values_and_one(7,2, sum_five))

## closures

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

## built-in higher order functions

#map

numbers = [2,5,10,21,3,30]

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))

#filter

def filter_grater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_grater_than_ten, numbers)))

#reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(sum_two_values.__reduce__(sum_two_values,numbers))