import collections

#
# namedtuple
#

Rectangle = collections.namedtuple('Rectangle', ['a', 'b'], verbose=True)

my_rect = Rectangle(a=10, b=20)
my_rect # >>> Rectangle(a=10, b=20)

a, b = my_rect
a, b # >>> (10, 20)

#
# deque
#

d = collections.deque('hello')
d.append('x') # add new item to right side
d.appendleft('y') # add new item to left side
d # >>> deque(['y', 'h', 'e', 'l', 'l', 'o', 'x'])

d.pop() # pop item from right side
d.popleft() # pop item from left side
d # >>> deque(['h', 'e', 'l', 'l', 'o'])

d.extend([4, 5, 6]) # add new item to right side
d.extendleft([1, 2, 3]) # add new item to left side
d # >>> deque([3, 2, 1, 'h', 'e', 'l', 'l', 'o', 4, 5, 6])

#
# Counter
#

counter = collections.Counter('collections')
counter['c'] # >>> 2
counter.most_common(4) # >>> [('l', 2), ('o', 2), ('c', 2), ('s', 1)]
list(counter.elements()) # >>> ['s', 'l', 'l', 'o', 'o', 'c', 'c', 'i', 'n', 'e', 't']

#
# OrderedDict
#

my_dict = collections.OrderedDict()
my_dict['key'] = 2
my_dict['key_two'] = 3
my_dict['key_three'] = 4

my_dict # >>> OrderedDict([('key', 2), ('key_two', 3), ('key_three', 4)])

#
# defaultdict
#

# group a sequence of key-value pairs into a dictionary of sets
data = [
    ('add', 2),
    ('delete', 3),
    ('add', 4),
    ('edit', 10),
    ('edit', 6),
]
things = collections.defaultdict(set)

for action, number in data:
    things[action].add(number)

things # >>> defaultdict(<class 'set'>, {'edit': set([10, 6]), 'add': set([2, 4]), 'delete': set([3])})
