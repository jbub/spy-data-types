# lets define a class that implements the iterator protocol
class MySequence(object):
    def __init__(self, n):
        self.n = n
        self.i = 0

    def next(self):
        self.i += 1
        if self.i > self.n:
            raise StopIteration
        return self.i

    def __iter__(self):
        return self


# instantiate it
my_seq = MySequence(10)


# run an infinite loop
while True:
    # this should fail eventually
    elem = next(my_seq)
    print(elem)
