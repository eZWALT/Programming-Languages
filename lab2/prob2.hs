
flatten:: [[Int]]->[Int]
flatten [[]] = []
flatten a = foldl (++) [] a

myLength :: String-> Int
myLength r = foldl (\x _ -> x+1) 0 r

myReverse :: [Int] -> [Int]
myReverse n = foldl (\x xs -> xs:x) [] n

countIn :: [[Int]]-> Int -> [Int]
countIn l x = map (length . (filter (==x))) l

firstWord :: String->String
firstWord s = (takeWhile(/=' ') .   (dropWhile(== ' '))) s
