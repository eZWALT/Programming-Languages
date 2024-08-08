
insert:: [Int]-> Int -> [Int]
insert [] a = [a]
insert (x:xs) d
    | d <= x = d: x : xs
    | otherwise  = x : (insert xs d)

isort :: [Int]->[Int]
isort [] = []
isort (d:xd)  = insert (isort xd) d

remove :: [Int] -> Int -> [Int]
remove (x:xs) a
    | x == a    = xs
    | otherwise = x :(remove xs a)

ssort :: [Int]->[Int]
ssort [] = []
ssort x = chiquito:ssort (remove x chiquito)
    where
        chiquito = minimum(x)

merge:: [Int] -> [Int] -> [Int]
merge [] [] = []
merge [] x = x
merge x [] = x
merge (a:as) (b:bs)
    | a <= b  = a : (merge as (b:bs))
    | otherwise = b : (merge (a:as) bs)

msort:: [Int] -> [Int]
msort [] = []
msort [x] = [x]
msort arr = merge (msort left) (msort rigth)
    where
        left = take mid  arr
        rigth = drop (mid) arr
        mid =  div (length arr) 2

qsort :: [Int] -> [Int]
qsort [] = []
qsort (x:xs) = ((qsort (menors xs x)) ++ [x] ++ (qsort (majors xs x) ))


menors :: Ord a => [a] -> a -> [a]
menors [] x = []
menors llista x = [k | k <- llista, k <= x]

majors :: Ord a => [a] -> a -> [a]
majors [] x = []
majors llista x = [k | k <- llista, k > x]

genQsort :: Ord a => [a] -> [a]

genQsort [] = []
genQsort (x:xs) = (genQsort (menors xs x)) ++ [x] ++ (genQsort (majors xs x))
