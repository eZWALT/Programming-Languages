
sumMultiples35::Integer->Integer
sumMultiples35 a = sum(l)
    where l = [x | x <- [1..a-1], ((mod x 3 == 0) || (mod x 5 == 0))]



fibonacci:: Int->Integer
fibonacci 1 =  0
fibonacci 2 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

fibonacciEvens:: Int->[Int]
