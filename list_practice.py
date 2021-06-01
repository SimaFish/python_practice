# Python lists are mutable sequences.
# As with tuples, list items are comma separated.
# Lists use 0-based indexing for accessing to elements.
# https://www.programiz.com/python-programming/list-vs-tuples

# Create empty list using tuple literal
list_a = []

# Create empty list using built-in list() function
list_b = list()

# Make a list from a string
list_b = list('hello')

print('\nlist_b (from str):', list_b)

# Assign values to a list instance.
list_a = ('a', 'b', 4, 5, 4)
list_a = ['a', 3, 46.525, (3, 4, 5), 'a', 'a']

print('\nlist_a:', list_a)

# Python is magic. That is called a `list comprehension`
list_b = [(x + 5) ** 2 for x in (2, 3, 4)]

print('list_b (magic):', list_b)

# Count the total quantity of items
print('\nlist_a count:', len(list_a))
print('list_b count:', len(list_b))

# The `count()` method counts how many times
# an element has occurred in a list.
# https://www.programiz.com/python-programming/methods/list/count
print("\nlist_a 'a' count:", list_a.count('a'))

list_c = [1, 'a']

# The `append()` method adds a single item to the existing list.
# It doesn't return a new list; rather it modifies the original list.
# Takes a single item and adds it to the end of the list.
# The item can be numbers, strings, another list, dictionary etc.
# https://www.programiz.com/python-programming/methods/list/append
list_c.append(3.1445) # append float
list_c.append((2, 4)) # append tuple
list_c.append(['test', 'hello']) # append list

print('\nlist_c:', list_c, '\n')

# Iteration over list items
for item in list_c:
    print(item, type(item))

# The `extend()` method extends the list by adding all items
# of a sequence (str/tuple/list), passed as an argument,
# to the end of the currrent list.
# Notice the difference between the `append` and `extend`.
# https://www.programiz.com/python-programming/methods/list/extend
list_d = [1, 2, 3]

print("\nlist_d:", list_d)

tuple_a = (4, 5, 6)
list_e = [7, 8, 9]

# You can extend lists using any sequence type
list_d.extend('test') # extend by string
list_d.extend(tuple_a) # extend by tuple
list_d.extend(list_e) # extend by list

print("list_d (extended):", list_d)

# The `sort()` method sorts the elements of a given list
# in a specific order - Ascending (default) or Descending.
# https://www.programiz.com/python-programming/methods/list/sort
list_f = [5, 13, 3, 2, 21, 1, 4, 3, 8]
print('\nlist_f (original):', list_f)

# Sort the list in the ascending order.
list_f.sort()

print('list_f (sorted ascending):', list_f)

# Sort the list in the descending order.
list_f.sort(reverse=True)

print('list_f (sorted descending):', list_f)

print('\nlist_d (original):', list_d)

# Reverse the order of the elements in the list.
# The `reverse()` method doesn't return any value.
# It only reverses the elements and updates the list.
# https://www.programiz.com/python-programming/methods/list/reverse
list_d.reverse()

print("list_d (reversed):", list_d)

# The `index()` method finds the given element in a list and returns its position.
# If the same element is present more than once, `index()` method
# returns its smallest/first position.
# If not found, it raises a `ValueError` exception
# indicating the element is not in the list.
# https://www.programiz.com/python-programming/methods/list/index

print('\nlist_f:', list_f)

# Position of `3` in the list (0-based indexing)
try:
    print("list_f (index of 3):", list_f.index(3))
except ValueError:
    print('Searched element is not in the list')

# programming language list
lang = ['Python', 'Java', 'C++', 'PL/SQL']
print('\nlang:', lang)

# The `pop()` method returns the item present at the given index.
# This item will be removed from the list.
# https://www.programiz.com/python-programming/methods/list/pop

print('lang pop(1): ', lang.pop(1))
print('lang pop(3): ', lang.pop(1))

print('lang:', lang)

# The `clear()` method removes all items from the list.
# https://www.programiz.com/python-programming/methods/list/clear
list_c.clear()

print('\nlist_c (cleared):', list_c, '\n')