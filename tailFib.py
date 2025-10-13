def tailFib(n,a,b):
    if n == 0:
        return a

    else:
        return tailFib(n-1,b,a+b)


def fib(n):

    return tailFib(n,0,1)
        
