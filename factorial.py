class error(Exception):
    pass

def fact(n):

    if (n<0 or n>1000):
        raise error("error")
    
    
    if (n==0 or n==1):
        return 1
    
    else:
        return n * fact(n-1)
