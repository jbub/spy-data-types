# returns length of sequence
len(a)


# returns maximum of sequence
max(a)


# returns minimum of sequence
min(a)


# returns sum of sequence
sum(a)


# returns reversed sequence
reversed(a)


# returns enumerate object, you can iterate over it
# it will produce tuples (index, value,) for each item in sequence
enumerate(a)


# checks that all objects in sequence evaluate to True
all(a)


# checks that at least one object in sequence evaluates to True
any(a)


# returns iterator that aggregates objects from "a" and "b"
zip(a, b)


# sorts sequence and returns its sorted copy
sorted(a)


# applies filter function to every item in sequence
# eleminating items that fn(item) is True, returns iterator
filter(fn, a)


# applies map function to every item in sequence, returns iterator
map(fn, a)


# returns iterator starting at "start", ending at "stop", using the "step" as the interval
range(start, stop, step)


# returns iterator object for a
iter(a)


# returns next item from the iterator
next(a)


import random


# pick one random item from sequence
random.choice([1, 4, 7, 9])


# pick two random items from sequence
random.sample([1, 2, 3, 4], 2)


# shuffle the sequence
t = [1, 2, 3]
random.shuffle(t)


# generate random password from sequence of characters (string)
''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 6))


# conversion between sequences
my_tuple = (2, 3, 4,)
my_list = list(my_tuple)
my_new_tuple = tuple(my_list)


# get unique characters from string
my_string = "hello there"
my_set = set(my_string)


# construct dict from two lists
my_list_of_keys = ['name', 'surname', 'age']
my_list_of_values = ['John', 'Doe', 38]
my_dict = dict(zip(my_list_of_keys, my_list_of_values))
