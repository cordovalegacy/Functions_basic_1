#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

5

# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# nothing or undefined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# 5 is what printed, not 5, 10

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# 5 is what printed, not 10, 5 you need to check scope

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# 5 --Good Job Me!

# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# none or no value, and 3 and 5

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# It prints out to 25, not '2''5'

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# b will be 100 and npofoc() will be 10, and return 7 will be undefined in its' scope

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# 7, 14, 21 for 21 they are both called in the final print statement and then added together

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# 8 because b+c, and within a relevant scope


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# 500, 500, 300, 500.... 300 only happens in a local scope AFTER the function is invoked

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# 500, 500, 300, 500, 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# 500, 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# 1, 3, 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# 1, 3, 5, 10