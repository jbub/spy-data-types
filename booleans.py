# lets define some booleans
my_false_bool = False
my_true_bool = True


# result of expressions is of boolean type
my_computed_bool = 2 > 1


# evaluation of basic boolean expressions
True and False # False
True and True  # True
False and True # False
False or True  # True
False or False # False


# to evaluate complex and nested expressions use parenthesis
(1 > 2) or (2 == 2 and 4 != 3)


# order of evaluation
==
!=
and
or


# returns negation of x
not x


# returns x if x is False, y otherwise
x and y


# returns y if x is False, x otherwise
x or y


# lets define a function that returns boolean
def my_max(a, b):
    if a > b:
        return a
    return b
