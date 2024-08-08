import Data.List

type Pos = (Int,Int)

dins :: Pos -> Bool
dins (x,y)
    |x > 8 = False
    |x < 1 = False
    |y > 8 = False
    |y < 1 = False
    | otherwise = True

moviments :: Pos -> [Pos]
moviments (x,y) = filter dins [(x+2,y+1), (x+2,y-1), (x-2,y-1),(x-2,y+1),(x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2)]

apply3:: (b->b) -> b -> b
apply3 f = f . f . f


potAnar3 :: Pos -> Pos -> Bool
potAnar3 (x,y) (xa,xb) =  elem (xa,xb) $  (apply3 (concatMap moviments) [(x,y)] )

potAnar3' :: Pos -> Pos -> Bool
potAnar3' (x,y)  (a,b) = elem(a,b) $ (apply3 (\a -> a >>= moviments) [(x,y)])

