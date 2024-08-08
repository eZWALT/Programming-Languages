myLength:: [Int] -> Int
myLength n
    | n == []   = 0
    | otherwise = myLength (init(n)) + 1

--init saca el ultimo elemento i head saca el primero, da igual cual se use en este caso


myMaximum :: [Int] -> Int
myMaximum [x] = x
myMaximum (x:xs)
  | x > max = x
  | otherwise = max
  where
    max = myMaximum xs

average :: [Int] -> Float
average [x] = fromIntegral x
average (x:xs) = fromIntegral(x+suma(xs))/fromIntegral(myLength(xs)+1)
    where
        suma :: [Int]-> Int
        suma [x] = x
        suma (x:xs) = x + suma(xs)


buildPalindrome :: [Int] -> [Int]
buildPalindrome x = revertir(x) ++ x
    where
        revertir :: [Int]->[Int]
        revertir [] = []
        revertir (x:xs) =  revertir(xs) ++ [x]

remove :: [Int]->[Int]->[Int]
remove [] _ = []
remove (x:xs) y
    | elem x y = remove xs y
    | otherwise = x : (remove xs y)

flatten:: [[Int]]->[Int]
flatten [] = []
flatten (x:xs) = x ++ flatten(xs)

oddsNevens :: [Int] -> ([Int],[Int])
oddsNevens [] = ([],[])
oddsNevens (x:llista)
    |even x = (fst(seg), x:snd(seg))
    |odd  x = (x:fst(seg), snd(seg))
    where
        seg = oddsNevens(llista)

primeDivisors :: Int -> [Int]
primeDivisors n = [divs | divs <- [1..n], mod n divs == 0, esPrimer divs]

esPrimer:: Int->Bool
esPrimer n
    |n < 2 = False
    |otherwise = not (teDivisors n 2)
    where
        teDivisors :: Int->Int->Bool
        teDivisors n divisor
            |divisor * divisor > n = False
            |mod n divisor == 0 = True
            |otherwise = teDivisors n (divisor+1)
