stringToFloat:: String->Float
stringToFloat s = read s

indexMassaCorporal:: String->String->String->String
indexMassaCorporal n w h = n ++ ": " ++ imc (stringToFloat h) (stringToFloat w)

imc :: Float -> Float -> String
imc h w = result (w/(h*h))

result:: Float -> String
result i
    | i < 18 = "magror"
    | i < 25 = "corpulencia normal"
    | i < 30 = "sobrepes"
    | i < 40 = "obesitat"
    | otherwise = "obesitat morbida"

main = do
    st <- getLine

    if (st /= "*")
    then do
        let x = words st
        let subwords =  drop 1 x
        putStrLn $ indexMassaCorporal (head x) (head subwords) (last x)
        main
    else return()


