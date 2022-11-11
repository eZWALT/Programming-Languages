
ones :: [Integer]
ones = iterate (+0) 1

nats :: [Integer]
nats = iterate (+1) 0

aux :: [Integer]
aux = iterate (+1) 1


ints :: [Integer]
ints = [0]++ (concat (map (\x -> [x,-x]) aux ))


triangulars :: [Integer]
triangulars =  (scanl (+) 0 aux)

factorials :: [Integer]
factorials = scanl (*) 1 aux

fibs :: [Integer]
fibs =  map  fst $ (iterate (\(a,b) -> (b,a+b))) (0,1)

isPrimeRecursive :: Integer -> Integer -> Bool
isPrimeRecursive num d
    | (d*d) > num = True
    | mod num d == 0 = False
    | otherwise = isPrimeRecursive num (d+1)

isPrime :: Integer-> Bool
isPrime n
    | n < 2 = False
    | otherwise = isPrimeRecursive n 2

--primes ::  [Integer]
--primes = filter (isPrime) aux

primes :: [Integer]
primes = esPrimer [2..]
    where esPrimer (p : ps) = p : esPrimer [x | x <- ps, mod x p /= 0]

hammings :: [Integer]
hammings = 1 : merge (map (2*) hammings) (map (3*) hammings ) (map (*5) hammings)

merge :: [Integer]->[Integer]->[Integer]->[Integer]
merge x y z = merge2 x (merge2 y z)

merge2 :: [Integer]->[Integer]->[Integer]
merge2 x [] = x
merge2 [] y = y
merge2 (x:xs) (y:ys)
    |x < y = x : merge2 xs (y:ys)
    |x > y = y : merge2 (x:xs) ys
    |otherwise = x : merge2 xs ys
