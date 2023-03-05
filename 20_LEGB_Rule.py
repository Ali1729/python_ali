
var = 3000
def outer_func_1():
    var = 5000
    def outer_func():
        # This block is the Local scope of outer_func()
        # var = 100  # A nonlocal var
        # It's also the enclosing scope of inner_func()
        # for i in range(1):
        #     var = 200
            
        def inner_func():
            var = 10
            # This block is the Local scope of inner_func()
            print(f"Printing var from inner_func(): {var}")

        inner_func()
        print(var)
        print(f"Printing var from outer_func(): {var}")

    outer_func()

outer_func_1()
print(f"Printing var from outside(): {var}")

    # Local
    # Enclosing
    # Global
    # Builtin