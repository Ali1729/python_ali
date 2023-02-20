
var = 3000
def outer_func():
    print(var) # this is global scope.
    # This block is the Local scope of outer_func()
    
    var = 100  # A nonlocal var
    # It's also the enclosing scope of inner_func()
    def inner_func():
        var = 10
        # This block is the Local scope of inner_func()
        print(f"Printing var from inner_func(): {var}")

    inner_func()
    print(f"Printing var from outer_func(): {var}")