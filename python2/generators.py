 
def fibs():
    a = 0
    yield a
    b = 1

    while True:
        yield b
        a,b = b, a+b

def roots(x):
    a = x
    yield a 

    while True:
        a = 1/2 * (a + x/a)
        yield a

def primes():
    a = 2
    yield a 
    while True:
        a = a + 1
        if(isPrime(a)):
            yield a

def isPrime(x):
    i = 2
    while i*i <= x:
        if(x%i == 0):
            return False
    return True
