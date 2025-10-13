def fib_int(n):
    if n == 1:
        return 1

    elif n == 0:
        return 0

    else:
        temp = 0
        dummy = 1
        for i in range(n-1):
            fibonauci = temp + dummy
            temp = dummy
            dummy = fibonauci

        return dummy
