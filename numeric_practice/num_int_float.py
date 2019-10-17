import sys

# Numbers are immutable objects.
# Python integers have unlimited range, subject only to the available virtual memory.
# It doesn't really matter how big a number you want to store: as long
# as it can fit in your computer's memory, Python will take care of it.
# Integer numbers can be positive, negative, and 0 (zero).

print('\nIntegers have unlimited range (no matter how big a number you want to store):\n')
a = 873458971365982364578623987562839746587234658723645872378957239857923875275829735107589475
a = a + 3
print(a, type(a))

a = 15
b = 4

print('\nBasic arithmetic operations:\n')

# Addition
print('a + b :', a + b)

# Subtraction
print('b - a :', b - a)

# Integer division
print('a // b :', a // b)

# True division
print('a / b :', a / b)

# Multiplication
print('a * b :', a * b)

# Power operator
print('b ** a :', b ** a)

print('\nInteger division performed towards minus infinity:\n')

# Integer division features
print('7 // 4 :', 7 // 4)
print('-7 // 4 :', -7 // 4)

print('\nNotice that truncation is done towards 0:\n')

# Truncation to integer
print('int(1.75) :', int(1.75))
print('int(-1.75) :', int(-1.75))

print('\nRemainder of a division (modulo operator):\n')

# Remainder of a division, `modulo operator`
print('10 % 3 :', 10 % 3)
print('10 % 4 :', 10 % 4, '\n')

# Real numbers, or floating point numbers, are represented in Python according to the
# IEEE 754 double-precision binary floating-point format, which is stored in 64 bits of
# information divided into three sections: sign, exponent, and mantissa.