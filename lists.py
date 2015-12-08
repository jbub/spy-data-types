# # lets define a list
my_list = [1, 2, 3]


# you can also use alternative list comprehension based syntax
my_list = [x for x in range(3)]


# lets construct a matrix
rows = 2
cols = 4
matrix = [[(i, j) for j in range(cols)] for i in range(rows)]


# append element to the end of the list
my_list.append(4)


# insert element on given index
my_list.insert(0, 6)


# insert each element of passed list to original list
my_list.extend([1, 2, 3])


# alternatively one can use +
my_list + [1, 2, 3]


# remove item from list on given index and return it
value = my_list.pop(0)


# remove first matched value from list
my_list.remove(4)


# reverses the order of the list
my_list.reverse()


# check if value is in the list
"value" in my_list


# get the index of the first matching value
my_list.index("value")


# get element on first index
my_list[0]


# get element on last index
my_list[len(my_list) - 1]


# you can also use negative indexing to get last element
my_list[-1]


# slice from the given index to the end
my_list[0:]


# slice from the beginning to the given index
my_list[:3]


# slice between the given starting and ending indexes
my_list[1:2]
