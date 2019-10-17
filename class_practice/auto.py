# Zen of Python
import this

# The definition of a class happens with the `class` statement.
# Defining the class `Auto`.
# class Auto(object): is also an allowable definition
class Auto():
    # ToDo class attributes vs. instance attributes
    # https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide

    # The __init__() function is called automatically every time the class is being used to create a new object.
    # Use the __init__() function to assign values to object properties, or other operations
    # that are necessary to do when the object is being created. Notice two leading and trailing underscores.
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    # It does not have to be named `self`, you can call it whatever you like, but it has to be the first parameter of any function in the class.
    def __init__(self, brand, model, year=None):
        self.brand = brand
        self.model = model
        self.year = year

    # __hash__() should return the same value for objects that are equal.
    # It also shouldn't change over the lifetime of the object.
    # Generally you only implement it for immutable objects.
    def __hash__(self):
        return 1357

    # `equal`
    def __eq__(self, other):
        return not other

    # not `equal`
    def __ne__(self, other):
        return not self.__eq__(other)

    # A method is basically a function that belongs to a class.
    def get_year(self):
        if self.year is None:
            return 'Undefined'
        else:
            return str(self.year)

    def desc_auto(self):
        print('\nObject:', id(self))
        print('Auto:', self.brand + ' ' + self.model)
        print('Manufactured:', self.get_year())

# Create an instance (object) of `Auto` class.
renault_logan = Auto('Renault', 'Logan', 2011)

# Invoke method `desc_auto`.
renault_logan.desc_auto()

# `__sizeof__()` method returns the size of object in bytes
print('\nObject size (bytes):', renault_logan.__sizeof__())

# Delete the year property from the renault_logan object:
del renault_logan.year

print('\nAfter deletion of `year` attribute:')
try:
    print(renault_logan.year, '\n')
except AttributeError:
    print('`renault_logan` object no longer has attribute `year`')

# Delete the `renault_logan` object:
del renault_logan

print('\nAfter deletion of `renault_logan` object:')
try:
    print(id(renault_logan), '\n')
except NameError:
    print('`renault_logan` object is not exists', '\n')