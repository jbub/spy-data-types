# lets define some objects
a = 2
b = "my string"


# returns type of object
type(a) # >>> <class 'int'>
type(b) # >>> <class 'str'>


# returns identity of object (address in CPython)
id(a) # >>> 4412808440


# returns whether object is an instance of class
isinstance(a, int) # >>> True
isinstance(a, str) # >>> False
isinstance(b, str) # >>> True


# to check if one class is subclass of another you can use issubclass
# for example booleans are based on integers
issubclass(bool, int) # >>> True


# "is" operator is used to compare identity of objects (function id() is used)
a is a # >>> True
a is b # >>> False


# c now points to the a object, id() returns the same address
c = a
a is c # >>> True
