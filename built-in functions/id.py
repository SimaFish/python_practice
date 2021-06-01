# The id() function returns a unique id for the specified object.
# All objects in Python has its own unique id.
# The id is assigned to the object when it is created.
# Is derived from the address of the object in memory.

# All references with the same value point to the same object (id)
foo = 1
bar = foo
baz = bar

fii = 1 # same as foo-bar-baz

# Variables with the same id's
print('foo:', id(foo))
print('bar:', id(bar))
print('baz:', id(baz))

# same as foo-bar-baz
print('fii:', id(fii))

# Immutable int objects point to different id's
age = 42
print('age(42):', id(age))

age = 43
print('age(43):', id(age))