# lets define a dictionary
my_dict = {
    'my-key': 2,
    'my-second-key': [1, 2, 3],
}


# alternative way using built-in class
my_dict = dict(a=1, b=2, c=3)


# another way using dict comprehensions
my_dict = {key: value for key, value in sequence}


# access value of key
my_dict['my-key']


# set value of key
my_dict['my-key'] = 8


# remove key
del my_dict['my-key']


# access value of key, return default if key is not present
my_dict.get('my-key', 4)


# check if key is present
'my-key' in my_dict


# check if key is not present
'my-key' not in my_dict


# list all items as key, value pairs (tuples)
my_dict.items()


# list all values
my_dict.values()


# list all keys
my_dict.keys()


# iterating over dictionary iterates over its keys
for key in my_dict:
    print key


# update dictionary using other dictionary
my_dict.update({'my-third-key': 7})


# count all items in dictionary
len(my_dict)


# remove and return key, value pair
key, value = my_dict.popitem()


# set default value for key, if key already present return its value
my_dict.setdefault('my-key', 34)
