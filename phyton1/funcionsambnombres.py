from functools import reduce

def absValue(x):
    if x < 0:
        return -x
    else:
         return x


def power(x,p):
    if p == 0: return 1
    if p == 1: return x
    else: return x * power(x,p-1)


def isPrime(x):
    if x == 1 or x == 0: return False
    l = [x % a != 0 for a in range(2,x-1)]
    return reduce(lambda x,y: x and y, l, True)

def slowFib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return slowFib(n-2) + slowFib(n-1)



def QuickFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        xd = exponent([0,1,1,1],n)
        return xd[2]


def product(x,y):
    return [x[0]*y[0] + x[1]*y[2] ,x[0]*y[1] + x[1] * y[3] ,x[2] * y[0]  + x[3] * y[1] , x[2] * y[1] + x[3] * y[3]]

def exponent(x,n):
    if n == 0:
        return  [1,0,1,0]
    if n == 1:
        return [0,1,1,1]
    
    y = exponent(x, n//2)
    if n%2 == 0:
        return product(y,y) 
    else:
        return product(product(y,y),x)
    