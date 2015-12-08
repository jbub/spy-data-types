# lets define some lists and sets
a = [1, 2, 3]
b = [4, 1, 1, 3, 5]


# sets can be defined using set literals
my_set = {1, 2, 3}


# sets can be also defined using set comprehensions
my_set = {x for x in sequence}


# notice that there are only unique items in the sets
sa = set(a)
sa # >>> set([1, 2, 3])
sb = set(b)
sb # >>> set([1, 3, 4, 5])


# check if value exists in set
2 in sb


# is every element in the "sa" in "sb"
sa.issubset(sb) # >>> False


# is every element in "sb" in the "sa"
sa.issuperset(sb) # >>> False


# return True if there are no common elements in "sa" and "sb"
sa.isdisjoint(sb) # >>> False


# intersection, return a new set with elements common to the set and all others
sa & sb # >>> set([1, 3])


# union, return a new set with elements from the set and all others
sa | sb # >>> set([1, 2, 3, 4, 5])


# symmetric_differencem, return a new set with elements in either the set or other but not both
sa ^ sb # >>> set([2, 4, 5])


# difference, return a new set with elements in the set that are not in the others
sa - sb # >>> set([2])


# add and remove items from set
my_set.add(2)
my_set.remove(3)


# clean the whole set
my_set.clear()


# frozent set is like set, but once you initialize it you cant change it (immutable)
my_frozen_set = frozenset(my_set)
