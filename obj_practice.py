# Create a new object
obj = {}

# Create a new object with key-value pairs
obj = {'key1': 'value1',
       'key2': 'value2',
       'key3': 'value3'}

# Iterate over object keys
for key in obj.keys():
    print(key)

# Iterate over object values
for val in obj.values():
    print(val)

# Access to object attribute by key
print(obj.get('key3')) # => value3
print(obj.get('key4')) # => None

# Check if certain attribute exists
if hasattr(obj, 'key4'):
    print("Attribute 'key4' exists!")
else:
    print("Attribute 'key4' NOT exists..")



# new_obj = {}
# new_obj.key5 = 'value5'





# print(getattr(obj, 'key2'))






