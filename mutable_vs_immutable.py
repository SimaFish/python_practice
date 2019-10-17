# Immutable int object:
age = 42
print('age(42):', id(age))

age = 45
print('age(45):', id(age))

age = 42
print('age(42):', id(age))

# Mutable Person class:
class Person:
    def __init__(self, age):
        self.age = age

vasya = Person(38)
print('Person(38):', id(Person))

vasya.age = 46
print('Person(46):', id(Person))

# Mutable test object:
# test_obj = {}
# print(type(test_obj))

# test_obj.__setattr__('age', 34)
# print('Test_obj(34):', id(test_obj))

# test_obj.__setattr__('age', 40)
# print('Test_obj(40):', id(test_obj))