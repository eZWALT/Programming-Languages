roman2int :: String -> Int
roman2int "" = 0
roman2int [x] = c2i x
roman2int (c1:c2:l)
    | (c2i c1) < (c2i c2) = - c2i c1 + roman2int (c2:l)
    | otherwise = c2i c1 + roman2int (c2:l)

roma :: Char -> Int
roma c
    | c == 'I' = 1
    | c == 'V' = 5
    | c == 'X' = 10
    | c == 'L' = 50
    | c == 'C' = 100
    | c == 'D' = 500
    | c == 'M' = 1000

c2i :: Char -> Int
c2i c
    | c == 'I' = 1
    | c == 'V' = 5
    | c == 'X' = 10
    | c == 'L' = 50
    | c == 'C' = 100
    | c == 'D' = 500
    | c == 'M' = 1000

value :: Char -> Char -> Int
value x1 x2 = if (c2i x1) < (c2i x2) then - c2i x1 else c2i x1


roman2int' :: String -> Int
roman2int' "" = 0
roman2int' [x] = c2i x
roman2int' num = sum (zipWith value num ((tail num) ++ [(last num)]))


taylor :: Float -> Float -> Float
taylor x tx = 0.5 * (tx + (x/tx))

arrels :: Float -> [Float]
arrels x = iterate (taylor x) x

diff :: Float -> (Float, Float) -> Bool
diff e (x1, x2) = abs (x1 - x2) > e

arrel :: Float -> Float -> Float
arrel x e = snd (head (dropWhile (diff e) (zip (arrels x) (tail (arrels x)))))

data LTree a = Leaf a | Node (LTree a) (LTree a)

instance (Show a ) => Show (LTree a) where
    show (Leaf a) = "{" ++ show a ++ "}"
    show (Node (xl) (xr)) = "<" ++ show xl ++ "," ++ show xr++ ">"

build :: [a] -> LTree a
build [x] = Leaf x
build l = Node (build l1) (build l2)
    where
        len = div (length l + 1) 2
        l1 = take len l
        l2 = drop len l

zipLTrees :: LTree a -> LTree b -> Maybe (LTree (a,b))

zipLTrees (Leaf x) (Node t1 t2) = do Nothing
zipLTrees (Node t1 t2) (Leaf x) = do Nothing
zipLTrees (Leaf x) (Leaf y) = do
    return (Leaf(x,y))
zipLTrees (Node x1 x2) (Node t1 t2) = do
    a <- zipLTrees x1 t1
    b <- zipLTrees x2 t2
    return (Node (a) (b))

