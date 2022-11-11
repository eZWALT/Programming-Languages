
divisors :: Int -> [Int]
divisors a = [x | x <- [1..a], (mod a x) == 0]

nbDivisors :: Int -> Int
nbDivisors a = length $ divisors a

moltCompost :: Int -> Bool
moltCompost x = elem (x,maxxx) ((filter (\(x,y) -> x == maxxx) llista))
    where
        llista = [((nbDivisors z ), z) | z <- [1..x]]
        maxxx = fst $ maximum llista
