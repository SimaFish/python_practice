# A tuple is a sequence of arbitrary Python objects.
# It is an immutable sequence type.
# https://www.programiz.com/python-programming/list-vs-tuples

# Create empty tuple using tuple literal
tupl = ()

# Create empty tuple using built-in tuple() function
tupl = tuple()

# Assign values to a tuple instance.
# Notice that to create a tuple with one item, we need to put that comma
# after the item. The reason is that without the comma that item is just itself
# wrapped in braces, kind of in a redundant mathematical expression.
tupl = ('a', ) # you need the comma!
tupl = ('a', 'b')
tupl = ('a', 3, 46.525)

for item in tupl:
    print('value: ', item, '\n')