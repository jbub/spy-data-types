import math
import numbers


# lets define some numbers
a = 4
b = 3.4
c = a - b
d = 2 + 3j


# check if objects are numbers
isinstance(a, numbers.Number)
isinstance(b, numbers.Number)
isinstance(c, numbers.Number)
isinstance(d, numbers.Number)


# integer division, returns quotient and remainder after division
divmod(a, b)


# returns absolute value of number
abs(a)


# returns number rounded to nearest integer
# one can also pass second parameter
# then it returns floating point number rounded to it
round(a)
round(a, 3)


# returns a to the power of b, equal to "a ** b"
pow(a, b)


# returns hexadecimal representation of number in string format prefixed with "0x"
hex(a)


# returns ordinal representation of character
ord('a')


# returns string representation of character represented by the integer
chr(97)


# return square root of number
math.sqrt(a)


# returns the largest integer less than or equal to a
math.floor(a)


# returns smallest integer greater than or equal to a
math.ceil(a)