# The random module provides functions for generating random numbers,
# letters, random selection of sequence elements.
# https://pythonworld.ru/moduli/modul-random.html
import random
import string

# Random integer in range 1000..9999.
print('1: ' + str(random.randint(1000, 9999)))
# print(type(random.randint(1000, 9999))) # --> int

# Random number from 0 to 1.
print('2: ' + str(random.random()))
# print(type(random.random())) # --> float

# Random number from 0 to 1.
print('3: ' + str(random.uniform(1, 5)))
# print(type(random.uniform(1, 5))) # --> float

# str_len = 10  # number of characters in the random string.
# call random.choices() string module to find the string in Uppercase + numeric data.
# rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = str_len))
# print("The randomly generated string is : " + str(rand_str)) # print the random data.