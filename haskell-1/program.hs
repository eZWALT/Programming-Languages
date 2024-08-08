absValue :: Int -> Int
absValue n = if n >= 0 then n else -n

power::Int -> Int -> Int
power _ 0 = 1
power x n =
    let n_halved = div n 2
        y = power x n_halved
    in
        if even n
        then y* y
        else y * y * x


isPrime::Int -> Bool
isPrime n
    |n < 2 = False
    |otherwise = isPrime' 2

    where
        isPrime' d
            |(d*d) > n = True
            |mod n d == 0 = False
            |otherwise = isPrime' (d + 1)

slowFib::Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n - 1)  + slowFib (n - 2)

quickFib::Int -> Int
quickFib n = fst (quickFib' (n))
            where
                quickFib'::Int -> (Int, Int)
                quickFib' 0 = (0,0)
                quickFib' 1 = (1, 0)
                quickFib' n = (fst qqfib + snd qqfib, fst qqfib)
                    where
                        qqfib = quickFib' (n - 1)

