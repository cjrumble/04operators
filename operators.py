print(7 % 4)
#3

# Arithmetic operators
#Example -

a = 7
b = 4

print('Sum : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)
# Output -
# Sum: 11
# Subtraction: 3
# Multiplication: 28
# Division(float): 1.75
# Division(floor): 1
# Modulus: 3
# Exponent: 2401
#
# # Comparison operators
#
# # Example -
#
a = 7
b = 4

print('a > b is', a > b)

print('a < b is', a < b)

print('a == b is', a == b)

print('a != b is', a != b)

print('a >= b is', a >= b)

print('a <= b is', a <= b)
# Output -
#
# a > b is True
# a < b is False
# a == b is False
# a != b is True
# a >= b is True
# a <= b is False
#
#
# # Logical operators
#
# # Example -
#
a = 7
b = 4

# Result: a and b is 4
print('a and b is', a and b)

# Result: a or b is 7
print('a or b is', a or b)

# Result: not a is False
print('not a is', not a)
# Output -
#
# a and b is 4
# a or b is 7
# not a is False
#
#
# # Bitwise operators
#
# # Example -
#
a = 4
b = 6

# Bitwise AND: The result of 'a & b' is 4
print('a & b is', a & b)
# Output -
#
# a & b is 4
# The
# above
# result is the
# outcome
# of
# following
# AND(‘ & ’) operation.
#
# 00000100 &
# 00000110
# ------------------
# 00000100
# # (the binary representation of the number 4)
#
# Assignment operators
#
# Advanced Python operators
#
# Identity operators
#
# # Example -
#
# Using 'is' identity operator
a = 7
if (type(a) is int):
    print("true")
else:
    print("false")

# Using 'is not' identity operator
b = 7.5
if (type(b) is not int):
    print("true")
else:
    print("false")
# # Output -
# true
# true
#
# # Membership operators
# #Example -

# Using Membership operator
str = 'Python operators'
dict = {6: 'June', 12: 'Dec'}

print('P' in str)
print('Python' in str)
print('python' not in str)
print(6 in dict)
print('Dec' in dict)
# # Output -
# True
# True
# True
# True
# False