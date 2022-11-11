data Tree a = Empty | Node a (Tree a) (Tree a)
data Forest a = Forest [Tree a] deriving (Show)

instance Show a => Show (Tree a) where
    show Empty = "()"
    show (Node b (xl) (xr)) = "(" ++ show xl ++ "," ++ (show b) ++  "," ++ show xr ++ ")"

instance Functor Tree where
    fmap  f Empty  = Empty
    fmap  f (Node a (xl) (xr)) = Node (f a) (fmap f xl) (fmap f xr)

instance Functor (Forest) where
    fmap f (Forest l) = Forest (map (fmap f) l)

doubleT :: Num a => Tree a -> Tree a
doubleT x = fmap (*2) x

doubleF :: Num a => Forest a -> Forest a
doubleF x = fmap (*2) x
