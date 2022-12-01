def caching_fibonacci():

    cache = {0: 0, 1: 1}

    def fibonacci(n):

        if n not in cache:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)

        return cache[n]

    return fibonacci
