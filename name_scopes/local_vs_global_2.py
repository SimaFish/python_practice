# Local vs. Global
# The `LEGB` rule.
# The order in which the namespaces are scanned when looking for a name is
# therefore: local, enclosing, global, built-in (LEGB).

# define a function, called `local`
def local():
    print(m, 'printing from the global scope') # printing `m` from global scope

m = 5 # `m` in global scope
print(m)

# calling the function `local`
local()