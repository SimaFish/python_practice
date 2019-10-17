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

# Count particular item occurrence
print("\nlist_a 'a' count:", list_a.count('a'))

list_c = [1, 'a']

# Append object to the end of the list
list_c.append(3.1445) # append float
list_c.append((2, 4)) # append tuple
list_c.append(['test', 'hello']) # append list

print('\nlist_c:', list_c, '\n')

# Iteration over list items
for item in list_c:
    print(item, type(item))

# Extend the list by another (or sequence).
# Notice the difference between the `append` and `extend`.
list_d = [1, 2, 3]
tuple_a = (4, 5, 6)
list_e = [7, 8, 9]

# You can extend lists using any sequence type
list_d.extend('test') # extend by string
list_d.extend(tuple_a) # extend by tuple
list_d.extend(list_e) # extend by list

print("\nlist_d (extended):", list_d)

# Sort the items in the list
list_f = [5, 13, 3, 2, 21, 1, 4, 3, 8]
list_f.sort()

print('\nlist_f (sorted):', list_f)

# Reverse the order of the elements in the list
list_f.reverse()

print("list_f (reversed):", list_f)

# Position of `3` in the list (0-based indexing)
print("list_f (index of 3):", list_f.index(3))

# Remove all elements from the list
list_c.clear()

print('\nlist_c (cleared):', list_c, '\n')