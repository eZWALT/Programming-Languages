import Data.List


degree:: Eq a => [(a,a)] -> a -> Int
degree [] _ = 0
degree ( (x,y) : xs) a
    | x == a || y == a = (degree xs a) + 1
    | otherwise = degree xs a


degree':: Eq a => [(a,a)] -> a -> Int
degree' x b = length ( filter (\(x,y) -> x == b || y == b) x)

neighbors :: Ord a => [(a,a)] -> a -> [a]
neighbors x b = sort ((filter (/=b) segon) ++ (filter (/= b) primer))
    where llista = filter (\(x,y) -> x == b || y == b) x
          primer = fst $  unzip llista
          segon  = snd $  unzip llista
