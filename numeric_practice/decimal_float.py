# Import Decimal module as Dec alias
from decimal import Decimal as Dec

# Notice that when we construct a Decimal number from a float,
# it takes on all the approximation issues the float may come from.

# Decimal from float => approximation issue occurs
a = Dec(23.4)
print('\na:', a)

# Decimal from int => no approximation issue
b = Dec(25)
print('b:', b)

# Decimal from str => no approximation issue
c = Dec('34.3634')
print('c:', c)

# Calculations with float
print('\nD(0.1) * D(3) - D(0.3): ', Dec(0.1) * Dec(3) - Dec(0.3))

# Calculations with int\str
print("D('0.1') * D(3) - D('0.3'): ", Dec('0.1') * Dec(3) - Dec('0.3'), '\n')

# Decimal instances are immutable
print("c(value: 34.3634): ", id(c))
c = Dec('0.7')
print("c(value: 0.7): ", id(c))
c = Dec('34.3634')
print("c(value: 34.3634): ", id(c), '\n')