countIf :: (Int ->Bool) -> [Int] -> Int
countIf f a = length(filter f a )

pam :: [Int]-> [Int-> Int]->[[Int]]
pam a [] =[]
pam a (f:fs) = [map f a] ++ pam a fs


pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 xs fs = [map (flip ($) x) fs | x<-xs ]

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl f g xo llista = foldl g xo [ x | x<-llista  , f x == True]



insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert f [] a = [a]
insert f (x:xs) a
    | (f x a)   = x : insert f xs a
    | otherwise = a : x : xs

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort f [] = []
insertionSort f (x:xs) = (insert f (insertionSort f xs) x )


