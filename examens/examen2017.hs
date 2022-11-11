eval1 :: String -> Int
eval1 expr = evalCalc stack []
    where stack = words expr

evalCalc :: [String] -> [String] -> Int
evalCalc [] [x] = read x :: Int
evalCalc (x:xs) stack
    | x == "+"  = evalCalc xs (sumRes:rest)
    | x == "-"  = evalCalc xs (minRes:rest)
    | x == "*"  = evalCalc xs (mulRes:rest)
    | x == "/"  = evalCalc xs (divRes:rest)
    | otherwise = evalCalc xs (x:stack)
        where a = head stack
              b = stack !! 1
              rest = drop 2 stack
              aInt = read a :: Int
              bInt = read b :: Int
              sumRes = show (bInt + aInt)
              minRes = show (bInt - aInt)
              mulRes = show (bInt * aInt)
              divRes = show (div bInt aInt)


eval2 :: String -> Int
eval2 s = evalX stack []
    where stack = words s


fsmap :: a -> [a -> a] -> a
fsmap x [] = x
fsmap x [f]  = f x
fsmap x (f:fs) = fsmap (f x) fs


divideNconquer :: (a -> Maybe b) -> (a -> (a, a)) -> (a -> (a, a) -> (b, b) -> b) -> a -> b
divideNconquer base divide



base :: a -> Maybe b


data Racional = Rac Integer Integer

racional :: Integer -> Integer -> Racional
racional x y =  simplify (Rac x y)

numerador :: Racional -> Integer
numerador (Rac x y ) = x

denominador:: Racional -> Integer
denominador (Rac x y) = y

simplify :: Racional -> Racional
simplify (Rac x y)
    | great == 1 = (Rac x y)
    | otherwise  = simplify (Rac (div x great) (div y great))
    where
        great = gcd x y

instance Eq Racional where
    (Rac x y) == (Rac a b) = x * b == y * a

instance Show Racional where
    show (Rac x y) = show x ++ "/" ++ show y

data Tree a = Node a (Tree a) (Tree a)
recXnivells :: Tree a -> [a]
recXnivells t = recXnivells' [t]
    where recXnivells' ((Node x fe fd):ts) = x:recXnivells' (ts ++ [fe, fd])

racionals :: [Racional]
racionals  = recXnivells (calkinwilf (Rac 1 1))

calkinwilf :: Racional -> Tree Racional
calkinwilf (Rac a b) = (Node (Rac a b) (calkinwilf (Rac a (a+b) )) (calkinwilf (Rac (a+b) b)))
