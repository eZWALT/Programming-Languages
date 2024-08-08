myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl _ a [] = a
myFoldl f a (b:bs) = myFoldl f (f a b) bs

myFoldr :: (a->b->b) -> b -> [a] -> b
myFoldr _ b [] = b
myFoldr f b (a:as) = f a (myFoldr f b as)

--
--
--
--

myIterate :: (a->a) -> a -> [a]
myIterate f a = [a] ++( myIterate f (f a))

myUntil :: (a->Bool) -> (a->a) -> a -> a
myUntil f g b
    | not $ f(b) == True = myUntil f g (g b)
    | otherwise = b

myMap :: (a->b) -> [a] -> [b]
myMap f [a] = [f a]
myMap f (a:as) = (f a):(myMap f as)

myFilter :: (a->Bool)->[a]->[a]
myFilter f [] = []
myFilter f (a:as)
    | f a == True = a: (myFilter f as)
    | otherwise = myFilter f as

myAll :: (a->Bool)->[a]->Bool
myAll f []  = True
myAll f [a] = f a
myAll f (x:xs) = (f x) && (myAll f xs)

myAny :: (a-> Bool)-> [a] -> Bool
myAny f []  = False
myAny f [a] = f a
myAny f (x:xs) = (f x) || (myAny f xs)

myZip :: [a] -> [b] ->  [(a,b)]
myZip [] a = []
myZip b [] = []
myZip (a:as) (b:bs) = [(a,b)] ++ (myZip as bs)

myZipWith:: (a->b->c) -> [a] -> [b] -> [c]

myZipWith f a b = [f a b | (a,b) <- myZip a b]
