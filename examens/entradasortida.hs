

sumador :: [String] -> Int
sumador [] = 0
sumador (x:xs) = (read x) + sumador xs

main = do
    x <- getContents
    print $ sumador (words x)
