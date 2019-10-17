# Local vs. Global
# The `LEGB` rule.
# The order in which the namespaces are scanned when looking for a name is
# therefore: local, enclosing, global, built-in (LEGB).

# define a function, called `local`
def local():
    m = 7 # `m` in local scope
    print(m)

m = 5 # `m` in global scope
print(m)

# calling the function `local`
local()