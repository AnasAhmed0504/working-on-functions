def my_reduce(func, iterable, init = None):
    if not iterable:
        if init is None:
            raise TypeError("my_reduce() of empty sequence with no initial value")
        return init
    
    for item in iterable:
        if init is None:
            init = item

        else:
            init = func(init, item)
    
    return init
            
        

print(my_reduce(lambda x, y: x if x > y else y, [7, 20, 10, 3]))  # Expected output: 20
print(my_reduce(max, [7, 20, 10, 3]))  # Expected output: 20