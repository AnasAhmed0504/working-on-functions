def my_map(func, *iterables):
    return [func(*args) for args in zip(*iterables)]

def multi_abs(a, b, c):
    return abs(a) * abs(b) * abs(c)

res = my_map(multi_abs, [1, -2, 3, 2], [-4, 5, 6, 7], [4, -5, -10, 9, 11])

print(res)  # Expected output: [16, 50, 180, 126]