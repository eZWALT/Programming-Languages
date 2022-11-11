from functools import reduce
def myLength(L):
    
    l = 0
    for i in L:
        l += 1
    return l

def myMaximum(L):
    max = L[0]
    for i in L:
        if i > max:
            max = i
    return max

#[start: end : stride]
#[::-1]

def average(L):

    return (reduce (lambda x, y: x+y, L, 0)) / myLength(L)

def buildPalindrome(L):
    return L[::-1] + L    

def remove(L1,L2):
    return [x for x in L1 if not x in L2]

def oddsNevens(L):
    return [x for x in L if x%2 != 0], [x for x in L if x%2 == 0]