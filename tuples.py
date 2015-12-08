# lets define some tuples
my_tuple = 2, 3
my_second_tuple = ('Alicia', 'Keys', 34,)


# we can concatenate tuples together to create new ones
my_new_tuple = my_second_tuple + (2, 3, 4,)


# we can access elements using indexes
my_new_tuple[2]


# we can check if value exists in tuple
3 in my_new_tuple


# we can multiply tuples
my_second_tuple * 4


# when function returns more values, it returns a tuple of them
def my_func(a, b):
    return a * 2, b * 3


# tuples can be converted to lists
my_new_list = list(my_second_tuple)
