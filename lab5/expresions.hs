data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

eval1:: Expr -> Int
eval1 (Val x) = x
eval1 (Add x y) = (eval1 x) + (eval1 y)
eval1 (Sub x y) = (eval1 x) - (eval1 y)
eval1 (Mul x y) = (eval1 x) * (eval1 y)
eval1 (Div x y) = div (eval1 x) (eval1 y)

eval2:: Expr -> Maybe Int
eval2 (Val x) = Just x
eval2 (Add x y) = liftM2 (+) (eval2 x) (eval2 y)
eval2 (Sub x y) = liftM2 (-) (eval2 x) (eval2 y)
eval2 (Mul x y) = liftM2 (*) (eval2 x) (eval2 y)
eval2 (Div x y) = do
        x1 <- (eval2 x)
        x2 <- (eval2 y)
        if x2 == 0 then Nothing
        else return (div x1 x2)

eval3:: Expr -> Either String Int
eval3 (Val x) = Right x
eval3 (Add x y) = liftM2 (+) (eval3 x) (eval3 y)
eval3 (Sub x y) = liftM2 (-) (eval3 x) (eval3 y)
eval3 (Mul x y) = liftM2 (*) (eval3 x) (eval3 y)
eval3 (Div x y) = do
        x1 <- (eval3 x)
        x2 <- (eval3 y)
        if x2 == 0 then Left "div0"
        else return (div x1 x2)



liftM :: Monad m => (a->b) -> m a -> m b
liftM f a = do
        x1 <- a
        return $ f x1


liftM2 :: Monad m => (a->b->c) -> m a -> m b -> m c
liftM2 f a b = do
        x1 <- a
        x2 <- b
        return  $ f x1 x2





liftM2 :: Monad m => (a->b->c) -> m a -> m b -> m c
liftM2 f a b = do
        x <- a
        y <- b
        return $ f a b
