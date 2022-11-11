data Tree a = Empty | Node a (Tree a) (Tree a)
    deriving (Show)

instance Foldable Tree where
    foldr f b Empty = b
    foldr f b (Node a (al) (ar)) = f a (foldr f (foldr f b ar) al )


avg :: Tree Int -> Double
avg t = (/) (fromIntegral (sum t)) (fromIntegral(length t))

cat :: Tree String -> String
cat Empty = ""
cat t =  init $ (foldr (\x y -> x ++ " " ++ y) "" t)
