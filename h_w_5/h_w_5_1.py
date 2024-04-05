def caching_fibonacci():
    """Function that finds Fibonaci number from given number
        by using recursion and 
        with usage of cache memory,
        if number was already calculated that there is answer in cache
        so it won't be calculated again"""
    fibonacci_cache = dict()

    def fibonacci(num):
        if num in fibonacci_cache:
            return fibonacci_cache[num]
        if num == 1:
            return 1
        elif num == 0:
            return 0
        elif num in fibonacci_cache:
            return fibonacci_cache[num]
        else:
            fibonacci_cache[num] = fibonacci(num - 1) + fibonacci(num - 2)
            return fibonacci(num)
    return fibonacci


fibo = caching_fibonacci()
print(fibo(6))
print(fibo(7))
