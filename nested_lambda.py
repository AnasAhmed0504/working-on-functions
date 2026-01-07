
sq = lambda x: x * x

def ff(st, en, step):
    def inner(f):
        return [f(val) for val in range(st, en, step)]
    return inner

processor = ff(2, 6, 1)

print(processor(sq))


# using nested lambda functions

ff2 = lambda st, end, step: lambda f: [f(v) for v in range(st, end, step)]
processor2 = ff2(2, 6, 1)
print(processor2(sq))