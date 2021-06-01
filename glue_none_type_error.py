import re # required module for regexps
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

try:
    print(None + None)
    # print(None - None)
except TypeError as error:
    if re.search("unsupported operand type\(s\) for", str(error)) and \
        re.search(r"\'NoneType\' and \'NoneType\'", str(error)):
        # Do something when None (operand) None
        pass