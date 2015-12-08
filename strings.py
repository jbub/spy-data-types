# lets define some strings
my_string = "hello there!"


# accesing individual characters by indexes
my_string[1]


# slicing also works for strings
my_string[1:4]


# string concatenation
my_string + ' hello ' + ' world '


# concatenation of other types (explicit conversion is needed)
number = 3
'My number is = '  + str(3)


# old way of string formatting
'My name is %s, and my age is %d' % ('John', 32)


# new way of string formatting
'My name is {0}, and my age is {1:d}'.format('Alicia', 32)
'My name is {name}, and my age is {age:d}'.format(name='Jane', age=22)


# join elements of sequence using string delimiter
', '.join(['my', 'oh', 'my'])


# lowercase all characters
my_string.lower()


# uppercase all characters
my_string.upper()


# is string alphabetic only ?
my_string.isalpha()


# is string digit only ?
my_string.isdigit()


# is string whitespace only ?
my_string.isspace()


# is string starting/ending with prefix, suffix ?
my_string.startswith('hello')
my_string.endswith('world')


# replace occurrences of hello with world
my_string.replace('hello', 'world')


# split string into list by separator
my_string.split(',')


# returns string left filled with "0" digits to make a string of length width
my_string.zfill(3)