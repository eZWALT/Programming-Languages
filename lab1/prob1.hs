absValue :: Int -> Int
absValue n
    | n>= 0 = n
    | otherwise = -n

power :: Int -> Int -> Int
power x p
    | p==0  = 1
    | p==1  = x
    | otherwise = (power x (p-1)) * x


isPrimeRecursive :: Int -> Int -> Bool
isPrimeRecursive num d
    | (d*d) > num = True
    | mod num d == 0 = False
    | otherwise = isPrimeRecursive num (d+1)

isPrime :: Int-> Bool
isPrime n
    | n < 2 = False
    | otherwise = isPrimeRecursive n 2

slowFib :: Int-> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = (slowFib (n-1) + slowFib (n-2))

quickFib::Int -> Int
quickFib n = fst (quickFib' (n))
            where
                quickFib'::Int -> (Int, Int)
                quickFib' 0 = (0,0)
                quickFib' 1 = (1, 0)
                quickFib' n = (fst qqfib + snd qqfib, fst qqfib)
                    where
                        qqfib = quickFib' (n - 1)
