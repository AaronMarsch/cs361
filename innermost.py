def f(n,m):
    if n == 0:
        return 0
    else:
        return f(n-1, f(n,m))


#python uses innermost recursion
