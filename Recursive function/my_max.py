# Instead of using None as default, which make it hard for others, we implement our own temp class
# 1. Create a simple Sentinel for the default value
# We use object() because it creates a unique, empty object in memory.
_MISSING = object()

def _recursive_max(items, key_func):
    """
    The internal recursive worker.
    It expects an iterable (like a list or tuple).
    """
    # 2. The "Head and Tail" Unpacking
    # This tries to split the list into the first item (head) 
    # and the rest of the list (tail).
    # If 'items' is empty, this line raises a ValueError, 
    # which we catch in the main function.
    head, *tail = items

    # 3. Base Case: The End of the Line
    # If 'tail' is empty, it means 'head' is the only item left.
    # The max of a single item is the item itself.
    if not tail:
        return head

    # 4. Recursive Step
    # Find the champion of the remaining items (the tail)
    tail_max = _recursive_max(tail, key_func)

    # 5. Comparison
    # Compare the current 'head' vs the champion of the 'tail'
    # We use the key_func to get the comparison values.
    head_val = key_func(head)
    tail_max_val = key_func(tail_max)

    if head_val > tail_max_val:
        return head
    else:
        return tail_max

def my_max(*args, key=None, default=_MISSING):
    """
    The wrapper function that handles arguments and errors.
    """
    # Prepare the key function (handle None case)
    key_func = key if key is not None else (lambda x: x)

    # 6. Distinguishing Input Modes without len()
    # Logic: Unpack the args. If 'rest' is empty, the user passed
    # a single argument (which might be a list).
    if not args:
        raise TypeError("my_max expected at least 1 argument, got 0")

    first, *rest = args

    if not rest:
        # Case A: my_max([1, 2, 3]) -> Single iterable argument
        target_items = first
    else:
        # Case B: my_max(1, 2, 3) -> Multiple arguments
        target_items = args

    # 7. Execute Recursion with Error Handling
    try:
        return _recursive_max(target_items, key_func)
    except ValueError:
        # This catches the unpacking error inside _recursive_max if the list was empty
        if default is not _MISSING:
            return default
        raise ValueError("my_max() arg is an empty sequence") from None
    except TypeError:
        # This catches cases like my_max(1) where the single item isn't iterable
        raise TypeError(f"'{type(first).__name__}' object is not iterable") from None
    

if __name__ == '__main__':
    


    #my_max = max   # uncomment to test python max

    print(my_max(2, 5))                       # 5
    print(my_max([10, 3, 60, 20]))            # 60
    print(my_max(10, 3, 6, 20))               # 20
    print(my_max({5, 7, 1}))                  # 7
    print(my_max([5, 1], [4, 9]))             # [5, 1]
    print(my_max('1234'))                     # 4
    print(my_max('1234', '98'))               # 98
    print(my_max('1234', '98', key = len))    # 1234
    print(my_max([5, 1], [4, 9], key = sum))  # [4, 9]

    # Don't show any other internal exceptions
    #print(my_max())                # TypeError: max expected 1 argument, got 0
    #print(my_max(default = -1))    # TypeError: max expected 1 argument, got 0
    #print(my_max([]))              # ValueError: max() arg is an empty sequence
    print(my_max([], default = None)) # None
    #print(my_max(-15))    # TypeError: 'int' object is not iterable
    #print(my_max(3, [4])) # TypeError: '>' not supported between instances of 'list' and 'int'