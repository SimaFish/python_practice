import string

# String constants (output type: str).

# The lowercase letters 'abcdefghijklmnopqrstuvwxyz'.
print('1: ' + string.ascii_lowercase)

# The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
print('2: ' + string.ascii_uppercase)

# The concatenation of the ascii_lowercase and ascii_uppercase constants described above.
print('3: ' + string.ascii_letters)

# The string '0123456789'.
print('4: ' + string.digits)

# The string '0123456789abcdefABCDEF'.
print('5: ' + string.hexdigits)

# String of ASCII characters which are considered punctuation characters in the C locale:
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
print('6: ' + string.punctuation)

# A string containing all ASCII characters that are considered whitespace.
# This includes the characters space, tab, linefeed, return, formfeed, and vertical tab.
print('7: ' + string.whitespace)

# String of ASCII characters which are considered printable.
# This is a combination of digits, ascii_letters, punctuation, and whitespace.
print('8: ' + string.printable)