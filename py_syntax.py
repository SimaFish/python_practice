# Imports should usually be on separate lines.
# Imports are always put at the top of the file, just after any module comments and docstrings,
# and before module globals and constants.
import sys
import os

# single-line comment
"""
Don't use triple-quotes; as you discovered, this is for documentation strings not block comments,
although it has a similar effect. If you're just commenting things out temporarily,
this is fine as a temporary measure. Prepend a # to each line to block comment.
Python 3 disallows mixing the use of tabs and spaces for indentation.
"""

# Indentation. Use 4 spaces per indentation level.
# if sys.platform == 'win32':
    # print("Hello, world!")

var_num = 999
print(type(var_num))