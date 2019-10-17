# Local vs. Global vs. Enclosing
# The `LEGB` rule.
# The order in which the namespaces are scanned when looking for a name is
# therefore: local, enclosing, global, built-in (LEGB).

def enclosing_func():
    m = 13
    def local():
        # m doesn't belong to the scope defined by the local
        # function so Python will keep looking into the next
        # enclosing scope. This time m is found in the enclosing
        # scope
        print(m, 'printing from the local scope')
    
    # calling the function `local`
    local()

m = 5
print(m, 'printing from the global scope')

# calling the function `enclosing_func`
enclosing_func()