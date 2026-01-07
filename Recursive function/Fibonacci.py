memory = {}

def fibonacci(n):
    #fibonacci(n) == fibonacci(n-1) + fibonacci(n-2)
    #fibonacci(6) == fibonacci(5) + fibonacci(4)

    if n <= 1:
        return 1

    global memory
    if n in memory:
        return memory[n]
    
    memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]


if __name__ =='__main__':
    print(fibonacci(5))
    print(fibonacci(50))
    print(fibonacci(500))