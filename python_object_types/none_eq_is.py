# null object in Python
# https://stackoverflow.com/questions/3289601/null-object-in-python

class Empty(object):
    def __eq__(self, other):
        return True

# Create an instance of `Empty`
empty = Empty()

# `==` uses object's __eq__() method for comparison
# The __eq__() method opens a door that voids any guarantee of accuracy,
# since it can be overridden in a class to provide special behavior.
print('1: (==)', empty == None)

print('2: (is)', empty is None)