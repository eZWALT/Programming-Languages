main = do
    x<- getLine
    if (esSenseDrets x) == True then do putStrLn $  "Hola maca!" else putStrLn $ "Hola maco!"


esSenseDrets:: String -> Bool
esSenseDrets [] = False
esSenseDrets ['a'] = True
esSenseDrets ['A'] = True
esSenseDrets (x:xs) = esSenseDrets xs
