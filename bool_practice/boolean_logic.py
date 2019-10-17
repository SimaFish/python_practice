print('\nTrue behaves like 1:')
print('int(True): ' + str(int(True)))

print('\nFalse behaves like 0:')
print('int(False): ' + str(int(False)))

# True and False are subclasses of integers.
# Python upcasts them to integers and performs math operations.
# Upcasting is a type conversion operation that goes from a
# subclass to its parent. In the example presented below, True and
# False, which belong to a class derived from the integer class,
# are converted back to integers when needed.

print('\n1 + True(1): ' + str(1 + True))
print('False(0) + 42: ' + str(False + 42))
print('7 - True(1): ' + str(7 - True), '\n')