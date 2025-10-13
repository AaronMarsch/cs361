class error(Exception):
    pass


def fib(n):

    
    if n < 0 or n > 45:
        raise error("error")
    
    if n <= 1:
        return n

    
    else:
        return fib(n - 1) + fib(n - 2)



