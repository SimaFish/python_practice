import re # need for "initcap" function
import string as st # need for "capwords" function
import jellyfish as jf # need for "soundex" function
import random as rd

# Sets the first character in each word to uppercase and the rest to lowercase
# https://docs.python.org/3/library/stdtypes.html#string-methods str.title()
def initcap(str):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0].upper() +
                             mo.group(0)[1:].lower(),
                  str)

# Returns a string with all occurrences of each character specified
# in another string as 2nd argument replaced by its corresponding character
# specified in the 3rd argument.
def translate(str, str_chrs, rep_chrs):
    str_len = len(str_chrs)
    rep_len = len(rep_chrs)
    if str_len == 0 or rep_len == 0:
        return ''
    len_diff = str_len - rep_len
    if len_diff > 0:
        trans_tab = str.maketrans(str_chrs[:rep_len], rep_chrs, str_chrs[rep_len:])
    elif len_diff < 0:
        trans_tab = str.maketrans(str_chrs, rep_chrs[:str_len], rep_chrs[str_len:])
    else:
        trans_tab = str.maketrans(str_chrs, rep_chrs)
    return str.translate(trans_tab)

# Replaces a sequence of characters in a string
# with another set of characters
def replace(str, sub_str, rep_str=''):
    return str.replace(sub_str, rep_str)

# Counts the number of times a substring occurs in a string
def substr_count(str, sub_str):
    try:
        substr_cnt = round((len(str) - len(str.replace(sub_str, ''))) / len(sub_str))
    except ZeroDivisionError:
        substr_cnt = 0
    finally:
        return substr_cnt

# Converts all letters in the specified string to lowercase
def lower(str):
    return str.lower()

# Converts all letters in the specified string to uppercase
def upper(str):
    return str.upper()

# Returns the input string in its reverse order
# https://stackoverflow.com/questions/931092/reverse-a-string-in-python
def reverse(str):
    return str[::-1]

# Pads the left-side of a string
# with a specific set of characters
def lpad(str, len, chr=' '):
    return str.rjust(len, chr)

# Pads the right-side of a string
# with a specific set of characters
def rpad(str, len, chr=' '):
    return str.ljust(len, chr)

# Returns the length of the specified string
def length(str):
    return len(str)

# Removes all specified characters
# from the left-hand side of a string
def ltrim(str, trm_chr=' '):
    return str.lstrip(trm_chr)

# Removes all specified characters
# from the right-hand side of a string
def rtrim(str, trm_chr=' '):
    return str.rstrip(trm_chr)

# Removes all specified characters either
# from the beginning or the end of a string
def trim(str, trm_chr=' '):
    return str.strip(trm_chr)

# Returns a phonetic representation
# (the way it sounds) of a string.
def soundex(str):
    return jf.soundex(str)

# String variable declaration
msg_string = 'hello world'
# print(msg_string)

# LOWER
# print('Lowercase_1: ' + msg_string.lower())
# print('Lowercase_2: ' + lower(msg_string))

# UPPER
# print('Uppercase_1: ' + msg_string.upper())
# print('Uppercase_2: ' + upper(msg_string))

# REVERSE
# print('Reversed_1: ' + msg_string[::-1])
# print('Reversed_2: ' + reverse(msg_string))

# LPAD
# print('Left_padded_1: ' + msg_string.rjust(15))
# print('Left_padded_2: ' + lpad(msg_string, 15))
# print('Left_padded_3: ' + msg_string.rjust(15, '#'))
# print('Left_padded_4: ' + lpad(msg_string, 15, '#'))

# RPAD
# print('Right_padded_1: ' + msg_string.ljust(15))
# print('Right_padded_2: ' + rpad(msg_string, 15))
# print('Right_padded_3: ' + msg_string.ljust(15, '#'))
# print('Right_padded_4: ' + rpad(msg_string, 15, '#'))

# INITCAP
# print('Initcap_1: ' + msg_string.title())
# print('Initcap_2: ' + initcap("they're bill's friends from the UK"))
# print('Initcap_3: ' + st.capwords('this   is a test'))

# TRANSLATE
# print(translate('1tech23 on the net', '123th', '456'))

# LENGTH
# print('Length_1: ' + str(len(msg_string)))
# print('Length_2: ' + str(length(msg_string)))

# LTRIM
# print('Left trim_1: "' + ltrim('   spacious   ') + '"')
# print('Left trim_2: "' + ltrim('00000000spacious  ', '0') + '"')

# RTRIM
# print('Left trim_1: "' + rtrim('   spacious   ') + '"')
# print('Left trim_2: "' + rtrim('  spacious00000000', '0') + '"')

# TRIM
# print('Trim_1: "' + trim('   spacious   ') + '"')
# print('Trim_2: "' + trim('000000spacious0000', '0') + '"')

# SOUNDEX
# print('Soundex_1: ' + soundex('Ala ma kaca'))
# print('Soundex_2: ' + soundex('Hello, Test123'))

# REPLACE
# print('Replace_1: "' + replace('Hello, world, Hello, TestHello', 'Hello') + '"')
# print('Replace_2: "' + replace('Hello, world, Hello, TestHello', 'Hello', '###') + '"')

# SUBSTR_COUNT
# print(substr_count('Hello, World! Test1234 Hello56', 'Hello'))

# print(round(2.655, 2))
# print(Decimal.from_float(0.1))
# print(math.fsum([0.1, 0.3, 0.2, 0.4]) == .1)
# print(math.fsum([0.1] * 10))

# isinstance
# print(0.1*10 == 1.0)

# if type(0.1*10) == float:
#     print('Yes!')
# else:
#     print('No..')

# keys = ['Safe', 'Bob', 'Thomas']
# values = ['Hammad', 'Builder', 'Engine']
# for i in zip(keys, values):
#     print(type(i))

# print(rd.random())