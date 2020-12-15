
def factorial_iter(n):
    result = 1
    for i in range(2,n+1):
        result *= i

    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n* factorial_recursive(n-1)


def Pmt(n,r):
    result = 1
    for i in range(n, n-r, -1):
        result *= i
    return result



def Cbn(n, r):

    result = Pmt(n, r)

    for i in range(r, 1, -1):
        result //= i
    return result

def fac(n):
    result = n
    
