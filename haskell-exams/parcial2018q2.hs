import Data.List

multEq :: Int -> Int -> [Int]
multEq x y =  iterate (*(x*y)) 1

selectFirst :: [Int] -> [Int] -> [Int] -> [Int]
selectFirst [] _ _ =  []
selectFirst _  [] _ = []
selectFirst l1 l2 [] = filter (\x-> elem x l2 ) l1
selectFirst l1 l2 l3 = filter (\x -> not (elem x l3 ) || ((elem x l2 ) && ((elemIndex x l2) < (elemIndex x l3)))  ) l1

myIterate :: (a->a) -> a -> [a]
myIterate f a = scanl (\x a -> f x) a (repeat a)

type SymTab a = String -> Maybe a

empty :: SymTab a
empty  =  (\x -> Nothing)

get :: SymTab a -> String -> Maybe a
get t s = (t s)

set :: SymTab a -> String -> a -> SymTab a
set t k v x
    | k == x = return v
    | otherwise = get t x

data Expr a
    = Val a
    | Var String
    | Sum (Expr a) (Expr a)
    | Sub (Expr a) (Expr a)
    | Mul (Expr a) (Expr a)
    deriving Show

eval :: (Num a) => SymTab a -> Expr a -> Maybe a
eval t (Val a) = return a
eval t (Var s) = get t s
eval t (Sum e1 e2) = do
    e1x <- eval t e1
    e2x <- eval t e2
    return (e1x + e2x)
eval t (Sub e1 e2) = do
    e1x <- eval t e1
    e2x <- eval t e2
    return (e1x - e2x)
eval t (Mul e1 e2) = do
    e1x <- eval t e1
    e2x <- eval t e2
    return (e1x * e2x)
